import streamlit as st
import claude2
import re

@st.cache
def load_model():
    return claude2.load_model("https://example.com/claude2_model") 

model = load_model()

st.title("Commercial Mortgage Appraisal Data Extraction")

pdf_file = st.file_uploader("Upload PDF of Appraisal")

if pdf_file:

    text = model.extract_text(pdf_file)

    # Search extracted text
    property_address = re.search(r"\d+\s[A-z]+\s[A-z]+,", text).group()  
    property_type = re.search(r"Property Type:\s(\w+)", text).group(1)
    appraisal_firm = re.search(r"Prepared By:\s([\w\s]+)", text).group(1)
    appraised_value = re.search(r"Appraised Value:\s\$(\d+)", text).group(1)
    effective_date = re.search(r"Effective Date:\s(\d{1,2}/\d{1,2}/\d{4})", text).group(1) 
    property_description = re.search(r"Property Description:\s(.*\n.*)", text).group(1)
    property_sqft = re.search(r"Total Square Feet:\s(\d+)", text).group(1)
    num_units = re.search(r"Number of Units:\s(\d+)", text).group(1)
    net_operating_income = re.search(r"Net Operating Income:\s\$(\d+)", text).group(1)
    cap_rate = re.search(r"Capitalization Rate:\s(\d+%)", text).group(1)

    # Display results
    st.header("Extracted Data")
    st.write("Property Address:", property_address)
    st.write("Property Type:", property_type)
    st.write("Appraisal Firm:", appraisal_firm)  
    st.write("Appraised Value:", appraised_value)
    st.write("Effective Date:", effective_date)
    st.write("Property Description:", property_description)
    st.write("Square Footage:", property_sqft)
    st.write("Number of Units:", num_units)
    st.write("Net Operating Income:", net_operating_income)
    st.write("Capitalization Rate:", cap_rate)
