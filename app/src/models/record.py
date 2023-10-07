from dataclasses import dataclass
from datetime import datetime
from typing import Final, final


@dataclass
@final
class Record:
    id: Final[int]
    zone_id: Final[int]
    type: Final[str]
    value: Final[str]
    version: Final[int]
