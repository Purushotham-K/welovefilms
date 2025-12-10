# app.py
# Clean premium wedding website for We Love Films
# Minimal White Background — Inspired by StudioA Style

from pathlib import Path
from datetime import datetime

import streamlit as st
import pandas as pd
from PIL import Image

# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="We Love Films",
    page_icon="📸",
    layout="wide",
)

STATIC_GALLERY_DIR = Path("gallery")
BOOKINGS_CSV = Path("bookings.csv")

# ▶️ Add your real YouTube video URL
YOUTUBE_VIDEO_URL = "https://youtu.be/CwuWjFJU_YQ?si=1iWnnoaRZOiBNY66"

# =========================
# GLOBAL CSS — FULL WHITE BACKGROUND + BLACK TEXT
# =========================

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display...wght@400;700;800&display=swap');


/* FULL PAGE WHITE BACKGROUND */
html, body, .stApp, [data-testid="stAppViewContainer"], 
[data-testid="stSidebar"], .block-container {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* ===================== */
/* Custom header + nav   */
/* ===================== */

.we-header {
    background: #ffffff;
    border-bottom: 1px solid #eee;
    position: sticky;
    top: 0;
    z-index: 999;
}

.we-header-inner {
    max-width: 1100px;
    margin: 0 auto;
    padding: 1.2rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: "Playfair Display", serif;
}

.we-header-brand {
    display: flex;
    align-items: center;
}

.we-logo-box {
    border: 2px solid #000;
    padding: 6px 10px;
    margin-right: 10px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
}

.we-logo-text {
    font-size: 1.1rem;
    letter-spacing: 0.12em;
    line-height: 1.1;
}

.we-header-nav {
    display: flex;
    align-items: center;
}

.we-header-nav a {
    margin-left: 24px;
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    text-decoration: none;
    color: #000000;
}

.we-header-nav a:hover {
    opacity: 0.7;
}

/* Hamburger toggle (hidden on desktop) */
.menu-toggle {
    display: none;
}

.menu-icon {
    display: none;
    cursor: pointer;
    font-size: 1.6rem;
    margin-left: 16px;
}

/* ===================== */
/* Mobile header styles  */
/* ===================== */

@media (max-width: 768px) {
    .we-header-inner {
        padding: 0.8rem 1rem;
    }

    .we-header-nav {
        position: absolute;
        top: 64px;          /* just below header */
        left: 0;
        width: 100%;
        background: #ffffff;
        border-top: 1px solid #eee;
        display: none;
        flex-direction: column;
        padding: 0.75rem 1.25rem 1rem;
    }

    .we-header-nav a {
        margin: 0.45rem 0;
    }

    .menu-icon {
        display: block;
    }

    /* show menu when checkbox is checked */
    #menu-toggle:checked ~ .we-header-nav {
        display: flex;
    }
}

.we-logo-box {
    width: 45px;
    height: 45px;
    border: 2px solid #000;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-weight: 800;
    font-size: 0.9rem;
    background-color: #ffffff;
    color: #000000;
}

.we-logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 800;
    text-transform: uppercase;
    color: #000000;
}



/* Hero Image Style */
.hero-image-frame {
    margin-top: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.10);
    border-radius: 4px;
    overflow: hidden;
}

.hero-caption {
    margin-top: 1rem;
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 600;
    color: #000000;
}

/* Section Wrapper */
.section-wrapper {
    margin-top: 3rem;
    padding: 0 1.5rem;
}

h2, h3, h4 {
    font-family: 'Playfair Display', serif !important;
    color: #000 !important;
}

/* Section Cards */
.section-card {
    background-color: #ffffff;
    border: 1px solid rgba(0,0,0,0.10);
    padding: 1.3rem 1.6rem;
    border-radius: 6px;
    margin-bottom: 1rem;
}

/* Gallery Images */
.gallery-img-wrap {
    margin-bottom: 1rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
    border-radius: 4px;
    overflow: hidden;
}

.gallery-img-wrap img {
    width: 100%;
    height: auto;
    display: block;
}

/* Submit Button */
.stButton>button {
    background-color: #FFFFFF !important;
    color: #fff !important;
    border-radius: 999px !important;
    padding: 0.5rem 1.8rem !important;
    font-weight: 600 !important;
    border: none !important;
}
.stButton>button:hover {
    background-color: #FFFFFF !important;
}

