# 📌 PlateVision — Smart Parking Management System
**A computer-vision–powered system that detects vehicle license plates, reads them using OCR, and assigns an available parking slot automatically.**

## 🚗 Project Overview
**PlateVision** is an intelligent parking automation system designed to:
- Detect vehicle license plates using a YOLOv8 model  
- Perform OCR-based text extraction via PyTesseract  
- Save plate data to an Excel log  
- Assign the driver an appropriate parking slot automatically  

Built on **AugeLab's custom block architecture**, it includes specialized Python modules for detection, OCR, and data logging.

---

# 📁 Installation & Directory Structure

## 1️⃣ Install Required Custom Blocks
The project contains three custom AugeLab blocks:

- ExcelLogger_PlateWriter.py
- PlateReader_PyTesseract.py
- YOLO_PlateDetector.py

### 📌 Place these files here:

### **Windows**
```
C:\Users\<USERNAME>\AppData\Local\AugeLab\custom_blocks\
```

### **Linux**
```
~/.local/share/AugeLab/custom_blocks/
```

AugeLab will automatically detect these blocks upon startup.

---

## 2️⃣ Add YOLO Model Weights
Download the YOLOv8 model from:

https://github.com/Muhammad-Zeerak-Khan/Automatic-License-Plate-Recognition-using-YOLOv8

Place the downloaded file:

```
license_plate_detector.pt
```

Into:

```
C:\models\PlateVision\license_plate_detector.pt
```

Make sure to update the path in `YOLO_PlateDetector.py` if needed.

---

## 3️⃣ Install Tesseract OCR
Windows installer:

https://github.com/UB-Mannheim/tesseract/wiki

Default install path:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Ensure the custom block references this location or update the path accordingly.

---

## 4️⃣ Install Required Python Packages
PlateVision requires two additional Python libraries to run YOLOv8 detection and Excel logging:

📦 Install Ultralytics (YOLOv8)

Used for loading the YOLOv8 license plate detection model.
```bash
pip install ultralytics
```

📦 Install openpyxl

Used for creating and updating the Excel log file.
```bash
pip install openpyxl
```

Make sure these packages are installed in the same Python environment that AugeLab uses.

---

# ⚙️ System Workflow

## 1. YOLO_PlateDetector  
Detects the license plate region and outputs a cropped plate image.

## 2. PlateReader_PyTesseract  
Extracts textual information from the cropped image using OCR.

## 3. ExcelLogger_PlateWriter  
Logs the plate and timestamp into Excel and assigns a parking slot.

---

# 📁 Recommended Project Structure

```
PlateVision/
│
├── custom_blocks/
│     ├── ExcelLogger_PlateWriter.py
│     ├── PlateReader_PyTesseract.py
│     └── YOLO_PlateDetector.py
│
├── models/
│     └── license_plate_detector.pt
│
├── plakalar.xlsx   (auto-generated)
└── README.md
```

---

# 🚀 Future Improvements

## 🔧 Improve Plate Accuracy
- Advanced preprocessing (CLAHE, denoise)
- Plate segmentation models
- Regex validation for valid formats

## ⚡ Dynamic Architecture
- Live video support
- Multi-vehicle tracking (Re-ID)
- Parking occupancy detection

## 💾 Database Integration
Replace Excel with:
- SQLite
- PostgreSQL
- Firebase/Supabase

## 📡 API Extensions
- Automated barrier control  
- Payment systems  
- Mobile notifications  

## 🖥️ UI Enhancements
- Desktop GUI  
- Web dashboard  
- Live monitoring  

---

# 📜 License
This project is open-source under the **MIT License**.
