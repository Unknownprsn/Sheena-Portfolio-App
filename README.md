# ✦ Sheena Marie Cordova — Portfolio Web App

A multipage personal portfolio built with **Streamlit (Python)**, featuring a pink & purple dark aesthetic, real certificate images, and interactive components.

---

## 👩‍💻 About This Project

This is the portfolio web application of **Sheena Marie Cordova**, a 3rd-year **BS Computer Science** student at **Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)**, Masbate, Philippines.

Built as a course requirement demonstrating multipage web application development using the Streamlit framework.

---

## 🗂️ Project Structure

```
portfolio_app/
│
├── Home.py                  # Main entry point — Hero, photo, What I Do
│
├── pages/
│   ├── about.py             # About Me — bio, education timeline, core values
│   ├── certificates.py      # Certificates — 3 real certificate images
│   └── contact.py           # Contact — form with validation, social links
│
├── sheena.jpg               # Profile photo (displayed in hero section)
├── cert1.png                # Python Essentials 1 — Cisco / Python Institute
├── cert2.png                # Getting Started with Cisco Packet Tracer — Cisco
├── cert3.jpg                # SQL Analytics and BI on Databricks — Simplilearn
│
├── .streamlit/
│   └── config.toml          # Theme config (pink & purple dark theme)
│
└── README.md                # This file
```

---

## 📄 Pages

| Page | File | Description |
|---|---|---|
| 🏠 Home | `Home.py` | Hero section with profile photo, skill tags, What I Do cards, quote |
| 👤 About | `pages/about.py` | Bio, Quick Info panel, Education Timeline, Core Values |
| 🏆 Certificates | `pages/certificates.py` | 3 real certificate images with metadata |
| ✉️ Contact | `pages/contact.py` | Contact form with validation, contact info, social links |

---

## ⚡ Features

- **Multipage navigation** via Streamlit sidebar
- **Profile photo** embedded as base64 in a glowing circular frame
- **Real certificate images** displayed with pink-purple gradient borders
- **Interactive contact form** with live validation and message preview
- **Pink & purple dark theme** with custom fonts (Cormorant Garamond, Space Mono, DM Sans)
- **Responsive layout** using Streamlit columns

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install streamlit
```

### 2. Navigate to the project folder

```bash
cd portfolio_app
```

### 3. Run the app

```bash
streamlit run Home.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 📦 Requirements

```
streamlit>=1.30.0
```

Create a `requirements.txt` with:

```bash
echo "streamlit>=1.30.0" > requirements.txt
```

---

## 🎨 Theme Colors

| Role | Color |
|---|---|
| Primary / Accent | `#ec4899` (Hot Pink) |
| Secondary | `#a855f7` (Purple) |
| Background | `#1A0A1E` (Deep Plum) |
| Sidebar | `#220A28` |
| Text | `#F9F0F8` |

---

## 📁 Asset Files

Make sure all image files are in the **same root folder** as `Home.py`:

| File | Purpose |
|---|---|
| `sheena.jpg` | Profile photo in hero section |
| `cert1.png` | Python Essentials 1 certificate |
| `cert2.png` | Cisco Packet Tracer certificate |
| `cert3.jpg` | Databricks SQL Analytics certificate |

---

## ✉️ Contact

**Sheena Marie Cordova**
📧 sheenacordova7@gmail.com
📍 Masbate, Philippines
🏫 DEBESMSCAT — BS Computer Science, 3rd Year

---

*© 2025 Sheena Marie Cordova. All rights reserved.*
