import random
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Have Fun With Math", page_icon="📐", layout="centered"
)

# Author & Title header
st.markdown("**By Sergio Gounehon / Par Sergio Gounehon**")
st.title("EXPLORATEUR DE LIVRES FGA")
st.caption("De MAT-2101 à MAT-4272 — Formation générale des adultes")

# Full course content database (Sec 2 to Sec 4 complete)
courses = {
    "MAT-2101 (SEC 2 - ALGÈBRE)": {
        "title": "MAT-2101 : Algèbre I",
        "content": (
            "1. Les nombres entiers et décimaux\n"
            "• Opérations de base (+, -, *, /)\n"
            "• Priorité des opérations (PEMDAS)\n"
            "2. Introduction aux expressions algébriques\n"
            "• Variables et termes algébriques\n"
            "• Réduction de termes semblables"
        ),
    },
    "MAT-2102 (SEC 2 - GÉOMÉTRIE)": {
        "title": "MAT-2102 : Géométrie I",
        "content": (
            "1. Les figures planes\n"
            "• Périmètre et aire des rectangles, carrés et triangles\n"
            "2. Les angles\n"
            "• Types d'angles (aigu, obtus, droit)\n"
            "• Mesure d'angles en degrés"
        ),
    },
    "MAT-3051 (SEC 3 - ALGÈBRE)": {
        "title": "MAT-3051 : Algèbre II",
        "content": (
            "1. Résolution d'équations de 1er degré\n"
            "• Isoler la variable x\n"
            "• Équations à coefficients fractionnaires\n"
            "2. Systèmes d'équations simples"
        ),
    },
    "MAT-3052 (SEC 3 - TRIANGLES & MÉTRIQUE)": {
        "title": "MAT-3052 : Triangles et Métrique",
        "content": (
            "1. Le Théorème de Pythagore\n"
            "• Formule : c² = a² + b²\n"
            "• Exemple : Dans un triangle rectangle où a = 3 cm et b = 4 cm :\n"
            " - c² = 3² + 4² = 9 + 16 = 25\n"
            " - c = √25 = 5 cm\n"
            "• Réponse : L'hypoténuse mesure 5 cm."
        ),
    },
    "MAT-4151 (SEC 4 - STATISTIQUE)": {
        "title": "MAT-4151 : Statistiques",
        "content": (
            "1. Analyse de données\n"
            "• Moyenne, médiane, mode et étendue\n"
            "2. Représentation graphique\n"
            "• Diagrammes à bandes, diagrammes circulaires"
        ),
    },
    "MAT-4152 (SEC 4 - PROBABILITÉS)": {
        "title": "MAT-4152 : Probabilités",
        "content": (
            "1. Calcul de probabilités\n"
            "• Probabilités théoriques et expérimentales\n"
            "• Arbres de probabilité\n"
            "2. Dénombrement\n"
            "• Permutations, arrangements et combinaisons"
        ),
    },
    "MAT-4271 (SEC 4 - GÉOMÉTRIE ANALYTIQUE)": {
        "title": "MAT-4271 : Géométrie Analytique",
        "content": (
            "1. Le plan cartésien\n"
            "• Coordonnées d'un point (x, y)\n"
            "2. La droite\n"
            "• Pente d'une droite (m = Δy / Δx)\n"
            "• Équation de la droite : y = mx + b"
        ),
    },
    "MAT-4272 (SEC 4 - OPTIMISATION)": {
        "title": "MAT-4272 : Optimisation",
        "content": (
            "1. Systèmes d'inéquations\n"
            "• Représentation graphique d'une inéquation\n"
            "• Polygone de contraintes\n"
            "2. Optimisation\n"
            "• Fonction à optimiser et recherche de la solution optimale"
        ),
    },
}

# Trivia list
trivia_list = [
    (
        "Le saviez-vous ?",
        "Le zéro (0) a été inventé indépendamment par les Mayas et les"
        " mathématiciens indiens !",
    ),
    (
        "Le saviez-vous ?",
        "Le nombre Pi (π) possède plus de 100 trillions de chiffres décimaux"
        " connus à ce jour.",
    ),
    (
        "Le saviez-vous ?",
        "Le triangle de Pascal cache la suite de Fibonacci et les coefficients"
        " binomiaux.",
    ),
]

# Quiz question bank
quiz_bank = [
    ("Quel est le résultat de 7 x 8 ?", "56", "Indice : C'est un peu moins de 60."),
    (
        "Dans un triangle rectangle, si a=3 et b=4, quelle est la longueur de"
        " l'hypoténuse c (Pythagore)?",
        "5",
        "Indice : 3² + 4² = 9 + 16 = 25, puis racine carrée.",
    ),
    (
        "Quelle est la pente (m) de la droite y = 3x - 5 ?",
        "3",
        "Indice : C'est le coefficient qui multiplie x.",
    ),
]

# Session state initialization
if "selected_content" not in st.session_state:
    st.session_state.selected_content = (
        "Sélectionnez un livre ci-dessous ou testez vos connaissances !"
    )

# Interactive Buttons at the top
col1, col2 = st.columns(2)

with col1:
    if st.button("🧠 MINI-QUIZ ALÉATOIRE", use_container_width=True):
        q, a, hint = random.choice(quiz_bank)
        st.session_state.selected_content = (
            f"### 🧠 MINI-QUIZ FGA\n\n**Question :** {q}\n\n💡 {hint}\n\n🎯"
            f" **Réponse :** {a}"
        )

with col2:
    if st.button("💡 LE SAVIEZ-VOUS ?", use_container_width=True):
        title, text = random.choice(trivia_list)
        st.session_state.selected_content = (
            f"### 💡 {title}\n\n{text}"
        )

st.divider()

# Course Selection Buttons
st.subheader("📚 Choisissez un cours :")
for code, data in courses.items():
    if st.button(code, use_container_width=True):
        st.session_state.selected_content = (
            f"### === {data['title']} ===\n\n{data['content']}"
        )

st.divider()

# Display Area
st.markdown("### 📖 Contenu :")
st.info(st.session_state.selected_content)