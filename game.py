import cv2
import cvzone
import mediapipe
from handtracking import handDetector
import os
import time
import random


images = r"C:\Users\User\Desktop\Ccoder\opencv\game_images\hands"
img_list = os.listdir(images)
image_list = []
for i in img_list:
    img = cv2.imread(f'{images}/{i}')
    image_list.append(img)
print(len(image_list))

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = handDetector(maxHands=1)


# Check the fingers which are held up
def fingers_up(fingers):
    if (fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1):
        return "Paper"
    elif (fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0):
        return "Scissors"
    elif (fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0):
        return "Rock"


# using a timer and flag variables for the display..
timer = 0
res = False
flag = False
scores = [0, 0]

while True:
    background_img = cv2.imread(
        r"C:\Users\User\Desktop\Ccoder\opencv\game_images\background.jpg")
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # Resize the web cam image and fit it into the player image of the background
    im_resize = cv2.resize(img, (0, 0), None, 0.4875, 0.4875)
    im_resize = im_resize[:, 14:290]

    # Resize the im_resize to match the dimensions of the region in background_img
    im_resize = cv2.resize(im_resize, (279, 230))
    im = detector.find_hands(im_resize)

    lmlist = detector.find_pos(im, draw=False)

    if flag == True:
        if res is False:
            timer = time.time()-initial
            cv2.putText(background_img, str(int(timer)), (274, 125),
                        cv2.FONT_HERSHEY_PLAIN, 3.0, (0, 0, 0), 4)
            # Let the time work till 3 seconds..
            if (timer > 3):
                res = True
                timer = 0  # Set the timer back to 0..
                if (len(lmlist) != 0):
                    # Use the predefined method fingers_up  to check the fingers which are up
                    fingers = detector.fingers_up()
                    print(fingers)
                    user_move = fingers_up(fingers)
                    print(user_move)

                    # Get a random index between 0 to 2
                    index = random.randint(0, 2)
                    # Choose the image at index
                    ai_img = image_list[index]
                    # AI Images.. 0->paper 1->rock  2->scissor
                    if (user_move == 'Paper'):
                        if (index == 2):
                            scores[0] += 1
                        elif (index == 1):
                            scores[1] += 1
                    elif (user_move == 'Rock'):
                        if (index == 0):
                            scores[0] += 1
                        elif (index == 2):
                            scores[1] += 1
                    elif (user_move == 'Scissors'):
                        if (index == 1):
                            scores[0] += 1
                        elif (index == 0):
                            scores[1] += 1
    background_img[182:412, 312:591] = im_resize

    if res == True:
        # Fit this image in the AI BOX
        background_img[182:412, 25:244] = ai_img
    cv2.putText(background_img, str(int(scores[0])), (206, 175),
                cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), 4)
    cv2.putText(background_img, str(int(scores[1])), (493, 176),
                cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), 4)

    cv2.imshow("background", background_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        flag = True
        initial = time.time()
        res = False
