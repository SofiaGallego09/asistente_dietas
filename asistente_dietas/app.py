from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Cargar las recetas
with open("recipes.json", "r", encoding="utf-8") as f:
    RECIPES = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    name = request.form["name"]
    weight = float(request.form["weight"])
    goal = request.form["goal"]
    ingredients = [i.strip().lower() for i in request.form["ingredients"].split(",")]

    # Determinar tipo de dieta según el objetivo
    if goal == "bajar":
        diet_type = "balanceada"
    elif goal == "subir":
        diet_type = "alta_proteina"
    else:
        diet_type = "vegetariana"

    possible_recipes = []

    # Buscar recetas en TODAS las dietas
    for tipo, lista in RECIPES.items():
        for recipe in lista:
            ingredientes_receta = [i.lower() for i in recipe["ingredientes"]]
            if any(i in ingredientes_receta for i in ingredients):
                possible_recipes.append(recipe)

    # Si no hay coincidencias, sugerir recetas del tipo de dieta
    if not possible_recipes:
        possible_recipes = RECIPES.get(diet_type, [])[:2]

    return render_template(
        "resultados.html",
        name=name,
        weight=weight,
        goal=goal,
        recipes=possible_recipes,
        user_ingredients=ingredients,
        diet_type=diet_type
    )

if __name__ == "__main__":
    app.run(debug=True)
