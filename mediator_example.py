from typing import List, Callable

class Mediator:
    def __init__(self):
        self.message_received: List[Callable[[str, str], None]] = []

    def subscribe(self, callback: Callable[[str, str], None]):
        self.message_received.append(callback)

    def send(self, message: str, sender: str):
        for callback in self.message_received:
            callback(message, sender)

class Person:

    def __init__(self, mediator:"Mediator", name: str):
        self._mediator = mediator
        self._name = name
        self._mediator.subscribe(self._receive)

    def _receive(self, message: str, sender: str):
        if sender != self._name:
            print(f"{self._name} received {message} from {sender}")

    def send(self, message: str):
        self._mediator.send(message, self._name)

def main() -> None:
    mediator = Mediator()      
    bob = Person(mediator, "Bob")
    alice = Person(mediator, "Alice")
    charlie = Person(mediator, "Charlie")
    bob.send("Hello World!")

if __name__ == "__main__":
    main()

