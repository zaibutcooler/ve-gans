import torch.nn as nn
import torch.nn.functional as F
from .config import Config
from huggingface_hub import PyTorchModelHubMixin


class Discriminator(nn.Module, PyTorchModelHubMixin):
    def __init__(self, config: Config):
        super(Discriminator, self).__init__()
        self.config = config
        self.model = nn.Sequential(nn.Linear())

    def forward(self, x, y):
        return x
