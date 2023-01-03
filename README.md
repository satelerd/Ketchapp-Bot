# Ketchapp-Bot

A bot that play the Ketchapp Knife Hit game fully autonomously using cv2.

## How to use?

1. Clone the repository.
2. Install the libraries (cv2, pyautogui and time) through the cmd (pip install).
3. Now open a the [knife hit game](https://www.minijuegos.com/juego/knife-hit) (or any other page with the game), start the game and put it in the middle of the screen (over the restart button).
4. Lastly, run the script (and put the mouse on the position of step 3). 
Now you can enjoy the bot playing the game. 

5. (Adittional step) If the bot is not working, you can enable the preview mode by changing the variable `preview` (on line 10) to `True` in the script. This will show you a window with what the bot is seeing. 
You may need to adjust the variable `region` (line 11) for the bot to see the game window.
