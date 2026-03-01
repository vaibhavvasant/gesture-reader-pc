# GestureReader

Gesture-controlled PDF reader for Brave browser.

## Features
- Thumb OUT = Scroll mode
- Thumb IN = Disabled
- Two-hand pinch = Zoom
- Works only when Brave is active

---

## Setup Instructions (Windows)

1. Install Python 3.10
2. Clone the repository:

   git clone <your-repo-url>
   cd gesture_reader

3. Create virtual environment:

   py -3.10 -m venv venv
   venv\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the app:

   python main.py

---

## Controls

Thumb OUT → Scroll  
Two-hand pinch → Zoom  
Press Q → Quit