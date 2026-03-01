# gesture_detector.py

import mediapipe as mp
import cv2
import math


class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        # Scroll state
        self.prev_y = None

        # Zoom state
        self.prev_zoom_distance = None

    # --------------------------------------------------
    # THUMB OUT DETECTION (Works for both hands)
    # --------------------------------------------------
    def thumb_out(self, landmarks, handedness_label):
        """
        Returns True if thumb is extended outward.
        Handles both Left and Right hands correctly.
        """

        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]

        if handedness_label == "Right":
            return thumb_tip.x < thumb_ip.x
        else:  # Left hand
            return thumb_tip.x > thumb_ip.x

    # --------------------------------------------------
    # PINCH DETECTION
    # --------------------------------------------------
    def is_pinching(self, landmarks):
        """
        Detects if index finger tip and thumb tip are touching.
        """
        dx = landmarks[4].x - landmarks[8].x
        dy = landmarks[4].y - landmarks[8].y
        distance = math.sqrt(dx * dx + dy * dy)

        return distance < 0.05  # Adjust if needed

    def get_pinch_position(self, landmarks, w, h):
        """
        Returns midpoint of thumb tip and index tip in pixel coordinates.
        """
        x = int((landmarks[4].x + landmarks[8].x) / 2 * w)
        y = int((landmarks[4].y + landmarks[8].y) / 2 * h)
        return x, y

    # --------------------------------------------------
    # MAIN DETECTION LOGIC
    # --------------------------------------------------
    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if not results.multi_hand_landmarks:
            self.prev_y = None
            self.prev_zoom_distance = None
            return None, frame, False, None

        hands = results.multi_hand_landmarks
        handedness = results.multi_handedness
        h, w, _ = frame.shape

        # Draw landmarks
        for hand_landmarks in hands:
            self.mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS
            )

        # ==================================================
        # ZOOM MODE (Two-hand pinch)
        # ==================================================
        if len(hands) == 2:
            pinch_states = []
            pinch_positions = []

            for i, hand in enumerate(hands):
                landmarks = hand.landmark
                pinch_states.append(self.is_pinching(landmarks))
                pinch_positions.append(
                    self.get_pinch_position(landmarks, w, h)
                )

            # If both hands pinching → zoom mode
            if all(pinch_states):
                x1, y1 = pinch_positions[0]
                x2, y2 = pinch_positions[1]

                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                zoom_delta = None

                if self.prev_zoom_distance is not None:
                    zoom_delta = distance - self.prev_zoom_distance

                self.prev_zoom_distance = distance

                # Disable scroll while zooming
                self.prev_y = None

                return None, frame, False, zoom_delta

            else:
                self.prev_zoom_distance = None

        # ==================================================
        # SCROLL MODE (Single hand, thumb OUT)
        # ==================================================
        hand = hands[0]
        landmarks = hand.landmark
        handed_label = handedness[0].classification[0].label

        y = int(landmarks[8].y * h)

        thumb_active = self.thumb_out(landmarks, handed_label)

        scroll_velocity = None

        if thumb_active and self.prev_y is not None:
            dy = y - self.prev_y

            if abs(dy) > 3:  # small deadzone
                scroll_velocity = dy

        self.prev_y = y

        return scroll_velocity, frame, thumb_active, None