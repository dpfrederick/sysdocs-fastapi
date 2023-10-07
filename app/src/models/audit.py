from dataclasses import dataclass
from datetime import datetime
from typing import Final, final


@dataclass
@final
class Audit:
    id: Final[int]
    action: Final[str]
    content: Final[str]
    timestamp: Final[datetime]
