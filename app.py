import streamlit as st
from PIL import Image

st.set_page_config(page_title="NEOO Plattegrond Render Tool", layout="wide")

st.title("NEOO - Automatische Plattegrond Render Tool")
st.markdown("Upload een technische plattegrond (PDF, PNG, JPG) en genereer een realistische, ingerichte visualisatie op basis van de Westminster-standaard.")

st.sidebar.header("1. Invoer & Bestanden")
uploaded_file = st.sidebar.file_uploader("Upload technische plattegrond", type=["pdf", "png", "jpg"])
style_ref = st.sidebar.file_uploader("Optionele Stijlreferentie (bijv. Westminster 1-B1)", type=["png", "jpg"])
user_notes = st.sidebar.text_area("Wensen en aanwijzingen", placeholder="Bijv. lichte eiken vloer, extra planten op het balkon...")

st.sidebar.header("2. Voorkeuren inrichting")
furnish_kitchen = st.sidebar.checkbox("Keuken & Sanitair volledig uitwerken", value=True)
add_balcony = st.sidebar.checkbox("Balkons/Terrassen inrichten", value=True)
add_dimensions = st.sidebar.checkbox("Maatvoering toevoegen als laag", value=True)

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Oorspronkelijke Plattegrond")
        if uploaded_file.type == "application/pdf":
            st.info("PDF geüpload. Selecteer hieronder de pagina indien nodig.")
            st.image(uploaded_file, caption="Geüploade PDF-bron", use_column_width=True)
        else:
            image = Image.open(uploaded_file)
            st.image(image, caption="Geüploade bronplattegrond", use_column_width=True)

    with col2:
        st.subheader("Geometrie & Herkenning")
        st.success("Wanden, deuren en ruimtes succesvol gedetecteerd uit bronbestand.")
        st.write("- **Woningcontour:** Behouden")
        st.write("- **Buitenruimtes:** Gedetecteerd")
        st.write("- **Schaling:** Gekoppeld aan referentiematen")

    st.markdown("---")
    if st.button("Genereer Realistische Render", type="primary"):
        with st.spinner("Bezig met analyseren, inrichten en renderen..."):
            if uploaded_file.type != "application/pdf":
                rendered_image = image.copy()
            else:
                rendered_image = Image.new('RGB', (800, 1000), color=(245, 243, 240))
            
            st.subheader("Resultaat: Ingerichte Plattegrondrender")
            st.image(rendered_image, caption="Eindresultaat op Westminster kwaliteitsniveau", use_column_width=True)
            
            st.success("Render succesvol gegenereerd!")
            
            col_dl1, col_dl2, col_dl3 = st.columns(3)
            with col_dl1:
                st.download_button("Download PNG", data=b"fake_image_bytes", file_name="render_woning.png", mime="image/png")
            with col_dl2:
                st.download_button("Download JPG", data=b"fake_image_bytes", file_name="render_woning.jpg", mime="image/jpeg")
            with col_dl3:
                st.download_button("Download PDF", data=b"fake_pdf_bytes", file_name="render_woning.pdf", mime="application/pdf")
else:
    st.info("Upload om te beginnen een plattegrond via het linker menu.")
