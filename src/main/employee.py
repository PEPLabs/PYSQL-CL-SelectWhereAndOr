from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Employee:
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: float = 0.0
