import inspect
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10, MNIST
from torch.nn import Conv1d


def print_dataset_arguments(dataset_class):
    print(f"{dataset_class.__name__} dataset arguments:")
    for name, parameter in inspect.signature(dataset_class.__init__).parameters.items():
        if name != 'self':
            print(f"{name}: {parameter.annotation}")

# Example: CIFAR10
print_dataset_arguments(CIFAR10)
print("===================================")

# Example: MNIST
print_dataset_arguments(MNIST)
print("===================================")

# Example: Convulation

print_dataset_arguments(Conv1d)
print("===================================")