import board
import constants
import digitalio

from adafruit_debouncer import Debouncer

class ButtonHandler:
    def __init__(self):
        print("init buttonHandler")

    def defineButton (self, pin):
        digitalInput = digitalio.DigitalInOut(pin)
        digitalInput.direction = digitalio.Direction.INPUT
        digitalInput.pull = digitalio.Pull.DOWN
        return digitalInput

    def __enter__ (self):
        print("enter buttonHandler")
        buttonDictionary = {}
        buttonDictionary[constants.POWER_BTN] = Debouncer(self.defineButton(board.GP3))
        buttonDictionary[constants.ENGINES_BTN] = Debouncer(self.defineButton(board.GP4))
        buttonDictionary[constants.SHIELDS_BTN] = Debouncer(self.defineButton(board.GP5))
        buttonDictionary[constants.WEAPONS_BTN] = Debouncer(self.defineButton(board.GP6))
        buttonDictionary[constants.LIGHTS_BTN] = Debouncer(self.defineButton(board.GP7))
        buttonDictionary[constants.LANDING_GEAR_BTN] = Debouncer(self.defineButton(board.GP8))
        buttonDictionary[constants.VTOL_BTN] = Debouncer(self.defineButton(board.GP0))
        buttonDictionary[constants.COUPLED_BTN] = Debouncer(self.defineButton(board.GP1))
        buttonDictionary[constants.CRUISE_BTN] = Debouncer(self.defineButton(board.GP2))
        buttonDictionary[constants.QUANTUM_BTN] = Debouncer(self.defineButton(board.GP9))
        buttonDictionary[constants.JUMP_BTN] = Debouncer(self.defineButton(board.GP10))
        return buttonDictionary

    def __exit__ (self, buttonDictionary):
        for button in buttonDictionary:
            button.deinit()
        print("exit buttonHandler")