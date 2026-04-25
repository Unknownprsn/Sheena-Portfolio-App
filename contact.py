import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="Contact | Sheena Marie Cordova", page_icon="✉️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [data-testid="stAppViewContainer"] { background:#0F0A1E !important; color:#F0ECF8 !important; }
[data-testid="stSidebar"] { background:#13092A !important; border-right:1px solid rgba(124,58,237,0.25) !important; }
[data-testid="stSidebar"] * { color:#D4C8F0 !important; }
h1,h2,h3 { font-family:'Cormorant Garamond',serif !important; }
p,li,span,div,label { font-family:'DM Sans',sans-serif !important; }
.section-title { font-family:'Cormorant Garamond',serif; font-size:2.4rem; font-weight:300; color:#F0ECF8; }
.accent-line { width:60px; height:2px; background:linear-gradient(90deg,#7C3AED,transparent); margin:0.8rem 0 1.5rem; }
.contact-info-card { background:rgba(124,58,237,0.07); border:1px solid rgba(124,58,237,0.22);
    border-radius:12px; padding:1.4rem; margin-bottom:1rem; display:flex; gap:0.8rem; align-items:center; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div {
    background:rgba(255,255,255,0.04) !important; border:1px solid rgba(124,58,237,0.4) !important;
    color:#F0ECF8 !important; border-radius:6px !important; font-family:'DM Sans',sans-serif !important; }
.stButton > button { background:linear-gradient(135deg,#7C3AED,#9D5CF5) !important; color:#fff !important;
    border:none !important; border-radius:4px !important; font-family:'Space Mono',monospace !important;
    font-size:0.78rem !important; letter-spacing:0.08em !important; padding:0.55rem 2rem !important; width:100%; }
.stButton > button:hover { transform:translateY(-2px) !important; box-shadow:0 8px 24px rgba(124,58,237,0.45) !important; }
label { font-family:'DM Sans',sans-serif !important; color:#C8BFDF !important; font-size:0.9rem !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:1.5rem 0 1rem;'>
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

st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#7C3AED;letter-spacing:0.15em;'>✦ CONTACT</p>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>Let's Connect</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
st.markdown("<p style='color:#9B8CC4;font-size:1rem;max-width:600px;line-height:1.7;'>Whether you have a project idea, collaboration opportunity, or just want to say hi — I'd love to hear from you. Fill in the form or reach out through any of the channels below.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_form, col_info = st.columns([2, 1], gap="large")

with col_form:
    st.markdown("<p style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#E0D9F0;margin-bottom:1rem;'>Send a Message</p>", unsafe_allow_html=True)

    with st.container():
        name = st.text_input("Your Name *", placeholder="e.g. Sheena Cordova")
        email = st.text_input("Your Email *", placeholder="e.g. sheena@email.com")
        subject = st.selectbox("Subject *", [
            "-- Select a subject --",
            "Project Collaboration",
            "Internship / Job Opportunity",
            "Academic Inquiry",
            "Tech Question",
            "Just Saying Hi! 👋",
            "Other",
        ])
        message = st.text_area("Message *", placeholder="Write your message here...", height=160)

        col_cb, _ = st.columns([2, 1])
        with col_cb:
            consent = st.checkbox("I agree that my message will be stored for response purposes.")

        st.markdown("<br>", unsafe_allow_html=True)
        send = st.button("📨 Send Message")

        if send:
            errors = []
            if not name.strip():
                errors.append("Please enter your name.")
            if not email.strip() or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                errors.append("Please enter a valid email address.")
            if subject == "-- Select a subject --":
                errors.append("Please select a subject.")
            if not message.strip() or len(message.strip()) < 15:
                errors.append("Please write a message (at least 15 characters).")
            if not consent:
                errors.append("Please accept the consent checkbox.")

            if errors:
                for e in errors:
                    st.error(e)
            else:
                st.success(f"""
                ✅ **Thank you, {name.split()[0]}!** Your message has been received.
                I'll get back to you at **{email}** as soon as possible. 💜
                """)
                st.markdown(f"""
                <div style='background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);
                     border-radius:10px;padding:1.2rem;margin-top:0.5rem;'>
                    <p style='font-family:Space Mono,monospace;font-size:0.7rem;color:#7C3AED;'>MESSAGE PREVIEW</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>From:</strong> {name} ({email})</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>Subject:</strong> {subject}</p>
                    <p style='color:#C8BFDF;font-size:0.9rem;'><strong style='color:#E0D9F0;'>Sent:</strong> {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
                    <p style='color:#9B8CC4;font-size:0.85rem;margin-top:0.5rem;border-top:1px solid rgba(124,58,237,0.2);
                         padding-top:0.5rem;'>{message}</p>
                </div>
                """, unsafe_allow_html=True)

with col_info:
    st.markdown("<p style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#E0D9F0;margin-bottom:1rem;'>Contact Info</p>", unsafe_allow_html=True)

    contacts = [
        ("📧", "Email", "sheenacordova7@gmail.com"),
        ("📍", "Location", "Masbate, Philippines"),
        ("🏫", "School", "DEBESMSCAT"),
        ("⏰", "Response Time", "Within 24–48 hours"),
    ]
    for icon, label, val in contacts:
        st.markdown(f"""
        <div class='contact-info-card'>
            <span style='font-size:1.5rem;'>{icon}</span>
            <div>
                <div style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7C3AED;
                     letter-spacing:0.1em;text-transform:uppercase;'>{label}</div>
                <div style='font-family:DM Sans,sans-serif;font-size:0.9rem;color:#E0D9F0;
                     margin-top:0.15rem;'>{val}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7C3AED;
         letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.7rem;'>Social Links</p>
    """, unsafe_allow_html=True)

    socials = [
        ("🐙", "GitHub", "github.com/sheena-cordova"),
        ("🐦", "Twitter / X", "@sheenacordova"),
        ("📘", "Facebook", "fb.com/sheena.cordova"),
    ]
    for icon, platform, handle in socials:
        st.markdown(f"""
        <div style='background:rgba(255,255,255,0.02);border:1px solid rgba(124,58,237,0.15);
             border-radius:8px;padding:0.7rem 1rem;margin-bottom:0.5rem;display:flex;gap:0.6rem;align-items:center;'>
            <span>{icon}</span>
            <div>
                <span style='font-family:Space Mono,monospace;font-size:0.7rem;color:#7C3AED;'>{platform}</span><br>
                <span style='font-size:0.82rem;color:#C8BFDF;'>{handle}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Availability Banner ───────────────────────────────────────────────────────
st.markdown("<br><hr style='border-color:rgba(124,58,237,0.2);'>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;padding:2rem;background:rgba(124,58,237,0.08);
     border:1px solid rgba(124,58,237,0.2);border-radius:12px;'>
    <div style='font-size:2rem;'>🟢</div>
    <div style='font-family:Cormorant Garamond,serif;font-size:1.6rem;color:#E0D9F0;margin:0.5rem 0;'>
        Open to Opportunities
    </div>
    <div style='font-family:DM Sans,sans-serif;font-size:0.92rem;color:#9B8CC4;max-width:500px;margin:0 auto;'>
        I'm currently available for internships, freelance projects, and collaboration.
        Let's build something great together!
    </div>
</div>
""", unsafe_allow_html=True)