import streamlit as st

st.set_page_config(
    page_title="Sheena Marie Cordova | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ───────────────────────────────────────────────────────────────
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] { background:#1A0A1E !important; color:#F9F0F8 !important; }
[data-testid="stSidebar"] { background:#220A28 !important; border-right:1px solid rgba(236,72,153,0.2) !important; }
[data-testid="stSidebar"] * { color:#F0D6F5 !important; }
[data-testid="stSidebarNav"] { display:none !important; }

h1,h2,h3,h4 { font-family:'Cormorant Garamond',serif !important; }
p,li,span,div,label { font-family:'DM Sans',sans-serif !important; }
code,pre { font-family:'Space Mono',monospace !important; }

.stButton > button {
    background:linear-gradient(135deg,#be185d,#9333ea) !important;
    color:#fff !important; border:none !important; border-radius:30px !important;
    font-family:'Space Mono',monospace !important; font-size:0.78rem !important;
    letter-spacing:0.08em !important; padding:0.5rem 1.4rem !important;
}
.stButton > button:hover { transform:translateY(-2px) !important; box-shadow:0 8px 28px rgba(236,72,153,0.5) !important; }

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background:rgba(255,255,255,0.04) !important;
    border:1px solid rgba(236,72,153,0.35) !important;
    color:#F9F0F8 !important; border-radius:4px !important;
    font-family:'DM Sans',sans-serif !important;
}
hr { border-color:rgba(236,72,153,0.18) !important; }

.hero-name {
    font-family:'Cormorant Garamond',serif;
    font-size:clamp(3rem,7vw,6rem); font-weight:300; line-height:1.05;
    background:linear-gradient(135deg,#fce7f3 20%,#f472b6 55%,#a855f7);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:0;
}
.hero-role { font-family:'Space Mono',monospace; font-size:0.85rem; color:#ec4899; letter-spacing:0.18em; text-transform:uppercase; }
.hero-sub { font-family:'DM Sans',sans-serif; font-size:1.05rem; color:#d8b4d8; max-width:540px; line-height:1.7; margin-top:1rem; }
.tag { display:inline-block; background:rgba(236,72,153,0.12); border:1px solid rgba(236,72,153,0.3);
    color:#f9a8d4; font-family:'Space Mono',monospace; font-size:0.72rem;
    padding:0.25rem 0.7rem; border-radius:20px; margin:0.2rem; letter-spacing:0.06em; }
.accent-line { width:60px; height:2px; background:linear-gradient(90deg,#ec4899,#a855f7,transparent); margin:1.2rem 0; }
.section-title { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:300; color:#F0ECF8; margin-bottom:0.2rem; }

.nav-link {
    display:block; padding:0.55rem 1rem; margin:0.2rem 0;
    border-radius:8px; text-decoration:none;
    font-family:'Space Mono',monospace; font-size:0.78rem;
    color:#D4C8F0 !important; letter-spacing:0.06em;
    transition:background 0.2s;
}
.nav-link:hover { background:rgba(236,72,153,0.12) !important; color:#f9a8d4 !important; }
</style>
"""

def render_sidebar():
    with st.sidebar:
        st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align:center;padding:1.5rem 0 1rem;'>
            <div style='width:80px;height:80px;border-radius:50%;
                 background:linear-gradient(135deg,#ec4899,#a855f7);
                 margin:0 auto;display:flex;align-items:center;justify-content:center;
                 font-family:Cormorant Garamond,serif;font-size:2rem;color:#fff;'>S</div>
            <div style='font-family:Cormorant Garamond,serif;font-size:1.1rem;
                 margin-top:0.7rem;color:#F0D6F5;'>Sheena Marie</div>
            <div style='font-family:Space Mono,monospace;font-size:0.68rem;
                 color:#ec4899;letter-spacing:0.12em;'>BSCS · DEBESMSCAT</div>
        </div>
        <hr style='border-color:rgba(236,72,153,0.18);margin:0.5rem 0 1rem;'>
        """, unsafe_allow_html=True)

        pages = [
            ("🏠", "Home", "home"),
            ("👤", "About Me", "about"),
            ("🏆", "Certificates", "certificates"),
            ("✉️", "Contact", "contact"),
        ]
        current = st.session_state.get("page", "home")
        for icon, label, key in pages:
            active_style = "background:rgba(236,72,153,0.15);color:#f9a8d4 !important;" if current == key else ""
            if st.button(f"{icon}  {label}", key=f"nav_{key}", use_container_width=True):
                st.session_state["page"] = key
                st.rerun()


def page_home():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    col_hero, col_photo = st.columns([2, 1], gap="large")

    with col_hero:
        st.markdown("""
        <p class='hero-role'>✦ Sheena Marie Cordova</p>
        <h1 class='hero-name'>Hi I'm<br>Sheena!</h1>
        <div class='accent-line'></div>
        <p class='hero-sub'>
            Aspiring software developer and problem-solver from
            <strong style='color:#f9a8d4'>DEBESMSCAT, Masbate</strong>.
            Passionate about building meaningful digital experiences, exploring algorithms,
            and turning ideas into elegant code.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top:1.2rem'>
            <span class='tag'>Python</span><span class='tag'>Web Dev</span>
            <span class='tag'>Data Structures</span><span class='tag'>UI/UX</span>
            <span class='tag'>Problem Solving</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✉️ Get In Touch"):
            st.session_state["page"] = "contact"
            st.rerun()

    with col_photo:
        try:
            st.image("sheena.png", width=230)
        except Exception:
            st.markdown("""
            <div style='width:230px;height:230px;border-radius:50%;
                 background:linear-gradient(135deg,#ec4899,#a855f7);
                 display:flex;align-items:center;justify-content:center;
                 font-family:Cormorant Garamond,serif;font-size:5rem;color:#fff;
                 margin:1.5rem auto 0;'>S</div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align:center;margin-top:1rem;'>
            <div style='font-family:Cormorant Garamond,serif;font-size:1.15rem;color:#F0D6F5;'>Sheena Marie Cordova</div>
            <div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#ec4899;letter-spacing:0.12em;margin-top:0.3rem;'>BSCS · 3RD YEAR · DEBESMSCAT</div>
        </div>
        """, unsafe_allow_html=True)

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
            <div style='background:rgba(236,72,153,0.06);border:1px solid rgba(236,72,153,0.2);
                 border-radius:12px;padding:1.5rem;height:100%;'>
                <div style='font-size:2rem;margin-bottom:0.7rem;'>{icon}</div>
                <div style='font-family:Cormorant Garamond,serif;font-size:1.3rem;color:#F9F0F8;margin-bottom:0.5rem;'>{title}</div>
                <div style='font-family:DM Sans,sans-serif;font-size:0.88rem;color:#c084a8;line-height:1.65;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;padding:2rem;
         border-top:1px solid rgba(236,72,153,0.15);border-bottom:1px solid rgba(168,85,247,0.15);
         background:linear-gradient(135deg,rgba(236,72,153,0.04),rgba(168,85,247,0.04));border-radius:12px;'>
        <span style='font-family:Cormorant Garamond,serif;font-size:1.6rem;font-style:italic;color:#f9a8d4;'>
            "Code is not just syntax — it is a language of possibilities."
        </span><br>
        <span style='font-family:Space Mono,monospace;font-size:0.7rem;color:#8B4A7A;letter-spacing:0.12em;text-transform:uppercase;margin-top:0.5rem;display:inline-block;'>
            — Sheena Marie Cordova
        </span>
    </div>
    """, unsafe_allow_html=True)


def page_about():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .info-label { font-family:'Space Mono',monospace !important; font-size:0.68rem; color:#7C3AED; letter-spacing:0.12em; text-transform:uppercase; }
    .info-val { font-family:'DM Sans',sans-serif !important; font-size:1rem; color:#E0D9F0; margin-top:0.15rem; margin-bottom:1rem; }
    .timeline-item { border-left:2px solid rgba(124,58,237,0.4); padding-left:1.2rem; margin-bottom:1.5rem; position:relative; }
    .timeline-item::before { content:'✦'; position:absolute; left:-0.58rem; color:#7C3AED; font-size:0.75rem; top:0.1rem; background:#0F0A1E; }
    .tl-year { font-family:'Space Mono',monospace; font-size:0.7rem; color:#7C3AED; letter-spacing:0.1em; }
    .tl-title { font-family:'Cormorant Garamond',serif; font-size:1.2rem; color:#E0D9F0; }
    .tl-desc { font-family:'DM Sans',sans-serif; font-size:0.88rem; color:#9B8CC4; line-height:1.6; margin-top:0.2rem; }
    .interest-chip { display:inline-block; background:rgba(124,58,237,0.12); border:1px solid rgba(124,58,237,0.3);
        color:#C4B5FD; font-family:'Space Mono',monospace; font-size:0.72rem; padding:0.3rem 0.8rem; border-radius:20px; margin:0.2rem; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#7C3AED;letter-spacing:0.15em;'>✦ ABOUT ME</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title' style='font-size:2.4rem;'>The Person Behind the Code</p>", unsafe_allow_html=True)
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
        interests = ["💻 Coding","📐 UI Design","📚 Reading Tech Blogs","🎮 Game Dev","🎵 Music","📷 Photography","🌊 Beach Walks","🤝 Volunteering"]
        chips = "".join([f"<span class='interest-chip'>{i}</span>" for i in interests])
        st.markdown(f"<div>{chips}</div>", unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div style='background:rgba(124,58,237,0.07);border:1px solid rgba(124,58,237,0.22);border-radius:12px;padding:1.6rem;'>
            <p style='font-family:Cormorant Garamond,serif;font-size:1.3rem;color:#E0D9F0;margin-bottom:1rem;'>Quick Info</p>
        """, unsafe_allow_html=True)
        for label, val in [("Full Name","Sheena Marie Cordova"),("School","DEBESMSCAT, Masbate"),("Program","BS Computer Science"),("Year Level","3rd Year"),("Location","Masbate, Philippines"),("Status","Active Student")]:
            st.markdown(f"<p class='info-label'>{label}</p><p class='info-val'>{val}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color:rgba(124,58,237,0.2);'><br>", unsafe_allow_html=True)
    st.markdown("<p class='section-title' style='font-size:2.4rem;'>Education Timeline</p>", unsafe_allow_html=True)
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    for year, title, desc in [
        ("2022 – Present","BS Computer Science — DEBESMSCAT","Currently in 3rd year, maintaining a strong academic standing with a focus on software development, data structures, and systems analysis."),
        ("2018 – 2022","Senior High School — Humanities and Social Science (HUMSS)","Graduated with honors."),
        ("2014 – 2018","Junior High School — Masbate School of Fisheries","Completed secondary education with emphasis on science and technology."),
    ]:
        st.markdown(f"""
        <div class='timeline-item'>
            <div class='tl-year'>{year}</div>
            <div class='tl-title'>{title}</div>
            <div class='tl-desc'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p class='section-title' style='font-size:2.4rem;'>Core Values</p>", unsafe_allow_html=True)
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    cols = st.columns(4)
    for col, (icon, val, desc) in zip(cols, [
        ("🎯","Purposeful","Every project I build has intent. I ask 'why' before 'how'."),
        ("🔍","Curious","I constantly explore new technologies and seek to understand deeply."),
        ("🤝","Collaborative","I believe the best solutions come from working together."),
        ("✨","Creative","I bring aesthetic sensibility to technical work — because beauty matters."),
    ]):
        with col:
            st.markdown(f"""
            <div style='text-align:center;padding:1.3rem 1rem;background:rgba(124,58,237,0.07);
                 border:1px solid rgba(124,58,237,0.2);border-radius:10px;'>
                <div style='font-size:2rem;'>{icon}</div>
                <div style='font-family:Cormorant Garamond,serif;font-size:1.2rem;color:#E0D9F0;margin:0.5rem 0 0.3rem;'>{val}</div>
                <div style='font-size:0.82rem;color:#8B7AB8;line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)


def page_certificates():
    import base64, os
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .cert-img-wrap { border-radius:12px; overflow:hidden; border:2px solid transparent;
        background:linear-gradient(#1A0A1E,#1A0A1E) padding-box,linear-gradient(135deg,#ec4899,#a855f7) border-box;
        box-shadow:0 4px 32px rgba(236,72,153,0.2); margin-bottom:0.6rem; }
    .cert-label { font-family:'Cormorant Garamond',serif; font-size:1.1rem; color:#F0D6F5; margin-top:0.5rem; }
    .cert-sublabel { font-family:'Space Mono',monospace; font-size:0.65rem; color:#ec4899; letter-spacing:0.08em; margin-top:0.2rem; }
    .cert-date-lbl { font-family:'Space Mono',monospace; font-size:0.62rem; color:#6B4A6A; margin-top:0.25rem; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#ec4899;letter-spacing:0.15em;'>✦ ACHIEVEMENTS</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title' style='font-size:2.4rem;'>Certificates & Awards</p>", unsafe_allow_html=True)
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    def img_to_b64(path):
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        return None

    real_certs = [
        {"img":"cert1.png","title":"Python Essentials 1","org":"Cisco Networking Academy · Python Institute","date":"31 Mar 2026","cert_id":"5674fd09-8e12-4906-9314-2bf1f5e8659c"},
        {"img":"cert2.png","title":"Getting Started with Cisco Packet Tracer","org":"Cisco Networking Academy","date":"26 Mar 2026","cert_id":""},
        {"img":"cert3.jpg","title":"Get Started with SQL Analytics and BI on Databricks","org":"Databricks · Simplilearn SkillUp","date":"31 Mar 2026","cert_id":"10031855"},
    ]

    cols = st.columns(3, gap="large")
    for col, c in zip(cols, real_certs):
        with col:
            b64 = img_to_b64(c["img"])
            if b64:
                st.markdown(f"""
                <div class='cert-img-wrap'>
                    <img src="data:image/png;base64,{b64}" style='width:100%;display:block;border-radius:10px;'/>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='background:rgba(236,72,153,0.06);border:2px dashed rgba(236,72,153,0.3);
                     border-radius:12px;height:190px;display:flex;flex-direction:column;
                     align-items:center;justify-content:center;margin-bottom:0.6rem;gap:0.5rem;'>
                    <span style='font-size:2.5rem;'>📜</span>
                    <span style='font-family:Space Mono,monospace;font-size:0.65rem;color:#6B4A6A;'>Image not found</span>
                </div>""", unsafe_allow_html=True)
            st.markdown(f"<div class='cert-label'>{c['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='cert-sublabel'>{c['org']}</div>", unsafe_allow_html=True)
            if c['date']:
                st.markdown(f"<div class='cert-date-lbl'>📅 {c['date']}</div>", unsafe_allow_html=True)
            if c['cert_id']:
                st.markdown(f"<div style='font-family:Space Mono,monospace;font-size:0.58rem;color:#4A3A6A;margin-top:0.2rem;word-break:break-all;'>ID: {c['cert_id']}</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)


def page_contact():
    import re
    from datetime import datetime
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .contact-info-card { background:rgba(124,58,237,0.07); border:1px solid rgba(124,58,237,0.22);
        border-radius:12px; padding:1.4rem; margin-bottom:1rem; display:flex; gap:0.8rem; align-items:center; }
    label { font-family:'DM Sans',sans-serif !important; color:#C8BFDF !important; font-size:0.9rem !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#7C3AED;letter-spacing:0.15em;'>✦ CONTACT</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title' style='font-size:2.4rem;'>Let's Connect</p>", unsafe_allow_html=True)
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9B8CC4;font-size:1rem;max-width:600px;line-height:1.7;'>Whether you have a project idea, collaboration opportunity, or just want to say hi — I'd love to hear from you.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_form, col_info = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown("<p style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#E0D9F0;margin-bottom:1rem;'>Send a Message</p>", unsafe_allow_html=True)
        name = st.text_input("Your Name *", placeholder="e.g. Sheena Cordova")
        email = st.text_input("Your Email *", placeholder="e.g. sheena@email.com")
        subject = st.selectbox("Subject *", ["-- Select a subject --","Project Collaboration","Internship / Job Opportunity","Academic Inquiry","Tech Question","Just Saying Hi! 👋","Other"])
        message = st.text_area("Message *", placeholder="Write your message here...", height=160)
        col_cb, _ = st.columns([2, 1])
        with col_cb:
            consent = st.checkbox("I agree that my message will be stored for response purposes.")
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("📨 Send Message"):
            errors = []
            if not name.strip(): errors.append("Please enter your name.")
            if not email.strip() or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email): errors.append("Please enter a valid email address.")
            if subject == "-- Select a subject --": errors.append("Please select a subject.")
            if not message.strip() or len(message.strip()) < 15: errors.append("Please write a message (at least 15 characters).")
            if not consent: errors.append("Please accept the consent checkbox.")
            if errors:
                for e in errors: st.error(e)
            else:
                st.success(f"✅ **Thank you, {name.split()[0]}!** Your message has been received. I'll get back to you at **{email}** as soon as possible. 💜")
                st.markdown(f"""
                <div style='background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);border-radius:10px;padding:1.2rem;margin-top:0.5rem;'>
                    <p style='font-family:Space Mono,monospace;font-size:0.7rem;color:#7C3AED;'>MESSAGE PREVIEW</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>From:</strong> {name} ({email})</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>Subject:</strong> {subject}</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>Sent:</strong> {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
                    <p style='color:#9B8CC4;font-size:0.85rem;margin-top:0.5rem;border-top:1px solid rgba(124,58,237,0.2);padding-top:0.5rem;'>{message}</p>
                </div>
                """, unsafe_allow_html=True)

    with col_info:
        st.markdown("<p style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#E0D9F0;margin-bottom:1rem;'>Contact Info</p>", unsafe_allow_html=True)
        for icon, label, val in [("📧","Email","sheenacordova7@gmail.com"),("📍","Location","Masbate, Philippines"),("🏫","School","DEBESMSCAT"),("⏰","Response Time","Within 24–48 hours")]:
            st.markdown(f"""
            <div class='contact-info-card'>
                <span style='font-size:1.5rem;'>{icon}</span>
                <div>
                    <div style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7C3AED;letter-spacing:0.1em;text-transform:uppercase;'>{label}</div>
                    <div style='font-family:DM Sans,sans-serif;font-size:0.9rem;color:#E0D9F0;margin-top:0.15rem;'>{val}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><p style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7C3AED;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.7rem;'>Social Links</p>", unsafe_allow_html=True)
        for icon, platform, handle in [("🐙","GitHub","github.com/sheena-cordova"),("🐦","Twitter / X","@sheenacordova"),("📘","Facebook","fb.com/sheena.cordova")]:
            st.markdown(f"""
            <div style='background:rgba(255,255,255,0.02);border:1px solid rgba(124,58,237,0.15);border-radius:8px;padding:0.7rem 1rem;margin-bottom:0.5rem;display:flex;gap:0.6rem;align-items:center;'>
                <span>{icon}</span>
                <div>
                    <span style='font-family:Space Mono,monospace;font-size:0.7rem;color:#7C3AED;'>{platform}</span><br>
                    <span style='font-size:0.82rem;color:#C8BFDF;'>{handle}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color:rgba(124,58,237,0.2);'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;padding:2rem;background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);border-radius:12px;'>
        <div style='font-size:2rem;'>🟢</div>
        <div style='font-family:Cormorant Garamond,serif;font-size:1.6rem;color:#E0D9F0;margin:0.5rem 0;'>Open to Opportunities</div>
        <div style='font-family:DM Sans,sans-serif;font-size:0.92rem;color:#9B8CC4;max-width:500px;margin:0 auto;'>
            I'm currently available for internships, freelance projects, and collaboration. Let's build something great together!
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Router ───────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state["page"] = "home"

render_sidebar()

page = st.session_state["page"]
if page == "home":
    page_home()
elif page == "about":
    page_about()
elif page == "certificates":
    page_certificates()
elif page == "contact":
    page_contact()