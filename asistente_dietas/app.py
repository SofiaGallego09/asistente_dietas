from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    nombre = request.form['nombre']
    peso = request.form.get("peso")
    edad = request.form['edad']
    ingredientes = request.form['ingredientes']
    objetivo = request.form['objetivo']

    ingredientes_param = ",".join([ing.strip() for ing in ingredientes.split(",") if ing.strip() != ""])

    # Buscar recetas por ingredientes
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredientes_param}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meals = data.get("meals")

        if meals:
            meal = random.choice(meals)
            meal_id = meal["idMeal"]
            details_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
            details_response = requests.get(details_url)

            if details_response.status_code == 200:
                meal = details_response.json()["meals"][0]
            else:
                meal = None
        else:
            random_response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
            if random_response.status_code == 200:
                meal = random_response.json()["meals"][0]
            else:
                meal = None

        return render_template(
            'resultados.html',
            nombre=nombre,
            edad=edad,
            peso=peso,
            objetivo=objetivo,
            ingredientes=ingredientes,
            meal=meal
        )

    else:
        return f"Error al conectar con TheMealDB (código {response.status_code})."

if __name__ == '__main__':
    app.run(debug=True)
