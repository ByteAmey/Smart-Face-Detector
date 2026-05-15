# Smart-Face-Detector
# 🎯 Smart Face Detector

A real-time face detection application built with Python and OpenCV that detects **faces**, **eyes**, and **smiles** using Haar Cascade classifiers.

---

## 📸 Demo

The application opens your webcam and draws bounding boxes around detected faces, with live labels for eye and smile detection.

---

## ✨ Features

- 🟢 **Face Detection** — Draws a green rectangle around every detected face
- 👁️ **Eye Detection** — Displays "Eyes Detected" label when eyes are found
- 😄 **Smile Detection** — Displays "Smiling" label when a smile is detected
- ⚡ **Real-time** — Processes each frame live from your webcam

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenCV (`cv2`) | Computer vision & image processing |
| Haar Cascades | Pre-trained XML classifiers for detection |

---

## 📁 Project Structure

```
OpenCV/Project/
│
├── smart_face_detector.py          # Main application script
├── haarcascade_frontalface_default.xml   # Face classifier
├── haarcascade_eye.xml             # Eye classifier
└── haarcascade_smile.xml           # Smile classifier
```

---

## ⚙️ Requirements

- Python 3.x
- OpenCV

Install OpenCV via pip:

```bash
pip install opencv-python
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-face-detector.git
cd smart-face-detector
```

### 2. Download Haar Cascade XML files

The XML classifiers are included with OpenCV. You can find them in your OpenCV installation:

```
<python_env>/Lib/site-packages/cv2/data/
```

Or download them directly from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

Place them in the `OpenCV/Project/` folder (or update the paths in the script).

### 3. Run the application

```bash
python smart_face_detector.py
```

### 4. Quit

Press **`Q`** to exit the application.

---

## 🔧 How It Works

1. **Capture** — Video frames are captured from the default webcam using `cv2.VideoCapture(0)`
2. **Grayscale** — Each frame is converted to grayscale for faster processing
3. **Detect Faces** — `detectMultiScale()` scans the frame for faces using the Haar cascade
4. **ROI (Region of Interest)** — For each detected face, a cropped region is extracted for eye and smile detection
5. **Annotate** — Rectangles and text labels are drawn on the original color frame
6. **Display** — The annotated frame is shown in a live window

---

## 🎛️ Tunable Parameters

You can adjust these values in the script to improve detection accuracy:

| Parameter | Current Value | Effect |
|-----------|--------------|--------|
| `scaleFactor` (face) | `1.1` | Lower = more sensitive, slower |
| `minNeighbors` (face) | `5` | Higher = fewer false positives |
| `scaleFactor` (smile) | `1.7` | Higher = less sensitive |
| `minNeighbors` (smile) | `20` | Higher = stricter smile detection |

---

## 📌 Notes

- Make sure your webcam is connected and accessible
- Good lighting improves detection accuracy
- Smile detection works best when a face is already detected

---

## 🙌 Acknowledgements

- [OpenCV](https://opencv.org/) — Open Source Computer Vision Library
- Haar Cascade classifiers by **Viola & Jones**
