# initialize vegans
import torch
import huggingface_hub

from .generator import Generator
from .discriminator import Discriminator
from .utils import save_image, display_image, log, generate_noise
from .dataset import TrainingSet
from .config import Config


class Vegans:
    def __init__(self, config: Config, dataset):
        assert config is not None
        self.config = config
        self.dataset = dataset
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.generator = Generator().to(self.device)
        self.discriminator = Discriminator().to(self.device)
        self.g_optim = torch.optim.Adam(
            self.generator.parameters(),
            lr=self.config.learning_rate,
            betas=self.config.betas,
        )
        self.d_optim = torch.optim.Adam(
            self.discriminator.parameters(),
            lr=self.config.learning_rate,
            betas=self.config.betas,
        )

    def train(self, upload=False, real=True):

        loss_fn = torch.nn.BCELoss()
        log("Started Training Loop")
        if real:
            dataset = self.dataset
        else:
            dataset = self._dummy_dataset()

        for epoch in range(self.num_epoch):
            for i, (image, label) in enumerate(dataset):

                # Train the generator
                self.g_optim.zero_grad()

                loss = loss_fn(0, 0)

                # Train the discriminator
                self.d_optim.zero_grad()

            log(f"Epoch {epoch} done. Loss is {loss.item()}")

        log("Finish Training")
        if upload:
            self.generator.save_pretrained("ve-gans")
            self.generator.push_to_hub("ve-gans")

    def eval(self):
        pass

    def _dummy_dataset(self):
        dummy_images = []
        dummy_labels = []
        for i in range(100):
            image = torch.randn(
                1, self.config.channels, self.config.image_size, self.config.image_size
            )
            label = torch.randint(0, 2, (1,))
            dummy_images.append(image)
            dummy_labels.append(label)
        return [(image, label) for image, label in zip(dummy_images, dummy_labels)]

    def generate(self, label, save=True):
        # TODO
        noise = generate_noise()
        output = self.generator(noise, label)
        if save:
            save_image(output)
        return output

    def save_pretrained(self, name="ve-gans"):
        print("Uploading model...")
        self.model.save_pretrained(name)
        print(f"Model saved locally as '{name}'")
        self.model.push_to_hub(name)
        print(f"Model '{name}' uploaded to the Hugging Face Model Hub")

    def load_pretrained(self, model_id="zaibutcooler/ve-gans"):
        print("Loading model...")
        model = model.from_pretrained(model_id)
        print(f"Model '{model_id}' loaded successfully")
        return model
    
    def huggingface_login(self,token):
        huggingface_hub.login(token)