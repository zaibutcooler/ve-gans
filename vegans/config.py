from pydantic import BaseModel


class Config(BaseModel):
    learning_rate: float = 0.0002  # learning rate for generator and discriminator
    num_epoch: int = 100  # number of epochs to train
    betas: tuple[float, float] = (0.5, 0.999)  # beta1 and beta2 for Adam optimizer
    batch_size: int = 32  # batch size for training
    image_size: int = 64  # size of input images
    channels: int = 3  # number of color channels in input images
    n_critic: int = 5  # number of critic iterations per generator iteration
    save_interval: int = 100  # interval for saving model checkpoints
    sample_interval: int = 100  # interval for generating sample images
