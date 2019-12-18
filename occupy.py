import os
import torch
from tqdm import tqdm
import time

# declare which gpu device to use
cuda_device = '0'

def check_mem(cuda_device):
    devices_info = os.popen('"/usr/bin/nvidia-smi" --query-gpu=memory.total,memory.used --format=csv,nounits,noheader').read().strip().split("\n")
    print(devices_info)
    total, used = 1024/0.9,0#devices_info[int(cuda_device)].split(',')
    return total,used

def occumpy_mem(cuda_device):
    total, used = check_mem(cuda_device)
    total = int(total)
    used = int(used)
    max_mem = int(total * 0.9)
    block_mem = max_mem - used
    print("we could occupy memory:",block_mem)
    x = torch.cuda.FloatTensor(256,1024,block_mem)#设置256m占用
    del x
    
if __name__ == '__main__':
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_device
    occumpy_mem(cuda_device)
    for _ in tqdm(range(60)):#设置进度条
        time.sleep(1)

    print('Done')
