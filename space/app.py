import streamlit as st
import torch
from torchvision.utils import make_grid
from torchvision.transforms import ToPILImage
from vegans.generator import Generator

generator = Generator().to('device')

pretrained = torch.load('')

generator.load_state_dict(pretrained)

def main():
    st.title("Image Generation")
    st.write("Made with GANS from scratch")
    
    
if __name__ == '__main__':
    main()
