import base64


def set_bg_hack(main_bg):
  with open(main_bg, "rb") as f:
    data = base64.b64encode(f.read()).decode()

  return f"""
    <style>
    /* Target the main body and app wrapper directly */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background: url("data:image/jpg;base64,{data}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    /* Make the central content container semi-transparent white */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.88) !important;
        border-radius: 15px;
        padding: 2.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    </style>
    """


st.markdown(set_bg_hack("bg.jpg"), unsafe_allow_html=True)