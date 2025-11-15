# 📌 PlateVision — Smart Parking Management System
**A computer-vision–powered system that detects vehicle license plates, reads them using OCR, and assigns an available parking slot automatically.**

---

## 🚗 Project Overview
**PlateVision** is an intelligent parking automation system designed to:
- Detect vehicle license plates using a YOLOv8 model  
- Perform OCR-based text extraction via PyTesseract  
- Save plate data to an Excel log  
- Assign the driver an appropriate parking slot automatically  

Built on **AugeLab's custom block architecture**, it includes specialized Python modules for detection, OCR, and data logging.

---

# 📁 Setup

## 1️⃣ Install Required Custom Blocks
The project contains three custom AugeLab blocks:

- `ExcelLogger_PlateWriter.py`
- `PlateReader_PyTesseract.py`
- `YOLO_PlateDetector.py`

### 📌 Place these files in:

**Windows:**
```
C:\Users\<USERNAME>\AppData\Roaming\AugeLab Studio\marketplace\custom_blocks\
```

AugeLab will automatically detect these blocks upon startup.

---

## 2️⃣ Add YOLO Model Weights

The YOLOv8 model weights are included in this repository.

**File:** `license_plate_detector.pt`

**To download and inspect:**
```
https://github.com/Muhammad-Zeerak-Khan/Automatic-License-Plate-Recognition-using-YOLOv8
```

### 📌 Place the model file in:
```
C:\models\license_plate_detector.pt
```

Make sure to update the path in `YOLO_PlateDetector.py` if you choose a different location.

---

## 3️⃣ Install Tesseract OCR

**Download from:**
```
https://github.com/UB-Mannheim/tesseract/wiki
```

**Default installation path:**
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

**Important:** After installation, add Tesseract to your system PATH:
1. Open System Properties → Environment Variables
2. Edit the `Path` variable
3. Add: `C:\Program Files\Tesseract-OCR`
4. Restart your terminal/command prompt

Ensure the custom block references this location or update the path accordingly.

---

## 4️⃣ Install Required Python Packages

PlateVision requires several Python libraries. Install them using **AugeLab Studio's built-in Python**.

### Step 1: Install pip (if not already installed)
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
"C:\Users\<USERNAME>\AppData\Local\Programs\AugeLab Studio\Python\python.exe" get-pip.py
```

### Step 2: Install Required Libraries

**Install Ultralytics (YOLOv8):**
```bash
"C:\Users\<USERNAME>\AppData\Local\Programs\AugeLab Studio\Python\python.exe" -m pip install ultralytics
```

**Install openpyxl (Excel logging):**
```bash
"C:\Users\<USERNAME>\AppData\Local\Programs\AugeLab Studio\Python\python.exe" -m pip install openpyxl
```

**Install OpenCV (may be required):**
```bash
"C:\Users\<USERNAME>\AppData\Local\Programs\AugeLab Studio\Python\python.exe" -m pip install --force-reinstall opencv-python
```

> **Alternative:** You can also use AugeLab Studio's **Package Manager** to install these libraries from the interface.

---

# ⚙️ System Workflow

## 1. YOLO_PlateDetector  
Detects the license plate region and outputs a cropped plate image.

## 2. PlateReader_PyTesseract  
Extracts textual information from the cropped image using OCR.

## 3. ExcelLogger_PlateWriter  
Logs the plate and timestamp into Excel and assigns a parking slot.

---

## 📸 Screenshots

![PlateVision Demo](https://github.com/user-attachments/assets/1ffc0587-386e-4750-a9b6-0dabf3ecb43e)

---

# 🚀 Future Improvements

## 🧠 Accuracy & Reliability Enhancements
- Stability Issues: System may occasionally miss plates or detect multiple ones—needs more robust filtering.
- Image Quality Sensitivity: OCR accuracy drops in low-light or angled shots.
- False Positives: Sometimes reads characters wrong due to reflections or plate fonts.
- Better Preprocessing: Use of CLAHE, bilateral filtering, or HSV transformations.
- Plate Validation: Apply regex rules to filter out invalid results.
  
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
