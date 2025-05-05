Face Detection with OpenCV
=========================

This Python project uses OpenCV to detect faces in real-time from a webcam feed. The display window automatically scales to 80% of your screen size for an optimal experience, with green rectangles and "Face" labels drawn around detected faces using the Haar Cascade classifier.

Table of Contents
-----------------
- Features
- Prerequisites
- Installation
- Usage
- Project Structure
- Troubleshooting
- Contributing
- License
- Acknowledgments

Features
--------
- Real-time face detection using a webcam.
- Dynamic window sizing to ~80% of screen resolution (falls back to 1280x720 if unavailable).
- Resizable window for manual adjustments.
- Robust error handling for OpenCV, webcam, and classifier issues.
- Optional `screeninfo` library for screen size detection.

Prerequisites
-------------
- **Python**: Version 3.6–3.10.
- **Webcam**: Built-in or external.
- **Operating System**: macOS, Windows, or Linux.
- **Git**: Optional, for cloning the repository.

Installation
------------
### Clone the Repository
Clone or download the project:
```bash
git clone https://github.com/Srijaanaa/face_detection.git
cd face_detection  
