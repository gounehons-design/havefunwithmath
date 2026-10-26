import base64
import os
import streamlit as st


def set_bg_hack(main_bg):
  root_dir = os.path.dirname(os.path.abspath(__file__))
  bg_path = os.path.join(root_dir, main_bg)

  # Read file header to detect exact image format automatically
  with open(bg_path, "rb") as f:
    header = f.read(12)
    f.seek(0)
    data = base64.b64encode(f.read()).decode()

  # Determine correct MIME type from magic bytes
  if header.startswith(b"\xff\xd8\xff"):
    mime_type = "image/jpeg"
  elif header.startswith(b"\x89PNG\r\n\x1a\n"):
    mime_type = "image/png"
  elif header.startswith(b"RIFF") and header[8:12] == b"WEBP":
    mime_type = "image/webp"
  else:
    mime_type = "image/jpeg" # fallback

  st.markdown(
      f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:{mime_type};base64,{data}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent !important;
        }}
        
        .block-container {{
            background-color: rgba(255, 255, 255, 0.90) !important;
            border-radius: 15px;
            padding: 2.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);
            margin-top: 2rem;
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


set_bg_hack("bg.jpg")