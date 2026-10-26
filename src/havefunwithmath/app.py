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