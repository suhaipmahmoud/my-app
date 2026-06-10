import streamlit as st
import speech_recognition as sr
import librosa
import soundfile as sf
import os

st.title("🎙️ محول الصوت الشامل")

uploaded_file = st.file_uploader("ارفع ملف صوتي (يفضل أحجام صغيرة)")

if uploaded_file is not None:
    # 1. فحص الحجم قبل البدء (لتجنب انهيار السيرفر)
    if uploaded_file.size > 10 * 1024 * 1024:  # 10 ميجابايت كحد أقصى
        st.error("الملف كبير جداً! حاول رفع مقطع أقل من 10 ميجابايت.")
    else:
        with open("temp_input", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("جاري التحويل...")
        
        try:
            # 2. تحويل أول 60 ثانية فقط من الصوت لضمان عدم التعليق
            audio, sr_rate = librosa.load("temp_input", sr=None, duration=60)
            sf.write("temp_output.wav", audio, sr_rate)
            
            r = sr.Recognizer()
            with sr.AudioFile("temp_output.wav") as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data, language="ar-SA")
                st.success("تم التحويل بنجاح!")
                st.text_area("النص:", text, height=300)
        except Exception as e:
            st.error(f"خطأ: {e}")
        
        if os.path.exists("temp_input"): os.remove("temp_input")
        if os.path.exists("temp_output.wav"): os.remove("temp_output.wav")
