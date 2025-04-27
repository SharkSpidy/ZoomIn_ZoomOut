import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread('prof1.png')


    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            print("Zoom")



    img[0:500, 0:500] = img1
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break