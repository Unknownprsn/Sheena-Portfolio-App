import streamlit as st

st.set_page_config(page_title="About | Sheena Marie Cordova", page_icon="👤", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [data-testid="stAppViewContainer"] { background:#0F0A1E !important; color:#F0ECF8 !important; }
[data-testid="stSidebar"] { background:#13092A !important; border-right:1px solid rgba(124,58,237,0.25) !important; }
[data-testid="stSidebar"] * { color:#D4C8F0 !important; }
h1,h2,h3,h4 { font-family:'Cormorant Garamond',serif !important; }
p,li,span,div,label { font-family:'DM Sans',sans-serif !important; }
.section-title { font-family:'Cormorant Garamond',serif; font-size:2.4rem; font-weight:300; color:#F0ECF8; }
.accent-line { width:60px; height:2px; background:linear-gradient(90deg,#7C3AED,transparent); margin:0.8rem 0 1.5rem; }
.info-label { font-family:'Space Mono',monospace !important; font-size:0.68rem; color:#7C3AED; letter-spacing:0.12em; text-transform:uppercase; }
.info-val { font-family:'DM Sans',sans-serif !important; font-size:1rem; color:#E0D9F0; margin-top:0.15rem; margin-bottom:1rem; }
.timeline-item { border-left:2px solid rgba(124,58,237,0.4); padding-left:1.2rem; margin-bottom:1.5rem; position:relative; }
.timeline-item::before { content:'✦'; position:absolute; left:-0.58rem; color:#7C3AED; font-size:0.75rem; top:0.1rem; background:#0F0A1E; }
.tl-year { font-family:'Space Mono',monospace; font-size:0.7rem; color:#7C3AED; letter-spacing:0.1em; }
.tl-title { font-family:'Cormorant Garamond',serif; font-size:1.2rem; color:#E0D9F0; }
.tl-desc { font-family:'DM Sans',sans-serif; font-size:0.88rem; color:#9B8CC4; line-height:1.6; margin-top:0.2rem; }
.interest-chip { display:inline-block; background:rgba(124,58,237,0.12); border:1px solid rgba(124,58,237,0.3);
    color:#C4B5FD; font-family:'Space Mono',monospace; font-size:0.72rem; padding:0.3rem 0.8rem;
    border-radius:20px; margin:0.2rem; }
.stButton > button { background:linear-gradient(135deg,#7C3AED,#9D5CF5) !important; color:#fff !important;
    border:none !important; border-radius:4px !important; font-family:'Space Mono',monospace !important;
    font-size:0.78rem !important; letter-spacing:0.08em !important; padding:0.5rem 1.4rem !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:1.5rem 0 1rem;'>
        <div style='width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#7C3AED,#C4B5FD);
             margin:0 auto;display:flex;align-items:center;justify-content:center;
             font-family:Cormorant Garamond,serif;font-size:2rem;color:#fff;'>S</div>
        <div style='font-family:Cormorant Garamond,serif;font-size:1.1rem;margin-top:0.7rem;color:#E0D9F0;'>Sheena Marie</div>
        <div style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7C3AED;letter-spacing:0.12em;'>BSCS · DEBESMSCAT</div>
    </div><hr style='border-color:rgba(124,58,237,0.2);'>""", unsafe_allow_html=True)
    st.page_link("home.py", label="🏠  Home")
    st.page_link("pages/about.py", label="👤  About Me")
    st.page_link("pages/certificates.py", label="🏆  Certificates")
    st.page_link("pages/contact.py", label="✉️  Contact")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#7C3AED;letter-spacing:0.15em;'>✦ ABOUT ME</p>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>The Person Behind the Code</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

col_bio, col_info = st.columns([2, 1], gap="large")

with col_bio:
    st.markdown("""
    <p style='font-family:DM Sans,sans-serif;font-size:1.05rem;color:#C8BFDF;line-height:1.85;'>
        Hi! I'm <strong style='color:#E0D9F0'>Sheena Marie Cordova</strong>, a third-year Bachelor of Science in Computer Science 
        student at <strong style='color:#C4B5FD'>Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology 
        (DEBESMSCAT)</strong> in Masbate, Philippines.
    </p>
    <p style='font-family:DM Sans,sans-serif;font-size:1.05rem;color:#C8BFDF;line-height:1.85;margin-top:1rem;'>
        I discovered my passion for technology early — fascinated by how a few lines of code can create 
        something that touches people's lives. My journey in BSCS has shaped me into a logical thinker 
        and a creative builder who loves the intersection of <strong style='color:#C4B5FD'>design and functionality</strong>.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.72rem;color:#7C3AED;letter-spacing:0.1em;'>INTERESTS & HOBBIES</p>", unsafe_allow_html=True)
    interests = ["💻 Coding", "📐 UI Design", "📚 Reading Tech Blogs", "🎮 Game Dev",
                 "🎵 Music", "📷 Photography", "🌊 Beach Walks", "🤝 Volunteering"]
    chips = "".join([f"<span class='interest-chip'>{i}</span>" for i in interests])
    st.markdown(f"<div>{chips}</div>", unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style='background:rgba(124,58,237,0.07);border:1px solid rgba(124,58,237,0.22);
         border-radius:12px;padding:1.6rem;'>
        <p style='font-family:Cormorant Garamond,serif;font-size:1.3rem;color:#E0D9F0;margin-bottom:1rem;'>
            Quick Info
        </p>
    """, unsafe_allow_html=True)

    info = [
        ("Full Name", "Sheena Marie Cordova"),
        ("School", "DEBESMSCAT, Masbate"),
        ("Program", "BS Computer Science"),
        ("Year Level", "3rd Year"),
        ("Location", "Masbate, Philippines"),
        ("Status", "Active Student"),
    ]
    for label, val in info:
        st.markdown(f"<p class='info-label'>{label}</p><p class='info-val'>{val}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Education Timeline ────────────────────────────────────────────────────────
st.markdown("<br><hr style='border-color:rgba(124,58,237,0.2);'><br>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>Education Timeline</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

timeline = [
    ("2022 – Present", "BS Computer Science — DEBESMSCAT",
     "Currently in 3rd year, maintaining a strong academic standing with a focus on software development, data structures, and systems analysis."),
    ("2018 – 2022", "Senior High School —Humanities and Social Science(HUMSS)",
     "Graduated with honors."),
    ("2014 – 2018", "Junior High School — Masbate School of Fisheries",
     "Completed secondary education with emphasis on science and technology."),
]

for year, title, desc in timeline:
    st.markdown(f"""
    <div class='timeline-item'>
        <div class='tl-year'>{year}</div>
        <div class='tl-title'>{title}</div>
        <div class='tl-desc'>{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>Core Values</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

vals = [
    ("🎯", "Purposeful", "Every project I build has intent. I ask 'why' before 'how'."),
    ("🔍", "Curious", "I constantly explore new technologies and seek to understand deeply."),
    ("🤝", "Collaborative", "I believe the best solutions come from working together."),
    ("✨", "Creative", "I bring aesthetic sensibility to technical work — because beauty matters."),
]
cols = st.columns(4)
for col, (icon, val, desc) in zip(cols, vals):
    with col:
        st.markdown(f"""
        <div style='text-align:center;padding:1.3rem 1rem;background:rgba(124,58,237,0.07);
             border:1px solid rgba(124,58,237,0.2);border-radius:10px;height:100%;'>
            <div style='font-size:2rem;'>{icon}</div>
            <div style='font-family:Cormorant Garamond,serif;font-size:1.2rem;color:#E0D9F0;
                 margin:0.5rem 0 0.3rem;'>{val}</div>
            <div style='font-size:0.82rem;color:#8B7AB8;line-height:1.6;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)