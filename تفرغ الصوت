import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os

st.title("محول الملفات إلى نص")

uploaded_file = st.file_uploader("ارفع ملف الصوت", type=['wav', 'mp3', 'ogg', 'opus', 'mp4'])

if uploaded_file is not None:
    file_path = "input_file"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("جاري التحليل...")
    
    try:
        audio = AudioSegment.from_file(file_path)
        audio.export("temp_wav.wav", format="wav")
        
        r = sr.Recognizer()
        with sr.AudioFile("temp_wav.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم")
            st.text_area("النص:", text, height=300)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
