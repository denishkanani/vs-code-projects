import torchvision
from torchvision import datasets, transforms

transform = transforms.ToTensor()

train_dataset = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.CIFAR10(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

print(len(train_dataset))

print(len(test_dataset))

image, label = train_dataset[0]

print(image.shape)
print(label)

classes = train_dataset.classes
print(classes)

print(classes[label])

transform = transforms.ToTensor()

train_dataset = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

print(len(train_dataset))

image, label = train_dataset[0]

print(image.shape)
print(label)

classes = train_dataset.classes
print(classes[label])

for i in range(3):
    image, label = train_dataset[i]
    print(i, image.shape, train_dataset.classes[label])
    
image, label = train_dataset[5]

transform = transforms.ToTensor()

train_dataset = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

print("Total Images:", len(train_dataset))

image, label = train_dataset[0]

print("Image Shape:", image.shape)
print("Label:", label)
print("Class:", train_dataset.classes[label])

