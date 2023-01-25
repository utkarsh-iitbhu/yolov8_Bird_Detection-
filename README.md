<div align="center">
  <p>
    <a align="center" href="https://ultralytics.com/yolov8" target="_blank">
      <img width="850" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png"></a>
  </p>


<br>

[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), developed by [Ultralytics](https://ultralytics.com), is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection, image segmentation and image classification tasks.

## <div align="center">Documentation</div>




<summary>Install</summary>

Pip install the ultralytics package including all [requirements.txt](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
pip install ultralytics
```
  
  <br>

  After installing ultralytics one has to run [final.py](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/final.py) file. This python code will store all the data of your webcams taken from the CCTV footage. Add all the RTSP streams for detection in [stream.txt](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/stream.txt).
  
   <br>
  
  After running the code and storing data for sufficient amount of time then we have see that detection data is being stored in the [demo.txt](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/demo.txt) 
  
   <br>
  
  To get the desired results in [Bird_detection.xlsx](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/Bird_detection.xlsx) we have to run the [Time_spent.py](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/Time_spent.py). With this we will get the desired output in [Bird_detection.xlsx](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/Bird_detection.xlsx) with multiple sheets corresponding to different CCTV's and overall result. 
  
   <br>
  
  Once you have got the desired result, run the [clear_files.py](https://github.com/utkarsh-iitbhu/yolov8_Bird_Detection-/blob/main/clear_files.py) file to delete all the object data from the text and csv files. This code will not delete data from Bird_detection.xlsx as it may contain valuable data.
  
  
  
 