/* Footer */
.footer {
    margin-top: 4rem;
    padding: 1.5rem 0;
    border-top: 1px solid rgba(0,0,0,0.10);
    text-align: center;
    font-size: 0.9rem;
    color: #444;
}

/* ----- FORM FIELDS (BOOK US SECTION) ----- */

/* Labels */
.stTextInput label,
.stTextArea label,
.stDateInput label,
.stSelectbox label {
    color: #222222 !important;
    font-weight: 500 !important;
}

/* Text / email / phone inputs */
.stTextInput input,
.stDateInput input {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 8px !important;
    border: 1px solid #d0d0d0 !important;
}

/* Text area */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 8px !important;
    border: 1px solid #d0d0d0 !important;
}

/* Select (Package Type) */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 8px !important;
    border: 1px solid #d0d0d0 !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #000000 !important;
}

/* ----- SUBMIT BUTTON FIX ----- */

.stButton>button {
    background-color: #FFFFFF !important;      /* elegant black button */
    color: #FFFFFF !important;                 /* white text */
    border-radius: 8px !important;             /* smooth corners */
    padding: 0.45rem 1.4rem !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    border: none !important;
    box-shadow: 0 4px 10px;;
}

.stButton>button:hover {
    background-color: #FFFFFF !important;      /* slightly lighter hover */
    cursor: pointer !important;
}

/* Mobile Responsive Fixes */
@media (max-width: 768px) {

    /* Make hero image fit mobile screen properly */
    .st-emotion-cache-1y4p8pa, .stImage {
        width: 100% !important;
        height: auto !important;
    }

    /* Reduce navbar spacing */
    .we-header-nav a {
        margin-right: 12px !important;
        font-size: 16px !important;
    }

    /* Center navbar for mobile */
    .we-header-nav {
        text-align: center !important;
        display: block !important;
    }

    /* Reduce page padding */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }

    /* Make gallery images scale properly */
    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* Fix hero text overlay positioning */
    .hero-text {
        font-size: 1.2rem !important;
        bottom: 20px !important;
    }
}


</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# =========================
# HELPERS
# =========================

def load_static_gallery():
    categories = {}
    if not STATIC_GALLERY_DIR.exists():
        return categories
    for folder in STATIC_GALLERY_DIR.iterdir():
        if folder.is_dir():
            images = []
            for ext in ["*.jpg", "*.jpeg", "*.png", "*.webp"]:
                images.extend(folder.glob(ext))
            if images:
                categories[folder.name.title()] = sorted(images)
    return categories


def append_booking_to_csv(entry: dict):
    df_new = pd.DataFrame([entry])
    if BOOKINGS_CSV.exists():
        df_old = pd.read_csv(BOOKINGS_CSV)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(BOOKINGS_CSV, index=False)


def get_hero_image():
    weddings = STATIC_GALLERY_DIR / "weddings"
    candidates = []
    if weddings.exists():
        for ext in ["*.jpg", "*.jpeg", "*.png", "*.webp"]:
            candidates.extend(sorted(weddings.glob(ext)))
    if not candidates:
        for imgs in load_static_gallery().values():
            if imgs:
                candidates.extend(imgs)
                break
    return candidates[0] if candidates else None

# =========================
# PAGE SECTIONS
# =========================

def top_nav():
    st.markdown("""
<div class="we-header">
    <div class="we-header-inner">
        <div class="we-header-brand">
            <div class="we-logo-box">WLF</div>
            <div class="we-logo-text">WE LOVE FILMS</div>
        </div>

        <input type="checkbox" id="menu-toggle" class="menu-toggle">
        <label for="menu-toggle" class="menu-icon">
            <span></span><span></span><span></span>
        </label>

        <nav class="we-header-nav">
            <a href="#home">Home</a>
            <a href="#gallery">Gallery</a>
            <a href="#films">Films</a>
            <a href="#about">About Us</a>
            <a href="#book">Book Us</a>
            <a href="#contact">Contact</a>
        </nav>
    </div>
</div>
    """, unsafe_allow_html=True)


