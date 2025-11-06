from abc import ABC, abstractmethod

class IDisplayDecorator(ABC):
    
    @abstractmethod
    def show(self) -> str:
        pass