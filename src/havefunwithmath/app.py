import base64
import os
import streamlit as st


def set_bg_hack(main_bg):
  root_dir = os.path.dirname(os.path.abspath(__file__))
  bg_path = os.path.join(root_dir, main_bg)

  with open(bg_path, "rb") as f:
    data = base64.b64encode(f.read()).decode()

  st.markdown(
      f"""
        <style>
        /* Force full-screen background via fixed container overlay */
        .fixed-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("data:image/jpeg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            z-index: -999;
        }}
        
        /* Make Streamlit background transparent */
        .stApp {{
            background: transparent !important;
        }}
        
        [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent !important;
        }}
        
        /* Style your central content card */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.90) !important;
            border-radius: 15px;
            padding: 2.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);
            margin-top: 2rem;
        }}
        </style>
        
        <div class="fixed-bg"></div>
        """,
      unsafe_allow_html=True,
  )


set_bg_hack("bg.jpg")