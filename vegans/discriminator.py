import torch.nn as nn
import torch.nn.functional as F
import torch

class Discriminator(nn.Module):
  def __init__(self):
    super(Discriminator, self).__init__()
    self.model = nn.Sequential(

    )

  def forward(self,x,y):
    return x