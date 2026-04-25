import streamlit as st

st.set_page_config(
    page_title="Sheena Marie Cordova | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #1A0A1E !important;
    color: #F9F0F8 !important;
}
[data-testid="stSidebar"] {
    background: #220A28 !important;
    border-right: 1px solid rgba(236,72,153,0.2) !important;
}
[data-testid="stSidebar"] * { color: #F0D6F5 !important; }

/* ── Typography ── */
h1,h2,h3,h4 { font-family: 'Cormorant Garamond', serif !important; }
p, li, span, div, label { font-family: 'DM Sans', sans-serif !important; }
code, pre { font-family: 'Space Mono', monospace !important; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #be185d, #9333ea) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 30px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.08em !important;
    padding: 0.5rem 1.4rem !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(236,72,153,0.5) !important;
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(236,72,153,0.35) !important;
    color: #F9F0F8 !important;
    border-radius: 4px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: rgba(236,72,153,0.05) !important;
    border: 2px dashed rgba(236,72,153,0.35) !important;
    border-radius: 12px !important;
    padding: 0.5rem !important;
}

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: rgba(190,24,93,0.08) !important;
    border: 1px solid rgba(236,72,153,0.22) !important;
    border-radius: 8px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2rem !important;
    color: #f472b6 !important;
}

/* ── Divider ── */
hr { border-color: rgba(236,72,153,0.18) !important; }

/* ── Sidebar nav labels ── */
[data-testid="stSidebarNav"] a {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.06em !important;
}

/* ── Hero name ── */
.hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3rem, 7vw, 6rem);
    font-weight: 300;
    line-height: 1.05;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #fce7f3 20%, #f472b6 55%, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.hero-role {
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #ec4899;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    color: #d8b4d8;
    max-width: 540px;
    line-height: 1.7;
    margin-top: 1rem;
}
/* ── Stat bubble ── */
.stat-grid {
    display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 2rem;
}
.stat-card {
    background: rgba(124,58,237,0.1);
    border: 1px solid rgba(124,58,237,0.3);
    border-radius: 10px;
    padding: 1rem 1.4rem;
    min-width: 130px;
    text-align: center;
}
.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    color: #A78BFA;
    line-height: 1;
}
.stat-lbl {
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    color: #8B7AB8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}
/* ── Highlight tag ── */
.tag {
    display: inline-block;
    background: rgba(236,72,153,0.12);
    border: 1px solid rgba(236,72,153,0.3);
    color: #f9a8d4;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    padding: 0.25rem 0.7rem;
    border-radius: 20px;
    margin: 0.2rem;
    letter-spacing: 0.06em;
}
/* ── Decorative line ── */
.accent-line {
    width: 60px; height: 2px;
    background: linear-gradient(90deg, #ec4899, #a855f7, transparent);
    margin: 1.2rem 0;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 300;
    color: #F0ECF8;
    margin-bottom: 0.2rem;
}
</style>
""", unsafe_allow_html=True)

col_hero, col_photo = st.columns([2, 1], gap="large")

with col_hero:
    st.markdown("""
    <p class='hero-role'>✦ Sheena Marie Cordova </p>
    <h1 class='hero-name'>Hi I'm<br>Sheena!</h1>
    <div class='accent-line'></div>
    <p class='hero-sub'>
        Aspiring software developer and problem-solver from <strong style='color:#f9a8d4'>DEBESMSCAT, Masbate</strong>.
        Passionate about building meaningful digital experiences, exploring algorithms,
        and turning ideas into elegant code.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-top:1.2rem'>
        <span class='tag'>Python</span>
        <span class='tag'>Web Dev</span>
        <span class='tag'>Data Structures</span>
        <span class='tag'>UI/UX</span>
        <span class='tag'>Problem Solving</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, = st.columns([1])
    with c1:
        if st.button("✉️ Get In Touch"):
            st.switch_page("pages/contact.py")

# ── Photo Column ──────────────────────────────────────────────────────────────
with col_photo:
    st.markdown("<div style='margin-top:1.5rem; display:flex; flex-direction:column; align-items:center;'>", unsafe_allow_html=True)

    st.image("sheena.png", width=230)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; margin-top:1rem;'>
        <div style='font-family:Cormorant Garamond,serif; font-size:1.15rem;
             color:#F0D6F5; letter-spacing:0.02em;'>Sheena Marie Cordova</div>
        <div style='font-family:Space Mono,monospace; font-size:0.65rem;
             color:#ec4899; letter-spacing:0.12em; margin-top:0.3rem;'>BSCS · 3RD YEAR · DEBESMSCAT</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>What I Do</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
cards = [
    ("🖥️", "Web Development", "Building responsive and visually engaging websites using HTML, CSS, JavaScript, and Python frameworks like Flask and Streamlit."),
    ("🧩", "Algorithm Design", "Solving complex computational problems through data structures, algorithm analysis, and logical thinking cultivated through coursework."),
    ("📊", "Data & Databases", "Designing and querying relational databases, working with SQL, and exploring data analysis using Python libraries."),
]
for col, (icon, title, desc) in zip([c1, c2, c3], cards):
    with col:
        st.markdown(f"""
        <div style='background:rgba(236,72,153,0.06); border:1px solid rgba(236,72,153,0.2);
             border-radius:12px; padding:1.5rem; height:100%;
             box-shadow:0 4px 24px rgba(236,72,153,0.06);'>
            <div style='font-size:2rem; margin-bottom:0.7rem;'>{icon}</div>
            <div style='font-family:Cormorant Garamond,serif; font-size:1.3rem;
                 color:#F9F0F8; margin-bottom:0.5rem;'>{title}</div>
            <div style='font-family:DM Sans,sans-serif; font-size:0.88rem;
                 color:#c084a8; line-height:1.65;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; padding:2rem;
     border-top:1px solid rgba(236,72,153,0.15);
     border-bottom:1px solid rgba(168,85,247,0.15);
     background:linear-gradient(135deg,rgba(236,72,153,0.04),rgba(168,85,247,0.04));
     border-radius:12px;'>
    <span style='font-family:Cormorant Garamond,serif; font-size:1.6rem; font-style:italic;
         color:#f9a8d4; letter-spacing:0.02em;'>
        "Code is not just syntax — it is a language of possibilities."
    </span>
    <br>
    <span style='font-family:Space Mono,monospace; font-size:0.7rem; color:#8B4A7A;
         letter-spacing:0.12em; text-transform:uppercase; margin-top:0.5rem; display:inline-block;'>
        — Sheena Marie Cordova
    </span>
</div>
""", unsafe_allow_html=True)