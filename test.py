# coding:utf-8
import os
import time

os.system(r"python ./PaddleClas/tools/infer.py -c ./PaddleClas/ppcls/configs/quick_start/ResNet50_vd.yaml -o Infer.infer_imgs=./PaddleClas/demo/a.jpg -o Global.pretrained_model=./PaddleClas/output/ResNet50_vd/latest/latest > result.txt")

with open('result.txt', 'r', encoding='utf-8') as f:  # 打开文件
    lines = f.readlines()  # 读取所有行
    last_line = lines[-1]  # 取最后一行
    #print(eval(last_line))
    print(eval(last_line)[0]['label_names'][0])
    #print(type(eval(last_line)))
