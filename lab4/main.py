from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    email: str
    age: int = 0
    role: str = "user"
