import streamlit as st
import speech_recognition as sr

st.title("🎙️ المحول السريع جداً")

uploaded_file = st.file_uploader("ارفع ملف WAV فقط")

if uploaded_file is not None:
    st.write("جاري التحويل... يرجى الانتظار...")
    
    # استخدام BytesIO للتعامل المباشر في الذاكرة (أسرع من القرص)
    import io
    audio_file = io.BytesIO(uploaded_file.read())
    
    r = sr.Recognizer()
    
    try:
        # قراءة مباشرة بدون حفظ ملفات
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
            # استخدام محرك جوجل للتعرف
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
    except sr.UnknownValueError:
        st.error("عذراً، لم أستطع فهم الصوت.")
    except Exception as e:
        st.error(f"خطأ غير متوقع: {e}")
