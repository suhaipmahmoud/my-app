import streamlit as st
import speech_recognition as sr
import os

st.title("🎙️ المحول البسيط والمضمون")

uploaded_file = st.file_uploader("ارفع ملف wav صغير")

if uploaded_file is not None:
    st.write("جاري التحويل...")
    try:
        # حفظ الملف مؤقتاً بصيغة wav (هذه الطريقة هي الأكثر توافقاً مع السيرفرات)
        with open("audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        r = sr.Recognizer()
        with sr.AudioFile("audio.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
    except Exception as e:
        st.error(f"خطأ: {e}")
    finally:
        # حذف الملف بعد الاستخدام
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")
