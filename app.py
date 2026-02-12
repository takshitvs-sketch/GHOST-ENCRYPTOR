import streamlit as st
from stegano import lsb
from PIL import Image
import io
import time

# --- 1. SUPER HIGH-DOPAMINE UI CONFIG ---
st.set_page_config(page_title="GHOST-ENCRYPTOR | TAKX", page_icon="👻", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle, #0d1117 0%, #000000 100%);
    }

    /* MASSIVE GHOST ENCRYPTOR TITLE */
    .hero-text {
        font-family: 'Orbitron', sans-serif;
        color: #ffffff;
        font-size: 150px; /* MAXIMUM SIZE */
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 0px;
        line-height: 0.9;
        letter-spacing: 15px;
        text-shadow: 0 0 30px #39FF14, 0 0 60px #39FF14;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.01); }
        100% { opacity: 1; transform: scale(1); }
    }

    .sub-hero {
        font-family: 'Share Tech Mono', monospace;
        color: #39FF14;
        text-align: center;
        font-size: 30px;
        letter-spacing: 10px;
        margin-top: 10px;
        font-weight: bold;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 40px;
        justify-content: center;
        padding-top: 30px;
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Share Tech Mono', monospace;
        font-size: 24px;
        color: #444;
    }

    .stTabs [aria-selected="true"] {
        color: #39FF14 !important;
        border-bottom: 5px solid #39FF14 !important;
    }

    /* Simple Team List */
    .team-name {
        color: white;
        font-family: 'Share Tech Mono', monospace;
        font-size: 22px;
        text-align: center;
        padding: 10px;
        border: 1px solid #222;
        border-radius: 5px;
    }

    /* Big Green Button */
    .stButton>button {
        background: #39FF14 !important;
        color: black !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900 !important;
        font-size: 25px !important;
        height: 80px;
        border-radius: 10px;
        box-shadow: 0 0 40px rgba(57, 255, 20, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE BIG HEADER ---
st.markdown('<p class="hero-text">GHOST<br>ENCRYPTOR</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-hero">BY TAKX FUTURE</p>', unsafe_allow_html=True)

# --- 3. THE TABS ---
tab1, tab2, tab3 = st.tabs(["🔒 ENCODE", "🔓 DECODE", "👥 TEAM"])

# --- ENCODE ---
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h3 style='color:#39FF14'>// SELECT IMAGE</h3>", unsafe_allow_html=True)
        file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="u1")
    with c2:
        st.markdown("<h3 style='color:#39FF14'>// SECRET MSG</h3>", unsafe_allow_html=True)
        msg = st.text_area("", placeholder="Message to hide...", height=150)
    
    if file and msg:
        if st.button("RUN GHOST ENCRYPTION"):
            with st.status("Injecting Signal...", expanded=True):
                time.sleep(1)
                img = Image.open(file)
                encoded = lsb.hide(img, msg)
            st.image(encoded, caption="RESULT", width=600)
            buf = io.BytesIO()
            encoded.save(buf, format="PNG")
            st.download_button("💾 DOWNLOAD PNG", buf.getvalue(), "ghost.png")

# --- DECODE ---
with tab2:
    st.markdown("<br><h2 style='color:#39FF14; text-align:center;'>// SPECTRE SCANNER ACTIVE</h2>", unsafe_allow_html=True)
    dec_file = st.file_uploader("", type=["png"], key="u2")
    if dec_file:
        if st.button("EXTRACT SIGNAL"):
            try:
                secret = lsb.reveal(Image.open(dec_file))
                if secret:
                    st.balloons()
                    st.success(f"RECOVERED: {secret}")
                else:
                    st.error("NO SIGNAL DETECTED.")
            except:
                st.error("SCAN FAILED.")

# --- TEAM ---
with tab3:
    st.markdown("<br><h2 style='color:#39FF14; text-align:center;'>PROJECT DEVELOPERS</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    t1, t2, t3, t4 = st.columns(4)
    with t1: st.markdown("<div class='team-name'>Takshit</div>", unsafe_allow_html=True)
    with t2: st.markdown("<div class='team-name'>Sriram Ponnivalavan</div>", unsafe_allow_html=True)
    with t3: st.markdown("<div class='team-name'>Sudharsan</div>", unsafe_allow_html=True)
    with t4: st.markdown("<div class='team-name'>Surya</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><p style='text-align: center; color: #111;'>UNDERGROUNDER ALPHA_v2</p>", unsafe_allow_html=True)
