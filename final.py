from ultralytics import YOLO
import cv2
import time
import pytz
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')

def convert_txt_to_list():
    file = open("stream.txt",'r')
    data = file.read()
    data_into_list = data.replace('\n', ' ').split()
    file.close()
    return data_into_list

model = YOLO("best.pt")


def main():
    url_list = convert_txt_to_list()

    stream_objs = []
    for url in url_list:
        
        stream_objs.append(cv2.VideoCapture(url))

    flag=0
    st = 0
    res = [] 
    while True and st<20:
        st += 1
        print("Iteration : ",st)
        if flag == len(url_list):
            flag = 0
        frame = stream_objs[flag].read()
        frame = frame[1]
        print(url_list[flag])
        if frame is None:
            flag= flag + 1
            print('flag increment')
            continue
        
        # cv2.imshow('frame',frame)
        j = 'recent.jpg'
        cv2.imwrite(j,frame)
        
        x = model.predict(j)
        res.append(x)
        
        try:
            with open('demo.txt', 'a') as f:
                rtsp = str(url_list[flag])
                from datetime import datetime
                # now = datetime.now()
                now = datetime.now(IST)
                day = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S.%f")
                day = str(day)
                time = str(time)
                pred = str(res[1][0][0][5].numpy())
                f.write(rtsp + " " + day + " " + time + " " + pred + "\n")
        except:
            print("No Detection")
            # pass
        
        flag += 1

    # csv file rtsp timestamp detection
    # rtsp wise work

if __name__ == '__main__':
    main()
    
    # yolo task=detect mode=predict model=yolov8n.pt source=stream.txtpython -u "u:\yolov8\ultralytics-main\Time_spent.py"