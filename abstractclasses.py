from abc import ABC, abstractmethod

class API(ABC):
    @abstractmethod
    def ConnectionAPI(self, url: str=None) -> None:
        ...

    @abstractmethod
    def DataPreparation(self) -> None:
        ...