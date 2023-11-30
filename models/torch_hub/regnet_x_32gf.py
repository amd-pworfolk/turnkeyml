# labels: test_group::turnkey name::regnet_x_32gf author::torch_hub task::Computer_Vision license::bsd-3-clause
from turnkeyml.parser import parse
import torch
from torchvision.models import RegNet_X_32GF_Weights

torch.manual_seed(0)

# Parsing command-line arguments
pretrained, batch_size, num_channels, width, height = parse(
    ["pretrained", "batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = torch.hub.load(
    "pytorch/vision:v0.13.1",
    "regnet_x_32gf",
    weights=RegNet_X_32GF_Weights.DEFAULT if pretrained else None,
)
model.eval()
inputs = {"x": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
