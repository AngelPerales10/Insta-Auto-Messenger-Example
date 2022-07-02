# to call time commands (delays)
import time

# for mouse clicks and typing
import pyautogui

# moving to upper left hand will stop macro incase anything goes wrong
pyautogui.FAILSAFE = True

# Note: Delays and pauses spread out over time due to potential
# macro mistakes and limits of sending 40 messages per hour

# ------- Start -------

times_you_want_to_loop = 4

loop = 0

user1 = 'username1'
user2 = 'username2'
user3 = 'username3'
user4 = 'username4'

pwd1 = 'password1'
pwd2 = 'password2'
pwd3 = 'password3'
pwd4 = 'password4'

proxy1 = '123.456.789.01'
proxy2 = '123.456.789.02'
proxy3 = '123.456.789.03'
proxy4 = '123.456.789.04'

message1 = 'This is a test message'
message2 = 'This is a 2nd test message'
message3 = 'This is a 3rd test message'
message4 = 'This is a 4th test message'

while loop < times_you_want_to_loop:

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
    pyautogui.typewrite(proxy1)

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
    pyautogui.typewrite(user1)

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(pwd1)

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
    pyautogui.typewrite(message1, interval=0.2)
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
    pyautogui.typewrite(proxy2)

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
    pyautogui.typewrite(user2)

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(pwd2)

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
    pyautogui.typewrite(message2, interval=0.2)
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
    pyautogui.typewrite(proxy3)

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
    pyautogui.typewrite(user3)

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(pwd3)

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
    pyautogui.typewrite(message3, interval=0.2)
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
    pyautogui.typewrite(proxy4)

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
    pyautogui.typewrite(user4)

    # INFO - click on old password
    pyautogui.PAUSE = 2.5
    pyautogui.click(599, 399)

    # add new password
    pyautogui.PAUSE = 2.5
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite(pwd4)

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
    pyautogui.typewrite(message4, interval=0.2)
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
