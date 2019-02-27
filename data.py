import torch
#print(torch.__version__) # torch Version
import numpy as np
from torchvision.datasets import MNIST,SVHN
from torch.utils.data import Dataset, DataLoader
from torch.tensor import Tensor as T

# To Do:
# Filter the Dataset Based on Range of Labels Given
class FilteredMnist(MNIST):
    """`MNIST <http://yann.lecun.com/exdb/mnist/>`_ Dataset.

    Args:
        root (string): Root directory of dataset where ``processed/training.pt``
            and  ``processed/test.pt`` exist.
        train (bool, optional): If True, creates dataset from ``training.pt``,
            otherwise from ``test.pt``.
        download (bool, optional): If true, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.

        label_min : Minimun Value of Label That is to be allowed. 
        # Todo : Need to support list of values instead of min value
    """
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False,label_min=5):
        super().__init__(root, train=train, transform=transform, target_transform=target_transform, download=download)
        self.label_range=label_min
        self.train_data=self.train_data[self.train_labels>self.label_range]
        self.train_labels=self.train_labels[self.train_labels>self.label_range]


# Checked And working as expected
# mnist=FilteredMnist('.',download=True,label_min=5)
# print((mnist.train_labels))



