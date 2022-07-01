# to call time commands (delays)
import time

# for mouse clicks and typing
import pyautogui

# moving to upper left hand will stop macro incase anything goes wrong
pyautogui.FAILSAFE = True

# - PROXY , - INFO , & MESSAGE to ctrl f and find to replace if needed

# Note: Delays and pauses spread out over time due to potential
# macro mistakes and limits of sending 40 messages per hour

# ------- Start -------

times_you_want_to_loop = 4

loop = 0

while loop != times_you_want_to_loop:

    # CYCLE 1 ----------------------------------------

    # open settings
    pyautogui.PAUSE = 2.5
    pyautogui.click(410, 1070)

    # click on proxy
    pyautogui.PAUSE = 2.5
    pyautogui.click(423, 699)

    # selecting all and deleting
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

    # PROXY - adding proxy
    pyautogui.typewrite('123.456.789.00')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on old username
    pyautogui.PAUSE = 2.5
    pyautogui.click(569, 354)

    # INFO - add new username
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('Username1')

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('password1')

    # log in
    pyautogui.PAUSE = 2.5
    pyautogui.click(364, 151)

    # click on messages
    pyautogui.PAUSE = 2.5
    pyautogui.click(721, 109)

    # click to icon to type new user
    pyautogui.PAUSE = 2.5
    pyautogui.click(335, 178)

    # cuts username
    pyautogui.PAUSE = 2.5
    pyautogui.click(1016, 115)
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    time.sleep(1)
    pyautogui.click(1854, 110)
    pyautogui.keyUp('shiftleft')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')

    # re-adjusts sheet
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('backspace')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on 'To:'
    pyautogui.PAUSE = 2.5
    pyautogui.click(342, 316)

    # click on 'Next' and wait to load profile
    pyautogui.PAUSE = 2.5
    pyautogui.click(632, 269)
    time.sleep(4)

    # click on message bar
    pyautogui.PAUSE = 2.5
    pyautogui.click(646, 963)

    # MESSAGE - type out message and send
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite('Example message #1', interval=0.2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    # click on my user icon
    pyautogui.PAUSE = 2.5
    pyautogui.click(912, 102)

    # log out
    pyautogui.PAUSE = 2.5
    pyautogui.click(784, 307)

    # CYCLE 2 ----------------------------------------

    # open settings
    pyautogui.PAUSE = 2.5
    pyautogui.click(410, 1070)

    # click on proxy
    pyautogui.PAUSE = 2.5
    pyautogui.click(423, 699)

    # selecting all and deleting
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

    # PROXY - adding proxy
    pyautogui.typewrite('001.234.567.89')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on old username
    pyautogui.PAUSE = 2.5
    pyautogui.click(569, 354)

    # INFO - add new username
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('Username2')

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('password2')

    # log in
    pyautogui.PAUSE = 2.5
    pyautogui.click(364, 151)

    # click on messages
    pyautogui.PAUSE = 2.5
    pyautogui.click(721, 109)

    # click to icon to type new user
    pyautogui.PAUSE = 2.5
    pyautogui.click(335, 178)

    # cuts username
    pyautogui.PAUSE = 2.5
    pyautogui.click(1016, 115)
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    time.sleep(1)
    pyautogui.click(1854, 110)
    pyautogui.keyUp('shiftleft')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')

    # re-adjusts sheet
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('backspace')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on 'To:'
    pyautogui.PAUSE = 2.5
    pyautogui.click(342, 316)

    # click on 'Next' and wait to load profile
    pyautogui.PAUSE = 2.5
    pyautogui.click(632, 269)
    time.sleep(4)

    # click on message bar
    pyautogui.PAUSE = 2.5
    pyautogui.click(646, 963)

    # MESSAGE - type out message and send
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite('Example message #2', interval=0.2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    # click on my user icon
    pyautogui.PAUSE = 2.5
    pyautogui.click(912, 102)

    # log out
    pyautogui.PAUSE = 2.5
    pyautogui.click(784, 307)

    # CYCLE 3 ----------------------------------------

    # open settings
    pyautogui.PAUSE = 2.5
    pyautogui.click(410, 1070)

    # click on proxy
    pyautogui.PAUSE = 2.5
    pyautogui.click(423, 699)

    # selecting all and deleting
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

    # PROXY - adding proxy
    pyautogui.typewrite('987.654.321.00')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on old username
    pyautogui.PAUSE = 2.5
    pyautogui.click(569, 354)

    # INFO - add new username
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('Username3')

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('password3')

    # log in
    pyautogui.PAUSE = 2.5
    pyautogui.click(364, 151)

    # click on messages
    pyautogui.PAUSE = 2.5
    pyautogui.click(721, 109)

    # click to icon to type new user
    pyautogui.PAUSE = 2.5
    pyautogui.click(335, 178)

    # cuts username
    pyautogui.PAUSE = 2.5
    pyautogui.click(1016, 115)
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    time.sleep(1)
    pyautogui.click(1854, 110)
    pyautogui.keyUp('shiftleft')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')

    # re-adjusts sheet
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('backspace')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on 'To:'
    pyautogui.PAUSE = 2.5
    pyautogui.click(342, 316)

    # click on 'Next' and wait to load profile
    pyautogui.PAUSE = 2.5
    pyautogui.click(632, 269)
    time.sleep(4)

    # click on message bar
    pyautogui.PAUSE = 2.5
    pyautogui.click(646, 963)

    # MESSAGE - type out message and send
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite('Example message #3', interval=0.2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    # click on my user icon
    pyautogui.PAUSE = 2.5
    pyautogui.click(912, 102)

    # log out
    pyautogui.PAUSE = 2.5
    pyautogui.click(784, 307)

    # CYCLE 4 ----------------------------------------

    # open settings
    pyautogui.PAUSE = 2.5
    pyautogui.click(410, 1070)

    # click on proxy
    pyautogui.PAUSE = 2.5
    pyautogui.click(423, 699)

    # selecting all and deleting
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

    # PROXY - adding proxy
    pyautogui.typewrite('456.789.001.23')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on old username
    pyautogui.PAUSE = 2.5
    pyautogui.click(569, 354)

    # INFO - add new username
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('Username4')

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('password4')

    # log in
    pyautogui.PAUSE = 2.5
    pyautogui.click(364, 151)

    # click on messages
    pyautogui.PAUSE = 2.5
    pyautogui.click(721, 109)

    # click to icon to type new user
    pyautogui.PAUSE = 2.5
    pyautogui.click(335, 178)

    # cuts username
    pyautogui.PAUSE = 2.5
    pyautogui.click(1016, 115)
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    time.sleep(1)
    pyautogui.click(1854, 110)
    pyautogui.keyUp('shiftleft')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')

    # re-adjusts sheet
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('backspace')

    # click on chrome
    pyautogui.PAUSE = 2.5
    pyautogui.click(464, 1059)

    # click on 'To:'
    pyautogui.PAUSE = 2.5
    pyautogui.click(342, 316)

    # click on 'Next' and wait to load profile
    pyautogui.PAUSE = 2.5
    pyautogui.click(632, 269)
    time.sleep(4)

    # click on message bar
    pyautogui.PAUSE = 2.5
    pyautogui.click(646, 963)

    # MESSAGE - type out message and send
    pyautogui.PAUSE = 2.5
    pyautogui.typewrite('Example message #4', interval=0.2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    # click on my user icon
    pyautogui.PAUSE = 2.5
    pyautogui.click(912, 102)

    # log out
    pyautogui.PAUSE = 2.5
    pyautogui.click(784, 307)

    loop += 1
