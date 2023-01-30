from enum import Enum, auto


class Status(Enum):
    New = auto()
    Quoted = auto()
    Accepted = auto()
    Active = auto()
    Archived = auto()
  