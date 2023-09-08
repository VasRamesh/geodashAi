import cv2 as cv
import numpy as np
import pyautogui
import keyboard

def collect_img_data():

    while True:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        cv.imshow('Computer Vision', screenshot)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    print("Done")


collect_img_data()


