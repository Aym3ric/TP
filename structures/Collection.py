from abc import ABC, abstractmethod

class Collection(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item=None):
        pass

    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass