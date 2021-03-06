# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/103_FCN.ipynb (unless otherwise specified).

__all__ = ['FCN']

# Cell
from ..imports import *
from .layers import *

# Cell
class FCN(Module):
    def __init__(self, c_in, c_out, layers=[128, 256, 128], kss=[7, 5, 3]):
        self.conv1 = Conv1d(c_in, layers[0], kss[0], padding='same', act_fn='relu')
        self.conv2 = Conv1d(layers[0], layers[1], kss[1], padding='same', act_fn='relu')
        self.conv3 = Conv1d(layers[1], layers[2], kss[2], padding='same', act_fn='relu')
        self.gap = nn.AdaptiveAvgPool1d(1)
        self.squeeze = Squeeze(-1)
        self.fc = nn.Linear(layers[-1], c_out)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.squeeze(self.gap(x))
        return self.fc(x)