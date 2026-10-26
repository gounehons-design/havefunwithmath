from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

courses = {
    "MAT-2101": {
        "title": "MAT-2101 : Algèbre I",
        "content": "1. Les nombres entiers et décimaux\n• Opérations de base (+, -, *, /)\n• Priorité des opérations (PEMDAS)\n2. Introduction aux expressions algébriques",
    },
    "MAT-2102": {
        "title": "MAT-2102 : Géométrie I",
        "content": (
            "1. Les figures planes\n• Périmètre et aire\n2. Les angles\n•"
            " Types d'angles et mesure en degrés"
        ),
    },
    "MAT-3051": {
        "title": "MAT-3051 : Algèbre II",
        "content": (
            "1. Résolution d'équations de 1er degré\n• Isoler x\n2. Systèmes"
            " d'équations simples"
        ),
    },
    "MAT-3052": {
        "title": "MAT-3052 : Triangles et Métrique",
        "content": (
            "1. Le Théorème de Pythagore\n• Formule : c² = a² + b²\n• Exemple :"
            " a=3, b=4 -> c=5 cm"
        ),
    },
    "MAT-4151": {
        "title": "MAT-4151 : Statistiques",
        "content": (
            "1. Analyse de données\n• Moyenne, médiane, mode\n2. Représentation"
            " graphique"
        ),
    },
    "MAT-4152": {
        "title": "MAT-4152 : Probabilités",
        "content": (
            "1. Calcul de probabilités\n• Arbres de probabilité\n2."
            " Dénombrement"
        ),
    },
    "MAT-4271": {
        "title": "MAT-4271 : Géométrie Analytique",
        "content": (
            "1. Le plan cartésien\n• Coordonnées (x, y)\n2. La droite (y = mx +"
            " b)"
        ),
    },
    "MAT-4272": {
        "title": "MAT-4272 : Optimisation",
        "content": (
            "1. Systèmes d'inéquations\n• Polygone de contraintes\n2."
            " Optimisation"
        ),
    },
}

trivia_list = [
    (
        "Le saviez-vous ?",
        "Le zéro (0) a été inventé indépendamment par les Mayas et les"
        " mathématiciens indiens !",
    ),
    (
        "Le saviez-vous ?",
        "Le nombre Pi (π) possède plus de 100 trillions de chiffres décimaux"
        " connus.",
    ),
]

quiz_bank = [
    ("Quel est le résultat de 7 x 8 ?", "56", "Indice : Un peu moins de 60."),
    (
        "Dans un triangle rectangle, si a=3 et b=4, quelle est l'hypoténuse"
        " (Pythagore)?",
        "5",
        "Indice : 3² + 4² = 25.",
    ),
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Have Fun With Math</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f9; color: #333; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .container { max-width: 600px; width: 100%; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { font-size: 1.4rem; color: #1e293b; margin-bottom: 5px; }
        .author { font-size: 0.9rem; font-weight: bold; color: #2563eb; margin-bottom: 20px; }
        .btn-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 15px; }
        .course-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-bottom: 20px; }
        button, .btn { background: #2563eb; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; text-align: center; text-decoration: none; font-size: 0.9rem; transition: background 0.2s; }
        button:hover, .btn:hover { background: #1d4ed8; }
        .course-btn { background: #334155; }
        .course-btn:hover { background: #1e293b; }
        .card { background: #f8fafc; border-left: 4px solid #2563eb; padding: 15px; border-radius: 6px; margin-top: 20px; white-space: pre-line; line-height: 1.5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>EXPLORATEUR DE LIVRES FGA</h1>
        <div class="author">By Sergio Gounehon / Par Sergio Gounehon</div>
        
        <div class="btn-grid">
            <form method="POST" style="margin:0;"><button name="action" value="quiz" style="width:100%;">🧠 MINI-QUIZ</button></form>
            <form method="POST" style="margin:0;"><button name="action" value="trivia" style="width:100%;">💡 LE SAVIEZ-VOUS ?</button></form>
        </div>

        <hr style="border:0; border-top:1px solid #e2e8f0; margin: 20px 0;">
        
        <h3 style="font-size: 1rem; color: #475569; margin-bottom: 10px;">📚 Choisissez un module :</h3>
        <div class="course-grid">
            {% for code in courses.keys() %}
            <form method="POST" style="margin:0;">
                <button name="action" value="{{ code }}" class="course-btn" style="width:100%;">{{ code }}</button>
            </form>
            {% endfor %}
        </div>

        {% if message %}
        <div class="card">
            {{ message }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    message = (
        "Sélectionnez un livre FGA ci-dessus ou testez vos connaissances !"
    )
    if request.method == "POST":
        action = request.form.get("action")
        if action == "quiz":
            q, a, hint = random.choice(quiz_bank)
            message = (
                f"🧠 MINI-QUIZ FGA :\n\nQuestion : {q}\n\n💡"
                f" {hint}\n\n🎯 Réponse : {a}"
            )
        elif action == "trivia":
            title, text = random.choice(trivia_list)
            message = f"💡 {title}\n\n{text}"
        elif action in courses:
            c = courses[action]
            message = f"=== {c['title']} ===\n\n{c['content']}"

    return render_template_string(HTML_TEMPLATE, courses=courses, message=message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)