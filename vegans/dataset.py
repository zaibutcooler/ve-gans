from torch.utils.data import Dataset
from torchvision import transforms as tran
from datasets import load_dataset



class TrainingSet(Dataset):
    def __init__(self,image_size=(128,128),gray_scale=True):
        super().__init__()        
        self.transforms = tran.Compose([
            tran.Resize(image_size),
            tran.ToTensor(),
            tran.Normalize([0.5],[0.5]),
            tran.Grayscale() if gray_scale==True else None,
        ])

        self.images = None
        self.labels = None
 
    def __getitem__(self, index):
        image = self.transforms(self.images[index])
        label = self.labels[index]
        return image,label
    
    def __len__(self):
        return len(self.images)
