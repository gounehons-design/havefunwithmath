import base64
import streamlit as st


def set_bg_hack(main_bg):
  with open(main_bg, "rb") as f:
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
        
        /* Make content background slightly translucent so the image peaks through */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 12px;
            padding: 2rem;
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


set_bg_hack("bg.jpg")