import constants
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboardHid = Keyboard(usb_hid.devices)

def holdButton():
    time.sleep(constants.KEY_HOLD_DURATION)

def powerButtonAction():
    keyboardHid.send(Keycode.U)

def enginesButtonAction():
    keyboardHid.send(Keycode.I)

def shieldsButtonAction():
    keyboardHid.send(Keycode.O)

def weaponsButtonAction():
    keyboardHid.send(Keycode.P)

def lightsButtonAction():
    keyboardHid.send(Keycode.L)

def landingGearButtonAction():
    keyboardHid.send(Keycode.N)

def vtolButtonAction():
    keyboardHid.send(Keycode.K)

def coupledButtonAction():
    keyboardHid.send(Keycode.LEFT_ALT,Keycode.C)

def cruiseButtonAction():
    keyboardHid.send(Keycode.C)

def quantumButtonAction():
    keyboardHid.send(Keycode.B)

def jumpButtonAction():
    keyboardHid.press(Keycode.B)
    holdButton()
    keyboardHid.release(Keycode.B)

def updateDebouncer(buttonDictionary):
    buttonDictionary[constants.POWER_BTN].update()
    buttonDictionary[constants.ENGINES_BTN].update()
    buttonDictionary[constants.SHIELDS_BTN].update()
    buttonDictionary[constants.WEAPONS_BTN].update()
    buttonDictionary[constants.LIGHTS_BTN].update()
    buttonDictionary[constants.LANDING_GEAR_BTN].update()
    buttonDictionary[constants.VTOL_BTN].update()
    buttonDictionary[constants.COUPLED_BTN].update()
    buttonDictionary[constants.CRUISE_BTN].update()
    buttonDictionary[constants.QUANTUM_BTN].update()
    buttonDictionary[constants.JUMP_BTN].update()

def scanButtons(buttonDictionary):
    updateDebouncer(buttonDictionary)
    if buttonDictionary[constants.POWER_BTN].rose or buttonDictionary[constants.POWER_BTN].fell:
        powerButtonAction()

    elif buttonDictionary[constants.ENGINES_BTN].rose or buttonDictionary[constants.ENGINES_BTN].fell:
        enginesButtonAction()

    elif buttonDictionary[constants.SHIELDS_BTN].rose or buttonDictionary[constants.SHIELDS_BTN].fell:
        shieldsButtonAction()

    elif buttonDictionary[constants.WEAPONS_BTN].rose or buttonDictionary[constants.WEAPONS_BTN].fell:
        weaponsButtonAction()

    elif buttonDictionary[constants.LIGHTS_BTN].rose or buttonDictionary[constants.LIGHTS_BTN].fell:
        lightsButtonAction()

    elif buttonDictionary[constants.LANDING_GEAR_BTN].rose or buttonDictionary[constants.LANDING_GEAR_BTN].fell:
        landingGearButtonAction()

    elif buttonDictionary[constants.VTOL_BTN].rose:
        vtolButtonAction()

    elif buttonDictionary[constants.COUPLED_BTN].rose:
        coupledButtonAction()

    elif buttonDictionary[constants.CRUISE_BTN].rose:
        cruiseButtonAction()

    elif buttonDictionary[constants.QUANTUM_BTN].rose:
        quantumButtonAction()

    elif buttonDictionary[constants.JUMP_BTN].rose:
        jumpButtonAction()