def section_home():
    st.markdown('<a name="home"></a>', unsafe_allow_html=True)

    hero_img = get_hero_image()
    if hero_img:
        st.markdown('<div class="hero-image-frame">', unsafe_allow_html=True)
        st.image(Image.open(hero_img), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <div class="hero-caption">
        Your wedding is one of the most meaningful chapters of your life.Our team at We Love Films is dedicated to capturing it with precision, beauty, and emotion so you can relive every moment exactly as it was.
        From intimate ceremonies to grand celebrations, we create photographs and films that are timeless, heartfelt, and uniquely yours.
        Book your wedding story with us today.
    </div>
    """,
        unsafe_allow_html=True,
)


def section_gallery():
    st.markdown('<a name="gallery"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.header("Gallery")
    st.write("A curated selection of weddings and celebrations we’ve documented.")

    categories = load_static_gallery()
    if not categories:
        st.info("Add images into /gallery folders to display your portfolio.")
        return

    tabs = st.tabs(list(categories.keys()))

    for tab, (cat, imgs) in zip(tabs, categories.items()):
        with tab:
            cols = st.columns(3)
            for i, img_path in enumerate(imgs):
                col = cols[i % 3]
                with col:
                    st.markdown('<div class="gallery-img-wrap">', unsafe_allow_html=True)
                    st.image(Image.open(img_path), use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def section_films():
    st.markdown('<a name="films"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.header("Wedding Films")
    st.write("A glimpse into our cinematic storytelling style.")

    if "YOUR_VIDEO_ID" not in YOUTUBE_VIDEO_URL:
        st.video(YOUTUBE_VIDEO_URL)
    else:
        st.info("Add your YouTube link in the YOUTUBE_VIDEO_URL variable to show your film here.")

    st.markdown('</div>', unsafe_allow_html=True)


def section_about():
    st.markdown('<a name="about"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.header("About Us")

    st.write(
        """
        **We Love Films** is a wedding photography and films studio based in Jubilee Hills, Hyderabad.  
        We focus on honest storytelling, elegant compositions, and timeless color tones.
        """
    )

    col1, col2 = st.columns([1.4, 0.6])

    with col1:
        st.markdown(
            """
            ### Our Philosophy  
            • People over poses  
            • Light & emotion come first  
            • Minimal, elegant, timeless edits  
            • Respectful, unobtrusive coverage  
            """
        )

    with col2:
        st.markdown(
            """
            ### Contact  
            **Phone:** 9553484443  
            **Email:** welovefilms54@gmail.com  
            **Location:** Jubilee Hills, Hyderabad  
            """
        )

    st.markdown('</div>', unsafe_allow_html=True)


def section_book():
    st.markdown('<a name="book"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.header("Book Us")

    with st.form("book_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *")
            email = st.text_input("Email *")
            phone = st.text_input("Phone Number *")
        with col2:
            date = st.date_input("Wedding Date *")
            location = st.text_input("Wedding Location *")
            package = st.selectbox("Package Type", ["Basic", "Premium", "Deluxe", "Not Decided"])

        message = st.text_area("Tell us about your events")

        if st.form_submit_button("Submit"):
            if not name or not email or not phone or not location:
                st.error("Please fill all required fields.")
            else:
                entry = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "wedding_date": date,
                    "location": location,
                    "package": package,
                    "message": message,
                }
                append_booking_to_csv(entry)
                st.success("Thank you! We will contact you shortly.")

    st.markdown('</div>', unsafe_allow_html=True)


def section_contact():
    st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.header("Contact")

    st.write(
        """
        **We Love Films**  
        Jubilee Hills, Hyderabad  

        **Phone:** 9553484443  
        **Email:** welovefilms54@gmail.com  
        """
    )

    st.markdown('</div>', unsafe_allow_html=True)


def footer():
    st.markdown(
        """
        <div class="footer">
        © 2025 We Love Films · All Rights Reserved
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================
# MAIN
# =========================

def main():
    top_nav()
    section_home()
    st.divider()
    section_gallery()
    st.divider()
    section_films()
    st.divider()
    section_about()
    st.divider()
    section_book()
    st.divider()
    section_contact()
    footer()


if __name__ == "__main__":
    main()
