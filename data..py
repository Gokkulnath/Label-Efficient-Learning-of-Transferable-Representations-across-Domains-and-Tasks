import torch
#print(torch.__version__) # torch Version
import numpy as np
from torchvision.datasets import MNIST,SVHN
from torch.utils.data import Dataset, DataLoader
from torch.tensor import Tensor as T

# To Do:
# Filter the Dataset Based on Range of Labels Given
class CustomMNIST(MNIST):
    """
    Additional Args:
        min_label : Minimun Value of Label That is to be allowed. 
        # Todo : Need to support list of values instead of min value
    """
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False,min_label=5):
        super().__init__(root, train=train, transform=transform, target_transform=target_transform, download=download)
        self.min_label=min_label
        self.train_data=self.train_data[self.train_labels>=self.min_label]
        self.train_labels=self.train_labels[self.train_labels>=self.min_label]


# Checked And working as expected
# mnist=FilteredMnist('.',download=True,label_min=5)
# print((mnist.train_labels))

class CustomSVNH(SVHN):
    def __init__(self, root, split='train', transform=None, target_transform=None, download=False,max_label=5):
        super().__init__(root, split=split, transform=transform, target_transform=target_transform, download=download)
        self.max_label=max_label
        self.data=self.data[self.labels<=self.max_label]
        self.labels=self.labels[self.labels<=self.max_label]


svnh=CustomSVNH(root='.',download=True,max_label=4)
mnist=CustomMNIST(root='.',download=True,min_label=5)


print(svnh.data.shape,svnh.labels.shape)
#print(np.unique(svnh.labels))
#print(np.unique(mnist.train_labels))
print(mnist.train_data.shape,mnist.train_labels.shape)