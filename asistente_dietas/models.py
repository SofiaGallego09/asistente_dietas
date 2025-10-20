from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    weight: float
    goal: str
    diet_type: str
    ingredients: list
