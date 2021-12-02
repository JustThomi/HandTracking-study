import cv2
import mediapipe


class Hand_detector():
    def __init__(self):
        self.hand_solutions = mediapipe.solutions.hands
        self.hands = self.hand_solutions.Hands()
        self.draw = mediapipe.solutions.drawing_utils


    def get_landmarks(self, img):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            landmarks = results.multi_hand_landmarks

            landmark_list = []
            if landmarks:
                for hand in landmarks:
                    for index_lm, lm in enumerate(hand.landmark):
                        hight, width, channel = img.shape
                        pixel_x, pixel_y = int(lm.x * width), int(lm.y * hight)
                        landmark_list.append((pixel_x, pixel_y))

            return landmark_list