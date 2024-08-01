import base64
import streamlit as st
from streamlit_pdf import pdf

# Function to display PDF
def display_pdf(file_path):
    with open(file_path, "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Title of the app
st.title("PDF Viewer")

# Buttons to display the PDFs
if st.button("View PDF 1"):
    display_pdf("pdf-dir/KAPS Paper 1_05022024.pdf")

if st.button("View PDF 2"):
    display_pdf("pdf-dir/KAPS Paper 2_05022024.pdf")
