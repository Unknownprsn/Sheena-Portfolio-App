import streamlit as st
import base64, os

st.set_page_config(page_title="Certificates | Sheena Marie Cordova", page_icon="🏆", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [data-testid="stAppViewContainer"] { background:#1A0A1E !important; color:#F9F0F8 !important; }
[data-testid="stSidebar"] { background:#220A28 !important; border-right:1px solid rgba(236,72,153,0.2) !important; }
[data-testid="stSidebar"] * { color:#F0D6F5 !important; }
h1,h2,h3 { font-family:'Cormorant Garamond',serif !important; }
p,li,span,div,label { font-family:'DM Sans',sans-serif !important; }
.section-title { font-family:'Cormorant Garamond',serif; font-size:2.4rem; font-weight:300; color:#F9F0F8; }
.accent-line { width:60px; height:2px; background:linear-gradient(90deg,#ec4899,#a855f7,transparent); margin:0.8rem 0 1.5rem; }
.cert-img-wrap {
    border-radius:12px; overflow:hidden;
    border:2px solid transparent;
    background: linear-gradient(#1A0A1E,#1A0A1E) padding-box,
                linear-gradient(135deg,#ec4899,#a855f7) border-box;
    box-shadow: 0 4px 32px rgba(236,72,153,0.2), 0 2px 12px rgba(168,85,247,0.15);
    margin-bottom:0.6rem;
}
.cert-label { font-family:'Cormorant Garamond',serif; font-size:1.1rem; color:#F0D6F5; margin-top:0.5rem; }
.cert-sublabel { font-family:'Space Mono',monospace; font-size:0.65rem; color:#ec4899; letter-spacing:0.08em; margin-top:0.2rem; }
.cert-date-lbl { font-family:'Space Mono',monospace; font-size:0.62rem; color:#6B4A6A; margin-top:0.25rem; }
.placeholder-card { background:rgba(236,72,153,0.06); border:1px solid rgba(236,72,153,0.2); border-radius:12px; padding:1.5rem; margin-bottom:1rem; }
.award-card { background:linear-gradient(135deg,rgba(236,72,153,0.1),rgba(168,85,247,0.05)); border:1px solid rgba(236,72,153,0.22); border-radius:14px; padding:1.4rem; text-align:center; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:1.5rem 0 1rem;'>
        <div style='width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#ec4899,#a855f7);
             margin:0 auto;display:flex;align-items:center;justify-content:center;
             font-family:Cormorant Garamond,serif;font-size:2rem;color:#fff;'>S</div>
        <div style='font-family:Cormorant Garamond,serif;font-size:1.1rem;margin-top:0.7rem;color:#F0D6F5;'>Sheena Marie</div>
        <div style='font-family:Space Mono,monospace;font-size:0.68rem;color:#ec4899;letter-spacing:0.12em;'>BSCS · DEBESMSCAT</div>
    </div><hr style='border-color:rgba(236,72,153,0.18);'>""", unsafe_allow_html=True)
    st.page_link("home.py", label="🏠  Home")
    st.page_link("pages/about.py", label="👤  About Me")
    st.page_link("pages/certificates.py", label="🏆  Certificates")
    st.page_link("pages/contact.py", label="✉️  Contact")

st.markdown("<p style='font-family:Space Mono,monospace;font-size:0.75rem;color:#ec4899;letter-spacing:0.15em;'>✦ ACHIEVEMENTS</p>", unsafe_allow_html=True)
st.markdown("<p class='section-title'>Certificates & Awards</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

def img_to_b64(path):
    if path and os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

st.markdown("<p style='font-family:Cormorant Garamond,serif;font-size:1.6rem;color:#F9F0F8;margin-bottom:0.3rem;'>🏅 My Certificates</p>", unsafe_allow_html=True)
st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

real_certs = [
    {
        "img":     "cert1.png",
        "title":   "Python Essentials 1",
        "org":     "Cisco Networking Academy · Python Institute",
        "date":    "31 Mar 2026",
        "cert_id": "5674fd09-8e12-4906-9314-2bf1f5e8659c",
    },
    {
        "img":     "cert2.png",
        "title":   "Getting Started with Cisco Packet Tracer",
        "org":     "Cisco Networking Academy",
        "date":    "26 Mar 2026",
        "cert_id": "",
    },
    {
        "img":     "cert3.jpg",
        "title":   "Get Started with SQL Analytics and BI on Databricks",
        "org":     "Databricks · Simplilearn SkillUp",
        "date":    "31 Mar 2026",
        "cert_id": "10031855",
    },
]

cols = st.columns(3, gap="large")
for col, c in zip(cols, real_certs):
    with col:
        b64 = img_to_b64(c["img"])
        if b64:
            ext = c["img"].rsplit(".", 1)[-1].lower()
            mime = "image/jpeg" if ext in ("jpg", "jpeg") else "image/png"
            st.markdown(f"""
            <div class='cert-img-wrap'>
                <img src="data:image/png;base64,{b64}" style='width:100%;display:block;border-radius:10px;'/>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background:rgba(236,72,153,0.06);border:2px dashed rgba(236,72,153,0.3);
                 border-radius:12px;height:190px;display:flex;flex-direction:column;align-items:center;
                 justify-content:center;margin-bottom:0.6rem;gap:0.5rem;'>
                <span style='font-size:2.5rem;'>📜</span>
                <span style='font-family:Space Mono,monospace;font-size:0.65rem;color:#6B4A6A;'>Coming soon</span>
            </div>""", unsafe_allow_html=True)

        st.markdown(f"<div class='cert-label'>{c['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='cert-sublabel'>{c['org']}</div>", unsafe_allow_html=True)
        if c['date']:
            st.markdown(f"<div class='cert-date-lbl'>📅 {c['date']}</div>", unsafe_allow_html=True)
        if c['cert_id']:
            st.markdown(f"<div style='font-family:Space Mono,monospace;font-size:0.58rem;color:#4A3A6A;margin-top:0.2rem;word-break:break-all;'>ID: {c['cert_id']}</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)