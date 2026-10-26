import base64


def set_bg_hack(main_bg):
  main_bg_ext = "jpg"
  return f"""
    <style>
    .stApp {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    /* Make main content containers transparent so the background shows through */
    [data-testid="stVerticalBlock"] > div {{
        background-color: rgba(255, 255, 255, 0.85); /* Optional: semi-transparent white box for readability */
        padding: 20px;
        border-radius: 10px;
    }}
    </style>
    """


st.markdown(set_bg_hack("static/bg.jpg"), unsafe_allow_html=True)