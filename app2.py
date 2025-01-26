from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import io
import base64
from PIL import Image
import PyPDF2 as pdf
import google.generativeai as genai

genai.configure(api_key='AIzaSyD_isUil2j9h6a7kt1pW8Ca-GjhiVf3AhA')

def get_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf(upload_file):
    if upload_file is not None:
        # PDF to text
        pdf_reader = pdf.PdfReader(upload_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += str(page.extract_text())
        return text
    else:
        raise FileNotFoundError("No file found")

    
st.set_page_config(page_title = "Resume Analyzer", page_icon = "📄", layout = "centered", initial_sidebar_state = "auto")
st.header("ATS Checker")
imput_text = st.text_area("Enter the job description ", key = "input_text")
upload_file = st.file_uploader("Upload your resume", type = ["pdf"])

if upload_file is not None:
    st.write("File uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can i improvise my resume")
submit3 = st.button("Match the resume with the job description")

input_prompt1 = """
You are an experienced Technical Human Resource Manager with a strong background in recruitment and talent acquisition, Your task is to evaluate the resume and provide a detailed summary of the candidate's experience, skills, and qualifications against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the candidate's strengths and areas for improvement in relation to the specific job requirements.
"""

input_prompt2 = """
You are skilled ATS( Applicant Tracking System) Analyst with a strong background in resume optimization and recruitment technology. Your task is to evaluate the resume against the job description. Give me the percentage of the resume that matches the job description. First the output should be in percentage and then the key points missing and the final thoguhts on the resume.
"""

if submit1:
    if upload_file is not None:
        pdf_content = input_pdf(upload_file)
        response = get_response(imput_text, pdf_content, input_prompt1)
        st.subheader("Resume Summary")
        st.write(response)
    else:
        st.write("Please upload a file")

elif submit2:
    if upload_file is not None:
        pdf_content = input_pdf(upload_file)
        response = get_response(imput_text, pdf_content, input_prompt2)
        st.subheader("Resume Optimization")
        st.write(response)
    else:
        st.write("Please upload a file")
    
elif submit3:
    if upload_file is not None:
        pdf_content = input_pdf(upload_file)
        response = get_response(imput_text, pdf_content, input_prompt2)
        st.subheader("Resume Matching")
        st.write(response)
    else:
        st.write("Please upload a file")
