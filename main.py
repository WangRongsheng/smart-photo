# coding:utf-8
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# 保持监听的文件
folder_to_track = "./src"
# 图片文件
#folder_destination_picture = "./source/picture"
animals = "./source/picture/animals"
food = "./source/picture/food"
people = "./source/picture/people"
scenery = "./source/picture/scenery"
text = "./source/picture/text"
# 音乐文件
folder_destination_music = "./source/music"
# 视频文件
folder_destination_video = "./source/video"


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(folder_to_track) :
            src = folder_to_track +"/"+ filename
            if filename.endswith("jpg") or filename.endswith("png"):
                #new_destination=folder_destination_picture + "/"+filename
                print(filename)
                os.system(r"python PaddleClas/tools/infer.py -c ./PaddleClas/ppcls/configs/quick_start/ResNet50_vd.yaml -o Infer.infer_imgs=./src/"+str(filename)+" -o Global.pretrained_model=./PaddleClas/output/ResNet50_vd/latest/latest > ./result.txt")
                with open('result.txt', 'r', encoding='utf-8') as f:  # 打开文件
                    lines = f.readlines()  # 读取所有行
                    last_line = lines[-1]  # 取最后一行
                    #print(eval(last_line))
                    result = eval(last_line)[0]['label_names'][0]
                    #print(type(eval(last_line)))
                if result=='animals':
                    new_destination=animals + "/" +filename
                if result=='people':
                    new_destination=people + "/" +filename
                if result=='food':
                    new_destination=food + "/" +filename
                if result=='scenery':
                    new_destination=scenery + "/" +filename
                if result=='text':
                    new_destination=text + "/" +filename
            elif filename.endswith("mp3") :
                new_destination=folder_destination_music + "/" + filename
            elif filename.endswith("avi") or filename.endswith("mp4"):
                #filename.__contains__("肖秀荣") :
                new_destination = folder_destination_video + "/"+filename
            os.rename(src, new_destination)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
        print('正在监听...')
except KeyboardInterrupt:
    observer.stop()

observer.join()