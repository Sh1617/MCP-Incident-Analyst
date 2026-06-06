from abc import ABC
from abc import abstractmethod


class BaseAgent(ABC):

    name: str

    @abstractmethod
    async def execute(
        self,
        state: dict
    ):
        pass