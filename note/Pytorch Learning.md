## Pytorch Learning: 

### Pytorch environment  and installation

### Py-torch data loading 

```python
# 1. Dataset  提供一种方式批量获取数据和标签.
# 2. Dataloader 为后续的网络运行提供数据加载形式.
数据的组织形式: 文件名作为标签名称, 图像名作为标签, 图像和标签分开整理.

"""
pytorch learning :
class dataset restructure:
init, getitem, len  three function should be rewrite
in __init__, root_dir, label_dir, data path, image_path list.
in __getitem__, idx, image_name, full image path, open image, and label_name
in __len__ , it is the length of dataset.

"""

from torch.utils.data import Dataset
import os
from PIL import Image

# parametes:
root_dir = "hymenoptera_data\\train"  # root_dir of dataset.
ants_label_dir = "ants"  # ants' label_dir.
bees_label_dir ="bees"  # bees' label_dir


class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.image_path = os.listdir(self.path)

    def __getitem__(self, idx):  # index of image
        image_name = self.image_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, image_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.image_path)


# 实例化数据
ants_data = MyData(root_dir, ants_label_dir)
bees_data = MyData(root_dir, bees_label_dir)
# merge small dataset to a train dataset.
TrainData = ants_data + bees_data
img, label = TrainData[45]
img.show() 
```

### Tensor board

```python
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image
"""
This class is a drawing tools to monitor our steps and values. for training logs.
and train images display.
"""
# demo
# pi = 3.14
# Writer = SummaryWriter("logs")
# for i in range(1000):
#    Writer.add_scalar("y_values2", 2*i+pi, i)
# Writer.close()


# Demo 2
writer = SummaryWriter("logs")
image_path = "hymenoptera_data/train/ants/6743948_2b8c096dda.jpg"
img_pil = Image.open(image_path)  # 图像数据格式在tensorboard 需要 numpy or tensor,
image_array = np.array(img_pil)  # transform types of data
writer.add_image("image", image_array, 0, dataformats='HWC')  # shape 
writer.close()

"""
(studyTorch) F:\Study-file-python>tensorboard --logdir=logs --port=6609
TensorFlow installation not found - running with reduced feature set.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.8.0 at http://localhost:6609/ (Press CTRL+C to quit)
"""

```

![image-20220823223455804](Pytorch Learning.assets/image-20220823223455804.png)

### Transform-torchvision

```python
"""
The transform under torchvision.
function:
    "Compose",
    "ToTensor",
    "PILToTensor",
    "ConvertImageDtype",
    "ToPILImage",
    "Normalize",
    "Resize",
    "CenterCrop",
    "Pad",
    "Lambda",
    "RandomApply",
    "RandomChoice",
    "RandomOrder",
    "RandomCrop",
    "RandomHorizontalFlip",
    "RandomVerticalFlip",
    "RandomResizedCrop",
    "FiveCrop",
    "TenCrop",
    "LinearTransformation",
    "ColorJitter",
    "RandomRotation",
    "RandomAffine",
    "Grayscale",
    "RandomGrayscale",
    "RandomPerspective",
    "RandomErasing",
    "GaussianBlur",
    "InterpolationMode",
    "RandomInvert",
    "RandomPosterize",
    "RandomSolarize",
    "RandomAdjustSharpness",
    "RandomAutocontrast",
    "RandomEqualize",
    totensor 为什么?  tensor 格式的数据打包包含装了我们学习网络的一些理论基础参数, 例如, 反向传播, 梯度, 设备, 等一系列的数据.
"""
# 单张图像的基础处理
from torchvision import transforms
import cv2 as cv
# loading an image
img_path = "hymenoptera_data/train/ants/6240338_93729615ec.jpg"
img = cv.imread(img_path)
print(img.shape)  # (181, 500, 3)
# transforms 类文件的一个实例化的过程.
transforms = transforms.ToTensor()  # 实例化对象
img_tensor = transforms(img)
print(img_tensor.shape)  # torch.Size([3, 181, 500])
print(type(img_tensor))  # <class 'torch.Tensor'>

```

### Transform , dataset,  DataLoader

```python
"""
Dataloader for self Dataset in pytorch.

"""
# dataset
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import os

from torchvision import transforms

root_dir = "hymenoptera_data/train"
label_dir = "ants"


class Mydata(Dataset):
    def __init__(self, root_dir, label_dir, transform=None):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.image_path = os.path.join(self.root_dir, self.label_dir)
        self.image_pac = os.listdir(self.image_path)
        self.transform = transforms.Compose([
            transforms.PILToTensor(),
            transforms.Resize((50, 50))

        ])

    def __getitem__(self, idx):
        image_name = self.image_pac[idx]
        image_item_path = os.path.join(self.image_path, image_name)
        image = Image.open(image_item_path)
        label = self.label_dir
        # transforms operator for each images
        if self.transform:
            image = self.transform(image)

        sample = {"image": image, "label": label}

        return sample

    def __len__(self):
        return len(self.image_pac)


# 实例化Dataset, DataLoader
dataset = Mydata(root_dir, label_dir)
dataloader = DataLoader(dataset=dataset, batch_size=6, shuffle=True, num_workers=0, drop_last=True)
sample = dataset[0]
print(sample)  # {'image': tensor([[[ 82,  82,  82,  ...,  78,  78,  80],...[236, 238, 238,  ...,   3,   3,   5]]], dtype=torch.uint8), 'label': 'ants'}
print(type(dataloader))  # <class 'torch.utils.data.dataloader.DataLoader'>
dataiter = iter(dataloader)
samples = dataiter.next()
print(type(samples))
print(samples)  # 一次输出batchsize 的数据



```

