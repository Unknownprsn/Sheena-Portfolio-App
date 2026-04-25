# ✦ Sheena Marie Cordova — Personal Portfolio

A personal portfolio website built with **Streamlit**, showcasing the academic background, certificates, and contact information of Sheena Marie Cordova, a 3rd-year BS Computer Science student at DEBESMSCAT, Masbate, Philippines.

---

## 📸 Preview

The portfolio features a dark, elegant aesthetic with a pink-to-purple gradient palette, serif typography (Cormorant Garamond), and a monospace accent font (Space Mono).

---

## 📁 Project Structure

```
portfolio/
│
├── home.py                  # Main entry point — contains all pages via session-state router
│
├── pages/                   # Standalone page files (alternative multi-page setup)
│   ├── about.py             # About Me page
│   ├── certificates.py      # Certificates & Awards page
│   └── contact.py           # Contact form page
│
├── sheena.png               # Profile photo (place in root directory)
├── cert1.png                # Certificate image 1 — Python Essentials 1
├── cert2.png                # Certificate image 2 — Cisco Packet Tracer
├── cert3.jpg                # Certificate image 3 — Databricks SQL Analytics
│
└── requirements.txt         # Python dependencies
```

---

## 🖥️ Pages

### 🏠 Home
- Hero section with name, role, and short bio
- Skill tags (Python, Web Dev, Data Structures, UI/UX, Problem Solving)
- Profile photo with gradient fallback if image is missing
- Quick-stats bar (Year Level, GWA, Skills, Certificates)
- Featured skills section with visual cards
- "Get In Touch" button navigating to Contact

### 👤 About Me
- Personal bio and background
- Quick Info card (name, school, program, year, location, status)
- Interests & hobbies chips
- Education timeline (College → Senior High → Junior High)
- Core Values section (Purposeful, Curious, Collaborative, Creative)

### 🏆 Certificates & Awards
Displays verified certificates in a 3-column card layout:

| Certificate | Issuer | Date |
|---|---|---|
| Python Essentials 1 | Cisco Networking Academy · Python Institute | Mar 31, 2026 |
| Getting Started with Cisco Packet Tracer | Cisco Networking Academy | Mar 26, 2026 |
| Get Started with SQL Analytics and BI on Databricks | Databricks · Simplilearn SkillUp | Mar 31, 2026 |

Certificate images are loaded from local files and encoded to Base64. A placeholder card is shown if the image file is not found.

### ✉️ Contact
- Contact form with validation (name, email, subject, message, consent checkbox)
- Contact info panel (email, location, school, response time)
- Social links (GitHub, Twitter/X, Facebook)
- "Open to Opportunities" availability banner

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. **Clone or download** the project files into a folder.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your assets** to the project root:
   - `sheena.png` — your profile photo
   - `cert1.png`, `cert2.png`, `cert3.jpg` — certificate images

4. **Run the app:**
   ```bash
   streamlit run home.py
   ```

5. Open your browser and go to `http://localhost:8501`.

---

## ⚙️ How Navigation Works

`home.py` uses a **session-state router** pattern — all four pages (`home`, `about`, `certificates`, `contact`) are defined as functions inside a single file and rendered based on `st.session_state["page"]`. The sidebar buttons update the session state and trigger a `st.rerun()` to switch views.

The `pages/` folder contains standalone versions of each page (for reference or alternative multi-page deployment).

---

## 🎨 Design System

| Element | Value |
|---|---|
| Background | `#1A0A1E` (deep dark purple) |
| Primary Accent | `#ec4899` (pink) |
| Secondary Accent | `#a855f7` (purple) |
| Text Primary | `#F9F0F8` |
| Text Muted | `#9B8CC4` |
| Heading Font | Cormorant Garamond (serif) |
| Body Font | DM Sans (sans-serif) |
| Monospace Font | Space Mono |

---

## 📦 Dependencies

```
streamlit>=1.32.0
```

All other libraries used (`base64`, `os`, `re`, `datetime`) are part of the Python standard library.

---

## 👩‍💻 Author

**Sheena Marie Cordova**
BS Computer Science · 3rd Year
Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)
Masbate, Philippines

- 📧 sheenacordova7@gmail.com
- 🐙 github.com/sheena-cordova
- 📘 fb.com/sheena.cordova
