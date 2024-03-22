# initialize vegans
import torch
from generator import Generator
from discriminator import Discriminator
from discriminator import Discriminator
from utils import save_image,display_image
from dataset import TrainingSet

class Vegans:
    def __init__(self,lr=0.01,b1=0.02,b2=0.02):
        self.learning_rate = lr
        self.num_epoch = 0
        self.betas = (b1,b2)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.generator = Generator().to(self.device)
        self.discriminator = Discriminator().to(self.device)
        self.dataset = TrainingSet()
        self.g_optim = torch.optim.Adam(self.generator.parameters(),lr=self.learning_rate,betas=self.betas)
        self.d_optim = torch.optim.Adam(self.discriminator.parameters(),lr=self.learning_rate,betas=self.betas)

    def train(self):
        for epoch in range(self.num_epoch):
            for i,(image,label) in enumerate(self.dataset):
                self.g_optim.zero_grad()
                self.d_optim.zero_grad()



    def generate(self,label):
        pass

    def load_pretrained(self,checkpoint):
        pass
