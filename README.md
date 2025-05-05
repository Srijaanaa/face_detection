Face Detection with OpenCV
This Python project uses OpenCV to detect faces in real-time from a webcam feed. The display window automatically scales to 80% of your screen size for an optimal experience, with green rectangles and "Face" labels drawn around detected faces using the Haar Cascade classifier.
Table of Contents

Features
Prerequisites
Installation
Usage
Project Structure
Troubleshooting
Contributing
License
Acknowledgments

Features

Real-time face detection using a webcam.
Dynamic window sizing to ~80% of screen resolution (falls back to 1280x720 if unavailable).
Resizable window for manual adjustments.
Robust error handling for OpenCV, webcam, and classifier issues.
Optional screeninfo library for screen size detection.

Prerequisites

Python: Version 3.6–3.10.
Webcam: Built-in or external.
Operating System: macOS, Windows, or Linux.
Git: Optional, for cloning the repository.

Installation
Clone the Repository
Clone or download the project:
git clone https://github.com/Srijaanaa/face_detection.git
cd your-repo-name

Replace your-username and your-repo-name with your GitHub username and repository name.
Set Up a Virtual Environment
Create and activate a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
Install required packages:
pip install -r requirements.txt

This installs:

opencv-python==4.10.0.84: For face detection and webcam access.
screeninfo>=0.8.1: Optional, for screen resolution detection.

macOS-Specific Setup

Install Xcode command-line tools:xcode-select --install


Grant camera access:
Go to System Settings > Privacy & Security > Camera.
Enable access for your terminal or Python.



Verify Installation
Check OpenCV installation:
python3 -c "import cv2; print(cv2.__version__)"

Expected output: 4.10.0 or similar.
Usage
Running the Script
Run the face detection script:
python3 face_detection.py

What to Expect

A "Face Detection" window opens, sized to ~80% of your screen (e.g., 1536x1152 on a 1920x1200 display).
Green rectangles with "Face" labels appear around detected faces in the webcam feed.
The terminal shows the OpenCV version and frame size.
Press q to exit.
Resize the window by dragging its edges.

Project Structure
face_detection/
├── face_detection.py  # Main face detection script
├── requirements.txt   # Dependency list
└── README.md          # This documentation

Troubleshooting
"No module named cv2"

Install opencv-python:pip install opencv-python==4.10.0.84


Verify the correct Python environment:python3 --version



"No module named screeninfo"

Install screeninfo:pip install screeninfo


Without it, the script defaults to 1280x720.

"Could not open webcam"

Ensure the webcam is connected and not used by other apps.
Edit face_detection.py to try cv2.VideoCapture(1) instead of cv2.VideoCapture(0).
On macOS, verify camera permissions.

Incorrect Window Size

Install screeninfo for dynamic sizing.
Adjust the scale factor in face_detection.py (e.g., 0.8 to 0.6 in frame_width = int(screen_width * 0.8)).
Manually set frame_width and frame_height.

Slow Installation

Update pip:pip install --upgrade pip


On macOS, ensure Xcode tools:xcode-select --install



Contributing
How to Contribute

Fork the repository.
Create a feature branch:git checkout -b feature/your-feature


Commit changes:git commit -m "Add your feature"


Push to the branch:git push origin feature/your-feature


Open a pull request.

Guidelines

Follow the Code of Conduct (optional, add if desired).
Ensure code is documented and tested.

License
Licensed under the MIT License.
Acknowledgments

OpenCV for computer vision tools.
screeninfo for screen resolution detection.
Inspired by real-time face detection tutorials.

