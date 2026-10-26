import base64


def set_bg_hack(main_bg):
  main_bg_ext = "jpg"
  with open(main_bg, "rb") as f:
    data = base64.b64encode(f.read()).decode()

  return f"""
    <style>
    .stApp {{
        background-image: url("data:image/{main_bg_ext};base64,{data}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    /* Make the central content box semi-transparent so the background shows through */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85) !important;
        border-radius: 15px;
        padding: 2rem;
    }}
    </style>
    """


st.markdown(set_bg_hack("static/bg.jpg"), unsafe_allow_html=True)