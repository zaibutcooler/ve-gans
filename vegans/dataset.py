from torch.utils.data import Dataset
from torchvision import transforms as tran
from datasets import load_dataset



class TrainingSet(Dataset):
    def __init__(self,dataset_name='',image_size=(128,128)):
        super().__init__()        
        self.transforms = tran.Compose([

        ])
    def __getitem__(self, index):
        return self
    
    def __len__(self):
        return self
    
