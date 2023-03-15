#!/usr/bin/env python
# coding: utf-8

# In[18]:


from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
from matplotlib import pyplot as plt
import albumentations
from albumentations.pytorch import ToTensorV2
import torch
import torchvision
import cv2


# ## PATH 설정

# In[5]:


path = 'C:/Users/mnju5/2023-youtuber-crawling/youtuber-look-alike-crawler/glory/mo'


# In[6]:


file_list = os.listdir(path)


# In[7]:


file_list[0]


# In[8]:


file_list


# In[9]:


file_name_list = []
for i in range(len(file_list)):
    file_name_list.append(file_list[i])


# In[10]:


file_name_list


# In[11]:


image = cv2.imread('C:/Users/mnju5/2023-youtuber-crawling/youtuber-look-alike-crawler/glory/mo/000009.jpg')
print(image)


# In[32]:


class AlbumentationsDataset(Dataset):
    def __init__(self, file_path, labels, transform=None): #과제에는 labels 빼도 됨
        self.file_path = file_path
        self.labels = labels
        self.transform = transform

# 파일 여러개 처리할 수 있도록 수정 필요
    def __getitem__(self, index):
        label = self.labels[index]
        file_path = self.file_path[index]

        # Image open
        # image = Image.open(file_path)
        image = cv2.imread(file_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        start_t = time.time()
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']

        total_time = (time.time() - start_t)

        return image, label, total_time

    def __len__(self):
        return len(self.file_path)


# In[36]:


albumentations_transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    #A.ShiftScaleRotate(shift_limit=0.4, scale_limit=(0.5, 0.9), rotate_limit=90, p=1, border_mode=cv2.BORDER_REPLICATE),
    A.RandomBrightnessContrast(brightness_limit=(-0.3, 0.3), contrast_limit=(-0.3, 0.3), p=1),
    A.ChannelShuffle(p=0.2),
    ToTensorV2()
])


# In[37]:


import time


# In[38]:


augment_cnt = 1

# 데이터 가져오기
for i in os.listdir('C:/Users/mnju5/2023-youtuber-crawling/youtuber-look-alike-crawler/glory/mo/') :

    os.makedirs("./custom_data", exist_ok=True)

    path = 'C:/Users/mnju5/2023-youtuber-crawling/youtuber-look-alike-crawler/glory/mo/' + i
    albumentations_dataset = AlbumentationsDataset(
            file_path=[path], #데이터 경로
            labels=[1],
            transform=albumentations_transform
    )

    # 배포 시간 측정
    total_time = 0
    for i in range(100):
        sample, _, transform_time = albumentations_dataset[0]
        total_time += transform_time

    print("torchvision time / sample : {} ms ".format(total_time*10))

    # 시각화 코드
    plt.figure(figsize=(10, 10))
    plt.imshow(transforms.ToPILImage()(sample)) #sample(1개) 말고 데이터 셋(여러개)으로 줘야 함
    #plt.show()
    transforms.ToPILImage()(sample).save("./custom_data/" + "custom_" + str(augment_cnt) + ".png")

    augment_cnt += 1

