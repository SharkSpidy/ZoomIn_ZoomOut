import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
scale = 0
cx, cy = 500, 500
startDist = None

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread('1.png')


    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            
            if startDist is None:
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDist = length
            
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int(length - startDist)//2
            cx, cy = info[4:]
            #print(scale)
    else:
        startDist = None

    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale)//2)*2, ((w1 + scale)//2)*2
        img1 = cv2.resize(img1, (newW, newH))


        img[cy-newH//2 :cy + newH//2, cx-newW//2 :cx + newW//2] = img1
    except:
        pass


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break