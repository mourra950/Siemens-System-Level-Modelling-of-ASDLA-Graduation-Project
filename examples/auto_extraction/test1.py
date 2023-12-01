import inspect
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10, MNIST
from torch.nn import Conv1d


def print_dataset_arguments(dataset_class):
    print(f"{dataset_class.__name__} dataset arguments:")
    for name, parameter in inspect.getmembers(object=dataset_class):
        if name != 'self':
            print(f"{name}: {parameter}" )

# Example: CIFAR10
# print_dataset_arguments(CIFAR10)
print("===================================")
for i in MNIST.__dict__:
    print(i)
    print(MNIST.__dict__[i])
print("===================================")

for name, parameter in inspect.signature(MNIST.__init__).parameters.items():
    print(name)

# Example: MNIST
# print_dataset_arguments(MNIST)
print("===================================")

print(MNIST.__dict__['__parameters__'])
# Example: Convulation

# print_dataset_arguments(Conv1d)
print("===================================")