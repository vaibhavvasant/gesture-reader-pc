# main.py

import cv2
import pygetwindow as gw
from gesture_detector import GestureDetector
from action_controller import ActionController

TARGET_APP_KEYWORD = "Brave"  # Change if needed

def is_target_window_active():
    try:
        active = gw.getActiveWindow()
        if active and TARGET_APP_KEYWORD.lower() in active.title.lower():
            return True
    except:
        pass
    return False

def draw_hud(frame, gesture, active, thumb_active):
    h, w, _ = frame.shape

    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 80), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

    status_text = "ACTIVE" if active else "INACTIVE"
    status_color = (0,255,0) if active else (0,0,255)

    thumb_text = "SCROLL MODE" if thumb_active else "RELAXED"
    thumb_color = (255,255,0) if thumb_active else (100,100,100)

    cv2.putText(frame, f"Window: {status_text}", (20,25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    cv2.putText(frame, f"Hand: {thumb_text}", (20,55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, thumb_color, 2)

    return frame

def main():
    cap = cv2.VideoCapture(0)
    detector = GestureDetector()
    controller = ActionController()

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        gesture, frame, thumb_active, zoom_delta = detector.detect(frame)
        active = is_target_window_active()

        # ---- ZOOM ----
        if active and zoom_delta:
            if abs(zoom_delta) > 5:
                if zoom_delta > 0:
                    controller.zoom_in()
                else:
                    controller.zoom_out()

        # ---- SCROLL ----
        elif active and thumb_active and gesture:
            scroll_strength = int(gesture * -1.2)  # FLIPPED direction
            controller.dynamic_scroll(scroll_strength)

        frame = draw_hud(frame, gesture, active, thumb_active)
        cv2.imshow("Gesture Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()