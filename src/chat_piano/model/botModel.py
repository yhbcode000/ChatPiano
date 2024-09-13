from dataclasses import dataclass

from src.control.services import BaseBot


@dataclass
class BotModel:
    api_key: str = None
    bot: BaseBot = None
