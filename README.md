<div align="center">
<h1>YOLO-EMAC</h1>
<h3>YOLO-EMAC: A High-performance and Enhanced Generalization Small Target Defect Detection Method for PCB Boards Based on YOLO-EMAC</h3>
  
[Han Wu](https://github.com/wuhan66/YOLO-EMAC/)<sup>1,2</sup>, [Yunhan Lin]()<sup>1,2</sup>  
<sup>1</sup> School of Computer Science and Technology, Wuhan University of Science and Technology, Wuhan, China  
<sup>2</sup> Hubei Provincial Key Laboratory of Intelligent Information Processing and Real Time Industrial System, Wuhan, China


</div>

## 🛠️ Installation
```
wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
conda create -n yolov-emac python=3.11
conda activate yolov-emac
pip install -r requirements.txt
pip install -e .
```
## 📂 Datasets

The following three datasets can be used to train and evaluate PCB defect detection models:

- **DeepPCB Dataset**  
    ```
    https://pan.quark.cn/s/2d76aea04631
    ```
  - Description: The DeepPCB dataset is a publicly available PCB defect detection dataset containing various defect types (e.g., “missing copper,” “solder skip,” etc.). All images have a uniform resolution and complete annotations, making it suitable for small-object defect detection tasks.

- **PCBDefect Dataset**  
    ```
    https://pan.quark.cn/s/367b4007a88a
    ```
  - Description: The PCBDefect Dataset provides both synthetic and real-world PCB defect samples covering a wide range of surface defects and blemishes. It is useful for enriching model generalization during training.

- **PCBSurface Defect Dataset**  
  - Link:  
    ```
    https://pan.quark.cn/s/59472a1fb32e
    ```
  - Description: Released by the Robotics and Intelligent Manufacturing Research Group at Shenzhen University, this dataset contains real PCB surface defect images and corresponding annotation files. It’s ideal for evaluating detection performance in real-world scenarios.

---


## Training 
```
python
from ultralytics import YOLO
# Train the model
results = model.train(
  data='data.yaml',
  epochs=500, 
  batch=256, 
  imgsz=640,
  scale=0.5,  # S:0.9; M:0.9; L:0.9; X:0.9
  mosaic=1.0,
  mixup=0.0,  # S:0.05; M:0.15; L:0.15; X:0.2
  copy_paste=0.1,  # S:0.15; M:0.4; L:0.5; X:0.6
  device="0,1,2,3",
)
```
# 🚀 YOLO-EMAC with FlashAttention

This repository provides an efficient training pipeline for YOLO-EMAC using [Ultralytics](https://github.com/ultralytics/ultralytics) and [FlashAttention](https://github.com/Dao-AILab/flash-attention), enabling high-speed object detection on multi-GPU setups.

---

## 📦 Requirements

- Python 3.11
- PyTorch ≥ 2.2
- CUDA 11.x
- FlashAttention v2.7.3
- NVIDIA GPU with compute capability ≥ 7.5

---

## 📦 Configuration
- torch==2.2.2 
- torchvision==0.17.2
- flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
- timm==1.0.14
- albumentations==2.0.4
- onnx==1.14.0
- onnxruntime==1.15.1
- pycocotools==2.0.7
- PyYAML==6.0.1
- scipy==1.13.0
- onnxslim==0.1.31
- onnxruntime-gpu==1.18.0
- gradio==4.44.1
- opencv-python==4.9.0.80
- psutil==5.9.8
- py-cpuinfo==9.0.0
- huggingface-hub==0.23.2
- safetensors==0.4.3
- numpy==1.26.4

## 🚀 hyperparameters
- batch_size: 32
- img_size: [640, 640]
- optimizer:
  - type: "SGD"
  - momentum: 0.937
  - weight_decay: 0.0005
- initial_lr: 0.01
- warmup_epochs: 5
- lr_scheduler:
  - type: "cosine"
  - T_max: "total_epochs"
  - eta_min: 0.0001
- lr_reduce_on_plateau:
  - factor: 0.5
  - patience: 10
  - min_delta: 0.001
- epochs:
  - pcb_defect: 300
  - deeppcb: 300
  - surface: 500
- early_stopping:
  - patience: 10
  - min_delta: 0.001
- augmentation:
  - mosaic_prob: 0.5
  - flip_prob_h: 0.5
  - flip_prob_v: 0.5
  - scale: [0.8, 1.2]
  - translate: 0.2
- normalization:
  - mean: [0.485, 0.456, 0.406]
  - std: [0.229, 0.224, 0.225]
- interpolation: "bilinear"
- mixed_precision: true
- grad_clip_max_norm: 10
- validation_iou_threshold: 0.7
- nms:
  - score_threshold: 0.25
  - iou_threshold: 0.45


## Validation
[`yolov-emac-deeppcb`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/deeppcb/best.pt)
[`yolov-emac-pcbdefect`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/pcbdefect/best.pt)
[`yolov-emac-pcbsurface`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/pcbsurface/best.pt)

```python
from ultralytics import YOLO

model = YOLO('best.pt')
model.val(data='data.yaml', save_json=True)
```

