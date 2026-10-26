import base64
import os
import streamlit as st


def set_bg_hack(main_bg):
  # Construct absolute path relative to this script's location
  root_dir = os.path.dirname(os.path.abspath(__file__))
  bg_path = os.path.join(root_dir, "../../", main_bg)

  with open(bg_path, "rb") as f:
    data = base64.b64encode(f.read()).decode()

  st.markdown(
      f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        .block-container {{
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 12px;
            padding: 2.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


set_bg_hack("bg.jpg")