import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    #model = YOLO(model=r'E:\yolov12-main\yolov12-main\ultralytics\cfg\models\v12\yolov12.yaml')
    #model = YOLO(model=r'E:\yolov12-main\yolov12-main\ultralytics\cfg\models\11\yolo11m.yaml')
    model = YOLO(model=r'E:\yolov12-main\yolov12-main\ultralytics\cfg\models\v5\yolov5s.yaml')
    #model = YOLO(model=r'E:\yolov12-main\yolov12-main\my.yaml')
    #model = YOLO(model=r'E:\yolov12-main\yolov12-main\ultralytics\cfg\models\11\yolo11-cls.yaml')
    #model.load('E:\yolov12-main\yolov12-main\yolov12n.pt') # 加载预训练权重,改进或者做对比实验时候不建议打开，因为用预训练模型整体精度没有很明显的提升
    #model.load('E:\yolov12-main\yolov12-main\\runs\\train\exp6\weights\\best.pt')
    model.train(data=r'E:\yolov12-main\yolov12-main\data.yaml',
                imgsz=640,
                epochs=300,
                batch=16,
                workers=4,
                device='0',
                optimizer='SGD',
                close_mosaic=10,
                resume=False,
                project='runs/train',
                name='exp',
                single_cls=False,
                cache=True ,
                )
