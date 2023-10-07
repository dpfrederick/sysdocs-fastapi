from dataclasses import dataclass
from datetime import datetime
from typing import Final, final


@dataclass
@final
class Zone:
    id: Final[int]
    name: Final[str]
    version: Final[int]
