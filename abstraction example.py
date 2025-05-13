
from abc import ABC
class Machine(ABC):
    def turn_on(self):
        pass
    def turn_off(self):
        passn  
class WashingMachine(Machine):
    def __init__(self):
        self._is_on = False
    def turn_on(self):
        self._is_on = True
        print("Washing machine is ON.")
        self._wash()
    def turn_off(self):
        self._is_on = False
        print("Washing machine is OFF.")
    def _wash(self):
        if self._is_on:
            print("Washing...")
        else:
            print("Please turn on the washing machine first.")
machine = WashingMachine()
machine.turn_on()
machine.turn_off()
