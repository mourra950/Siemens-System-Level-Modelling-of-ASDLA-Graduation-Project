import torch
from torch import FloatTensor,Tensor
import matplotlib.pyplot as plt
import cv2
import numpy as np
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.jit.load(r'E:\Github\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\data\result\model5.pt')
model.to(device)
print(device)
img_path = r'E:\Github\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\data\image_samples\img_1.jpg'
img = plt.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# img = cv2.resize(img,(224,224))
torch.nn.Conv2d(padding_mode=)

img_tensor = Tensor.cuda(FloatTensor(img.reshape((1, 3, 28, 28))))
print(img_tensor.shape)

img_tensor.to(device)

# print(img_tensor)

output = model.forward(img_tensor)

output=Tensor.cpu(output)
print(output)
res = np.argmax(output.detach().numpy(), 1)
print(res)