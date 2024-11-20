from __future__ import print_function
import cv2 as cv
import argparse
from detection import bodyDetection
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
camera_device = args.camera

#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
cap.set(3,480) #CV_CAP_PROP_FRAME_WIDTH
cap.set(4,360) #CV_CAP_PROP_FRAME_HEIGHT
cap.set(cv.CAP_PROP_FPS, 120)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    bodyDetection(frame, face_cascade, 'img/tshirt_1.png')
    if cv.waitKey(10) == 27:
        cap.release()
        cv.destroyAllWindows()
        break
