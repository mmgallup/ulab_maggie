import torch
import numpy as np

def _hidden_function(x):
    """Applies a transformation to obscure the underlying pattern with noise."""
    return (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1) + torch.randn(x.shape[0], 1) * 0.2

# Defining the dataset dimensions
N, D_in, D_out = 1000, 2, 1

# Creating the input data
x = torch.randn(N, D_in) * 3.1415
y = _hidden_function(x)

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()

