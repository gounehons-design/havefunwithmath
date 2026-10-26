    return f"""
    <style>
    /* Target the root HTML and body elements */
    html, body, [data-testid="stAppViewContainer"] {{
        background: url("data:image/jpg;base64,{data}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    /* Keep the app container transparent so the background shows through */
    .stApp {{
        background: transparent !important;
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