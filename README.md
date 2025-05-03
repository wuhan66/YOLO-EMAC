<div align="center">
<h1>YOLO-EMAC</h1>
<h3>YOLO-EMAC: A High-performance and Enhanced Generalization Small Target Defect Detection Method for PCB Boards Based on YOLO-EMAC</h3>
  
[Han Wu](https://github.com/wuhan66/YOLO-EMAC/)<sup>1</sup>

<sup>1</sup> School of Computer Science and Technology, Wuhan University of Science and Technology, Hubei Provincial Key Laboratory of Intelligent Information Processing and Real Time Industrial System, Wuhan, China

</div>

## 🛠️ Installation
```
wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
conda create -n yolov-emac python=3.11
conda activate yolov-emac
pip install -r requirements.txt
pip install -e .
```

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

This repository provides an efficient training pipeline for YOLOv12 using [Ultralytics](https://github.com/ultralytics/ultralytics) and [FlashAttention](https://github.com/Dao-AILab/flash-attention), enabling high-speed object detection on multi-GPU setups.

---

## 📦 Requirements

- Python 3.11
- PyTorch ≥ 2.2
- CUDA 11.x
- FlashAttention v2.7.3
- NVIDIA GPU with compute capability ≥ 7.5

---

## Validation
[`yolov-emac-deeppcb`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/deeppcb/best.pt)
[`yolov-emac-pcbdefect`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/pcbdefect/best.pt)
[`yolov-emac-pcbsurface`](https://github.com/wuhan66/YOLO-EMAC/edit/main/training_logs_and_weights/pcbsurface/best.pt)

```python
from ultralytics import YOLO

model = YOLO('best.pt')
model.val(data='data.yaml', save_json=True)
```

