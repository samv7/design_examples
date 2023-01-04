'''Factory example translated from Wikipedia'''

from abc import ABCMeta, abstractmethod
from enum import Enum


class IPerson:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

class Villager(IPerson):

    def get_name(self) -> str:
        return "Village Person"
    
class CityPerson(IPerson):

    def get_name(self) -> str:
        return "City Person"


class PersonType(Enum):
    Rural = 1
    Urban = 2

class Factory:
    def get_person(self, type: PersonType) -> IPerson:

        if type == PersonType.Rural:
            return Villager()
        elif type == PersonType.Urban:
            return CityPerson()
        else:
            raise NotImplementedError

def main() -> None:
    person1 = Factory().get_person(PersonType.Rural)
    print(person1.get_name())
    
    person2 = Factory().get_person(PersonType.Urban)
    print(person2.get_name())
    

if __name__ == "__main__":
    main()  
