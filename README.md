# Gesture Reader PC

Gesture Reader PC is a real-time gesture-controlled reading system for
Windows.\
It allows users to scroll and zoom PDF documents in the Brave browser
using hand gestures detected through a webcam.

The system is built using:

-   MediaPipe (hand tracking)
-   OpenCV
-   PyAutoGUI
-   Python 3.10

------------------------------------------------------------------------

## Features

-   Thumb extended (out) enables scroll mode
-   Thumb tucked (in) disables scrolling
-   Two-hand pinch gesture activates zoom mode
-   Scroll direction mimics mobile-style interaction
-   Controls are restricted to Brave browser
-   Real-time HUD with hand landmark visualization

------------------------------------------------------------------------

## System Requirements

-   Windows 10 or Windows 11
-   Webcam
-   Python 3.10
-   Brave browser

Important: Python 3.10 is required. MediaPipe is most stable on this
version.

Download Python 3.10 from:
https://www.python.org/downloads/release/python-31011/

During installation: - Enable "Add Python to PATH" - Install for all
users (recommended)

------------------------------------------------------------------------

## Installation

### 1. Clone the Repository

git clone https://github.com/vaibhavvasant/gesture-reader-pc.git\
cd gesture-reader-pc

### 2. Create a Virtual Environment

py -3.10 -m venv venv\
venv`\Scripts`{=tex}`\activate`{=tex}

After activation, `(venv)` should appear in the terminal.

### 3. Install Dependencies

pip install -r requirements.txt

This installs:

-   mediapipe
-   opencv-python
-   pyautogui
-   numpy
-   pygetwindow
-   pywin32

### 4. Run the Application

python main.py

A camera window (HUD) will open.

------------------------------------------------------------------------

## Usage

1.  Open a PDF file in Brave browser.
2.  Click inside the PDF to ensure Brave is the active window.
3.  Keep the Gesture Reader window open.

### Scrolling

-   Thumb extended (out) enables scroll mode.
-   Move your hand up or down to scroll.
-   Thumb tucked (in) disables scrolling.

### Zooming

-   Pinch (touch index finger and thumb) on both hands.
-   Move hands apart to zoom in.
-   Move hands closer together to zoom out.
-   Release pinch on either hand to exit zoom mode.

### Exit

Press `Q` inside the Gesture Reader window to close the application.

------------------------------------------------------------------------

## Technical Overview

The system operates as follows:

1.  OpenCV captures frames from the webcam.
2.  MediaPipe detects hand landmarks in real time.
3.  Scroll mode is activated based on thumb position.
4.  Zoom mode is activated when both hands perform a pinch gesture.
5.  PyAutoGUI injects scroll and zoom input into the system.
6.  PyGetWindow ensures input is only sent when Brave is the active
    window.

------------------------------------------------------------------------

## Known Limitations

-   Designed specifically for Brave browser (window title matching).
-   Requires adequate lighting for reliable tracking.
-   Performance may vary depending on hardware.
-   Currently runs as a foreground application (HUD must remain open).

------------------------------------------------------------------------

## Future Improvements

-   Configurable target browser or application
-   Adjustable scroll sensitivity
-   Scroll smoothing and acceleration curve
-   Zoom sensitivity tuning
-   GUI-based configuration panel
-   Background/system tray mode
-   Cross-platform support

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

Developed by Vaibhav Vasant
