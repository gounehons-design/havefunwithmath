import base64
import os
import streamlit as st

st.set_page_config(
    page_title="Have Fun With Math", page_icon="🔢", layout="centered"
)


def set_bg_hack(main_bg):
  root_dir = os.path.dirname(os.path.abspath(__file__))
  bg_path = os.path.join(root_dir, main_bg)

  with open(bg_path, "rb") as f:
    data = base64.b64encode(f.read()).decode()

  st.markdown(
      f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{data}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent !important;
        }}
        
        .block-container {{
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 15px;
            padding: 2.5rem;
            box-shadow: 0 4px 25px rgba(0,0,0,0.3);
            margin-top: 2rem;
            margin-bottom: 2rem;
        }}

        .block-container p, .block-container span:not(.stButton span), .block-container h1, .block-container h2, .block-container h3, .block-container li {{
            color: #1a1a1a !important;
        }}
        
        .stButton button p {{
            color: #ffffff !important;
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


set_bg_hack("bg.jpg")

st.title("Have Fun With Math")
st.markdown(
    "**Par Sergio Gounehon**<br>"
    "<span style='color: #444444; font-size: 0.9em;'>EXPLORATEUR DE LIVRES FGA"
    " (MAT-2101 à MAT-4272)</span>",
    unsafe_allow_html=True,
)

st.write("")

if "selected_module" not in st.session_state:
  st.session_state.selected_module = "MAT-2101"

# Course Buttons Layout (En Français)
col1, col2 = st.columns(2)

with col1:
  if st.button("MAT-2101 (SEC 2 - ALGÈBRE)", use_container_width=True):
    st.session_state.selected_module = "MAT-2101"
  if st.button("MAT-3051 (SEC 3 - ALGÈBRE)", use_container_width=True):
    st.session_state.selected_module = "MAT-3051"
  if st.button("MAT-4151 (SEC 4 - STATISTIQUE)", use_container_width=True):
    st.session_state.selected_module = "MAT-4151"
  if st.button(
      "MAT-4271 (SEC 4 - GÉOMÉTRIE ANALYTIQUE)", use_container_width=True
  ):
    st.session_state.selected_module = "MAT-4271"

with col2:
  if st.button("MAT-2102 (SEC 2 - GÉOMÉTRIE)", use_container_width=True):
    st.session_state.selected_module = "MAT-2102"
  if st.button(
      "MAT-3052 (SEC 3 - TRIANGLES & MÉTRIQUE)", use_container_width=True
  ):
    st.session_state.selected_module = "MAT-3052"
  if st.button("MAT-4152 (SEC 4 - PROBABILITÉS)", use_container_width=True):
    st.session_state.selected_module = "MAT-4152"
  if st.button("MAT-4272 (SEC 4 - OPTIMISATION)", use_container_width=True):
    st.session_state.selected_module = "MAT-4272"

st.write("---")

q_col1, q_col2 = st.columns(2)
with q_col1:
  if st.button("🧠 MINI-QUIZ ALÉATOIRE", use_container_width=True):
    st.session_state.selected_module = "QUIZ"
with q_col2:
  if st.button("💡 LE SAVIEZ-VOUS ?", use_container_width=True):
    st.session_state.selected_module = "TRIVIA"

st.write("---")

# Module Content Display (En Français)
mod = st.session_state.selected_module

if mod == "MAT-2101":
  st.subheader("=== MAT-2101 (SEC 2 - ALGÈBRE) ===")
  st.markdown("### 1. Résolution d'équations de 1er degré")
  st.markdown("- **Exemple** : Résoudre $3x + 5 = 20$")
  st.markdown("- **Démarche** :")
  st.markdown(" - $3x = 20 - 5 \\Rightarrow 3x = 15$")
  st.markdown(" - $x = 15 / 3$")
  st.markdown("- **Réponse** : $x = 5$")

elif mod == "MAT-2102":
  st.subheader("=== MAT-2102 (SEC 2 - GÉOMÉTRIE) ===")
  st.markdown("### 1. Périmètre et Aire des Figures Planes")
  st.markdown(
      "- **Exemple** : Trouver l'aire d'un cercle de rayon $r = 7 \\text{ cm}$."
  )
  st.markdown("- **Formule** : $A = \\pi r^2$")
  st.markdown("- $A = \\pi \\times (7)^2 = 49\\pi \\approx 153.94 \\text{ cm}^2$")

elif mod == "MAT-3051":
  st.subheader("=== MAT-3051 (SEC 3 - ALGÈBRE) ===")
  st.markdown("### 1. Systèmes d'équations linéaires")
  st.markdown("- **Exemple** : Résoudre par substitution ou comparaison.")
  st.markdown(" - $y = 2x + 1$")
  st.markdown(" - $y = x + 4$")
  st.markdown("- **Solution** : $2x + 1 = x + 4 \\Rightarrow x = 3$, donc $y = 7$.")

elif mod == "MAT-3052":
  st.subheader("=== MAT-3052 (SEC 3 - TRIANGLES & MÉTRIQUE) ===")
  st.markdown("### 1. Le Théorème de Pythagore")
  st.markdown("- **Formule** : $c^2 = a^2 + b^2$")
  st.markdown(
      "- **Exemple** : Dans un triangle rectangle où $a = 3 \\text{ cm}$ et $b ="
      " 4 \\text{ cm}$ :"
  )
  st.markdown("- $c^2 = 3^2 + 4^2 = 9 + 16 = 25$")
  st.markdown("- $c = \\sqrt{25} = 5 \\text{ cm}$")
  st.markdown("- **Réponse** : L'hypoténuse mesure $5 \\text{ cm}$.")

elif mod == "MAT-4151":
  st.subheader("=== MAT-4151 (SEC 4 - STATISTIQUE) ===")
  st.markdown("### 1. Mesures de tendance centrale")
  st.markdown(
      "- **Exemple** : Calculer la moyenne de la série : $10, 12, 14, 15, 19$"
  )
  st.markdown("- $\\text{Moyenne} = (10 + 12 + 14 + 15 + 19) / 5 = 70 / 5 = 14$")

elif mod == "MAT-4152":
  st.subheader("=== MAT-4152 (SEC 4 - PROBABILITÉS) ===")
  st.markdown("### 1. Probabilité d'un événement")
  st.markdown(
      "- **Exemple** : Tirer une carte rouge dans un jeu standard de 52 cartes."
  )
  st.markdown("- $\\text{P} = 26 / 52 = 1 / 2 = 50\\%$")

elif mod == "MAT-4271":
  st.subheader("=== MAT-4271 (SEC 4 - GÉOMÉTRIE ANALYTIQUE) ===")
  st.markdown("### 1. La Pente d'une Droite")
  st.markdown(
      "- **Formule** : $m = \\frac{y_2 - y_1}{x_2 - x_1}$"
  )
  st.markdown(
      "- **Exemple** : Entre les points $(1, 2)$ et $(3, 8)$ :"
  )
  st.markdown("- $m = \\frac{8 - 2}{3 - 1} = \\frac{6}{2} = 3$")

elif mod == "MAT-4272":
  st.subheader("=== MAT-4272 (SEC 4 - OPTIMISATION) ===")
  st.markdown("### 1. Programmation Linéaire")
  st.markdown(
      "- **Principe** : Maximiser ou minimiser une fonction objectif sous"
      " contraintes."
  )
  st.markdown(
      "- Évaluer les sommets du polygone des contraintes pour trouver"
      " l'optimisation."
  )

elif mod == "QUIZ":
  st.subheader("🧠 Mini-Quiz Aléatoire")
  st.write("Testez vos compétences en mathématiques avec des questions FGA !")

elif mod == "TRIVIA":
  st.subheader("💡 Le Saviez-Vous ?")
  st.write("Découvrez des faits mathématiques fascinants !")