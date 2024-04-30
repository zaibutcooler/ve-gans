import torch.nn as nn
import torch.nn.functional as F
import torch


from huggingface_hub import PyTorchModelHubMixin


class Generator(nn.Module, PyTorchModelHubMixin):
    def __init__(self):
        super(Generator, self).__init__()

        def block(in_feat, out_feat, norm=False):
            pass

        self.model = nn.Sequential()

    def forward(self, x, y):
        pass
