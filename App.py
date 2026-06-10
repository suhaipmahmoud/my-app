import streamlit as st
import speech_recognition as sr
import librosa
import soundfile as sf
import os

st.title("🎙️ محول الصوت الشامل")

uploaded_file = st.file_uploader("ارفع أي ملف صوتي")

if uploaded_file is not None:
    # 1. حفظ الملف المرفوع
    with open("temp_input", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("جاري التحويل...")
    
    try:
        # 2. تحويل أي صيغة إلى WAV باستخدام librosa
        # هذه الخطوة هي التي تنهي مشكلة "لا يقبل إلا wav"
        audio, sr_rate = librosa.load("temp_input", sr=None)
        sf.write("temp_output.wav", audio, sr_rate)
        
        # 3. معالجة الملف المحول
        r = sr.Recognizer()
        with sr.AudioFile("temp_output.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
            
    except Exception as e:
        st.error(f"خطأ: {e}")
    
    # تنظيف
    if os.path.exists("temp_input"): os.remove("temp_input")
    if os.path.exists("temp_output.wav"): os.remove("temp_output.wav")
