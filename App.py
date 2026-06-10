import streamlit as st
import speech_recognition as sr
import os

st.title("🎙️ محول الصوت المضمون")

# إضافة رابط لموقع تحويل سريع للمستخدم
st.warning("إذا لم يعمل ملفك، حوله إلى صيغة WAV من هنا: [Online Audio Converter](https://online-audio-converter.com/)")

uploaded_file = st.file_uploader("ارفع ملف بصيغة WAV فقط")

if uploaded_file is not None:
    st.write("جاري المعالجة...")
    try:
        # حفظ الملف مؤقتاً
        with open("audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        r = sr.Recognizer()
        with sr.AudioFile("audio.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
    finally:
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")
