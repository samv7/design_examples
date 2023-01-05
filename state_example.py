from __future__ import annotations
from abc import abstractmethod, ABCMeta

class VendingMachine:

    _state = None

    def __init__(self, state: State) -> None:
        self.switch_to(state)

    def switch_to(self, state: State):
        print(f"Vending Machine: Switching to {type(state).__name__}")
        self._state = state
        self._state.vending_machine = self

    def pay(self) -> None:
        self._state.insert_payment()

    def choose(self) -> None:
        self._state.select_item()

class State():

    __metaclass__ = ABCMeta

    @property
    def vending_machine(self) -> VendingMachine:
        return self._vending_machine

    @vending_machine.setter
    def vending_machine(self, vending_machine: VendingMachine) -> None:
        self._vending_machine = vending_machine

    @abstractmethod
    def insert_payment(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def select_item(self) -> None:
        raise NotImplementedError


class WaitingState(State):

    def insert_payment(self) -> None:
        print("Thanks for your payment")
        self._vending_machine.switch_to(SelectingState())

    def select_item(self) -> None:
        print("Please insert a payment")


class SelectingState(State):

    def insert_payment(self) -> None:
        print("Payment already inserted. Please select an item")
        
    def select_item(self) -> None:
        print("Thanks for selecting an item")
        self._vending_machine.switch_to(DispensingState())

class DispensingState(State):

    def insert_payment(self) -> None:
        print("Payment already inserted.")

    def select_item(self) -> None:
        print("Now dispensing your item")
        self._vending_machine.switch_to(WaitingState())
        print("Please insert payment to select another item.")

if __name__ == "__main__":
    
    vending_machine = VendingMachine(WaitingState())
    vending_machine.pay()
    vending_machine.choose()
    vending_machine.choose()
