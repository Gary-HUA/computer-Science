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

```

