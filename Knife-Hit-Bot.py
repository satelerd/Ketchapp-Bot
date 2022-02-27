import cv2
import pyautogui
import numpy as np
import time

"""
THINGS TO MODIFY
"""
# PATH to Ketchapp-Bot folder
path = r"C:\Users\satel\OneDrive\code\Artilujios\Ketchapp-Bot"

# Preview where the screenshot is taken and what cv2 is seeing
preview = True  # True or False
region = (700, 550, 550, 150)  # update this to your screenshot location
"""
END OF THINGS TO MODIFY
"""

# Uploading images
not_knife_img2 = cv2.imread(
    rf"{path}\img\not_knife2.png",
    cv2.COLOR_BGR2GRAY,
)
not_knife_img3 = cv2.imread(
    rf"{path}\img\not_knife3.png",
    cv2.COLOR_BGR2GRAY,
)
knife_img = cv2.imread(
    rf"{path}\img\nailed_knife.png",
    cv2.COLOR_BGR2GRAY,
)
knife_45_img = cv2.imread(
    rf"{path}\img\nailed_knife_45.png",
    cv2.COLOR_BGR2GRAY,
)
flip_knife_45_img = cv2.flip(knife_45_img, 1)

# Img for search
searching1 = knife_img
searching2 = knife_45_img
searching3 = flip_knife_45_img

cont = 0
# Game loop
while True:
    time1 = time.time()

    # Take the screenshot and save it
    ss = pyautogui.screenshot(region=region)
    ss.save(rf"{path}\screenshots\ss1.png")
    ss1 = cv2.imread(
        rf"{path}\screenshots\ss1.png",
        cv2.COLOR_BGR2GRAY,
    )

    # searching for the img
    result1 = cv2.matchTemplate(
        ss1.astype(np.float32), searching1.astype(np.float32), cv2.TM_CCOEFF_NORMED
    )
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

    result2 = cv2.matchTemplate(ss1, searching2, cv2.TM_CCOEFF_NORMED)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

    result3 = cv2.matchTemplate(ss1, searching3, cv2.TM_CCOEFF_NORMED)
    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)

    if max_val1 <= 0.7 and max_val2 <= 0.53 and max_val3 <= 0.53:
        pyautogui.click()
        print("shoot the knife")

    else:
        print("dont shoot the knife")

    time2 = time.time()
    print(f"time: {time2-time1}")
    time.sleep(0.1)

    if preview:
        # Creating the rectagle where found the img and display it
        w = searching1.shape[1]
        h = searching1.shape[0]
        cv2.rectangle(ss1, max_loc1, (max_loc1[0] + w, max_loc1[1] + h), (0, 0, 255), 2)
        w = searching2.shape[1]
        h = searching2.shape[0]
        cv2.rectangle(ss1, max_loc2, (max_loc2[0] + w, max_loc2[1] + h), (0, 0, 255), 2)
        w = searching3.shape[1]
        h = searching3.shape[0]
        cv2.rectangle(ss1, max_loc3, (max_loc3[0] + w, max_loc3[1] + h), (0, 0, 255), 2)
        cv2.imshow("img", ss1)
        cv2.waitKey()
        cv2.destroyAllWindows()

    cont += 1
    if cont == 1000:
        break
