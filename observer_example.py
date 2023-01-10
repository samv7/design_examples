'''Simple Observer design pattern example'''
from __future__ import annotations
from abc import ABC, abstractmethod, ABCMeta
from random import randint

class Observable(ABC):

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
      raise NotImplementedError

    @abstractmethod
    def notify_observers(self) -> None:
      raise NotImplementedError

class WeatherMonitor(Observable):

    def __init__(self) -> None:
      self._observers = []
      self._temperature = 0
      self._wind_speed = 0
      self.refresh_weather()

    def add_observer(self, observer: Observer) -> None:
      self._observers.append(observer)

    def notify_observers(self, msg: str) -> None:
      for observer in self._observers:
        observer.notify(msg)

    def refresh_weather(self):
      self._temperature = randint(0, 40)
      self._wind_speed = randint(0, 40)
      self.notify_observers(msg=f"temperature:{self._temperature},wind_speed:{self._wind_speed}")



class Observer(ABC):

    @abstractmethod
    def notify(self, msg: str) -> None:
      raise NotImplementedError

class WeatherObserver(Observer):

    def __init__(self, name: str, weather_monitor: WeatherMonitor) -> None:
      self._name = name
      weather_monitor.add_observer(self)

    def notify(self, msg: str) -> None:
      print(f"{self._name} received message: {msg}")


if __name__ == "__main__":
    

    weather_monitor = WeatherMonitor()
    weather_observer1 = WeatherObserver("observer1", weather_monitor)
    weather_observer2 = WeatherObserver("observer2", weather_monitor)

    print("Updating weather")
    weather_monitor.refresh_weather()
    print("Updating weather again")
    weather_monitor.refresh_weather()
