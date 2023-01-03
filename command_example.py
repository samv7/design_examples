'''A toy example translated from Wikipedia'''

from abc import ABCMeta, abstractmethod

class ICommand:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        raise NotImplementedError


# The Invoker class 
class Switch(object):

    def __init__(self, closed_command : ICommand, opened_command: ICommand):
        self._closed_command = closed_command
        self._opened_command = opened_command

    # Close the circuit / power on
    def close(self):
        self._closed_command.execute()

    # Open the circuit / power off
    def open(self):
        self._opened_command.execute()
  

#An interface that defines actions that the receiver can perform
class ISwitchable:

    __metaclass__ = ABCMeta

    @abstractmethod
    def power_on(self):
        raise NotImplementedError

    @abstractmethod
    def power_off(self):
        raise NotImplementedError


# The Receiver class 
class Light(ISwitchable):

    def power_on(self):
        print("The light is on")

    def power_off(self):
        print("The light is off")
    


# The Command for turning off the device - ConcreteCommand #1
class CloseSwitchCommand(ICommand):

    def __init__(self, switchable : ISwitchable):
        self._switchable = switchable

    def execute(self):
        self._switchable.power_off()


# The Command for turning on the device - ConcreteCommand #2
class OpenSwitchCommand(ICommand):

    def __init__(self, switchable : ISwitchable):
       self._switchable = switchable

    def execute(self):
        self._switchable.power_on()
    

def main():

    lamp = Light()

    # Pass reference to the lamp instance to each command
    switch_close = CloseSwitchCommand(lamp)
    switch_open = OpenSwitchCommand(lamp)

    # Pass reference to instances of the Command objects to the switch
    switch = Switch(switch_close, switch_open);


    # Switch (the Invoker) will invoke Execute() on the command object.
    switch.open()
    
    # Switch (the Invoker) will invoke the Execute() on the command object.
    switch.close()
        
