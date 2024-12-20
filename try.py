import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
import random
import torch.utils.data as Data
import os


m=nn.Softmax(dim=0)
x=torch.tensor([1,2,3,4],dtype=torch.float64)
print(m(x))
print(m(x+1))
print(m(2*x))











