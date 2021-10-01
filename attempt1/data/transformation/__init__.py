from torch._C import _valgrind_supported_platform
from torchvision import transforms

train_transform = transforms.Compose([transforms.Resize((224, 224)),
                                    transforms.ToTensor()])

val_transform = transforms.Compose([transforms.Resize((224, 224)),
                                    transforms.ToTensor()])