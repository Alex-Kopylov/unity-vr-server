import mediapipe as mp
import mediapipe.python.solutions.drawing_utils as mp_drawing
import mediapipe.python.solutions.hands as mp_hands

from .MediapipeLandmark import MediapipeLandmark


class MediapipeHand:

    def __init__(self, hand_landmark):
        self.landmarks = []

        count = 0
        for landmark in hand_landmark.landmark:
            name = mp_hands.HandLandmark(count).name
            self.landmarks.append(MediapipeLandmark(name, landmark))
            count += 1

    def __str__(self):
        return "|".join([str(x) for x in self.landmarks])
