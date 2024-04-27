from abc import ABC, abstractmethod

class IModelRepo(ABC):
    @abstractmethod
    def metodo(self):
        ...
        
class ModelRepo(IModelRepo):
    def metodo(self):
        pass