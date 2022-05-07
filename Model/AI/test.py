import os
import cv2
import csv
import timm
import torch
import numpy as np
import albumentations as A
from torch.utils.data import Dataset, DataLoader

# # 절대경로 수정필요
# absolute_path = 'C:/Users/Sinion/Desktop/resnet/csv/'
#
# f = open(absolute_path + 'test.csv', 'r')
# rdr = csv.reader(f)


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


class TestDataset(Dataset):
    def __init__(self, file_lists, transforms=None):
        self.file_lists = file_lists.copy()
        self.transforms = transforms

    def __getitem__(self, idx):
        img = imread(self.file_lists[idx])
        rs_img = cv2.resize(img, (256, 256))
        img = cv2.cvtColor(rs_img, cv2.COLOR_BGR2RGB)

        if self.transforms:
            img = self.transforms(image=img)["image"]

        img = img.transpose(2, 0, 1)

        img = torch.tensor(img, dtype=torch.float)
        return img

    def __len__(self):
        return len(self.file_lists)


def run(image):
    testPath = './Model/AI/'
    filePath = image

    model_name = "swsl_resnext50_32x4d"
    batch_size = 96

    device = torch.device("cpu")  # cpu
    # device = torch.device("cuda")  # gpu

    class_list = []
    f = open(testPath + 'csv/address.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    c = 0
    for line in rdr:
        if c == 0:
            c += 1
        else:
            class_list.append(line[0])

    class_encoder = {}

    for i in class_list:
        class_encoder.update({class_list[class_list.index(i)]: class_list.index(i)})

    class_decoder = {v: k for k, v in class_encoder.items()}


    test_transforms_ = A.Compose([
        A.Normalize()
    ])

    test_files = [testPath + 'test/' + filePath]

    test_dataset = TestDataset(file_lists=test_files, transforms=test_transforms_)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    answer_logits = []

    model = timm.create_model(model_name, pretrained=True, num_classes=len(class_list)).to(device)
    model.load_state_dict(torch.load(testPath + 'model.pth', map_location="cpu"))
    model.eval()

    result = []
    with torch.no_grad():
        for iter_idx, test_imgs in enumerate(test_loader, 1):
            test_imgs = test_imgs.to(device)
            test_pred = model(test_imgs)

            result.append(class_decoder[np.argmax(test_pred.cpu(), axis=-1).item()])
    return result
