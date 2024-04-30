from torch.utils.data import Dataset
from torchvision import transforms as tran
from datasets import load_dataset
from .utils import log
from .config import Config


class TrainData(Dataset):
    def __init__(self, config: Config, gray_scale=True):
        super().__init__()

        self.transforms = tran.Compose(
            [
                tran.Resize((config.image_size, config.image_size)),
                tran.ToTensor(),
                tran.Normalize([0.5], [0.5]),
                tran.Grayscale() if gray_scale else None,
            ]
        )
        self.images = None
        self.labels = None
        self.download_dataset()

    def download_dataset(self):
        dataset = load_dataset("zaibutcooler/archi-vault")
        self.images = dataset["train"]["images"]
        self.labels = dataset["train"]["labels"]
        log("Successfully loaded the dataset")

    def __getitem__(self, index):
        image = self.transforms(self.images[index])
        label = self.labels[index]
        return image, label

    def __len__(self):
        return len(self.images)
