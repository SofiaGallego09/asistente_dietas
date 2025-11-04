# asistente_dietas/models.py

class User:
    def __init__(self, name, age, weight, goal, diet_type, ingredients):
        self.name = name
        self.age = age
        self.weight = weight
        self.goal = goal
        self.diet_type = diet_type
        self.ingredients = ingredients
