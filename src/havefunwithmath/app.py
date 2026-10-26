import base64
import os
import streamlit as st

# Page configuration
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
            background-color: rgba(255, 255, 255, 0.92) !important;
            border-radius: 15px;
            padding: 2.5rem;
            box-shadow: 0 4px 25px rgba(0,0,0,0.3);
            margin-top: 2rem;
            margin-bottom: 2rem;
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


# Apply background image
set_bg_hack("bg.jpg")

# App Header
st.title("Have Fun With Math")
st.markdown(
    "**By Sergio Gounehon / Par Sergio Gounehon**<br>"
    "<span style='color: gray; font-size: 0.9em;'>EXPLORATEUR DE LIVRES"
    " FGA (MAT-2101 à MAT-4272)</span>",
    unsafe_allow_html=True,
)

st.write("")

# Initialize session state for active view
if "selected_module" not in st.session_state:
  st.session_state.selected_module = "MAT-3052"

# Course Buttons Layout
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

# Extra Features Row
q_col1, q_col2 = st.columns(2)
with q_col1:
  if st.button("🧠 MINI-QUIZ ALÉATOIRE", use_container_width=True):
    st.session_state.selected_module = "QUIZ"
with q_col2:
  if st.button("💡 LE SAVIEZ-VOUS ?", use_container_width=True):
    st.session_state.selected_module = "TRIVIA"

st.write("---")

# Dynamic Content Display based on selection
if st.session_state.selected_module == "MAT-3052":
  st.subheader("=== MAT-3052 : Triangles et Métrique ===")
  st.markdown("### 1. Le Théorème de Pythagore")
  st.markdown("- **Formule** : $c^2 = a^2 + b^2$")
  st.markdown(
      "- **Exemple** : Dans un triangle rectangle où $a = 3 \\text{ cm}$ et $b ="
      " 4 \\text{ cm}$ :"
  )
  st.markdown("- $c^2 = 3^2 + 4^2 = 9 + 16 = 25$")
  st.markdown("- $c = \\sqrt{25} = 5 \\text{ cm}$")
  st.markdown("- **Réponse** : L'hypoténuse mesure $5 \\text{ cm}$.")

elif st.session_state.selected_module == "QUIZ":
  st.subheader("🧠 Mini-Quiz Aléatoire")
  st.write("Test your math skills with random FGA questions!")

elif st.session_state.selected_module == "TRIVIA":
  st.subheader("💡 Le Saviez-Vous ?")
  st.write("Discover fascinating mathematical facts!")

else:
  current = st.session_state.selected_module
  st.subheader(f"=== {current} ===")
  st.write(
      f"Content for {current} is loading. Add your lessons, formulas, and"
      " examples here!"
  )