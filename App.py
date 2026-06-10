import streamlit as st
import speech_recognition as sr
import librosa
import soundfile as sf
import io

st.title("🎙️ محول الصوت الاحترافي")

uploaded_file = st.file_uploader("ارفع ملفك الصغير")

if uploaded_file is not None:
    st.write("جاري المعالجة المباشرة...")
    
    try:
        # قراءة محتوى الملف إلى الذاكرة مباشرة
        audio_bytes = uploaded_file.read()
        
        # تحويل من الذاكرة باستخدام librosa
        audio, sr_rate = librosa.load(io.BytesIO(audio_bytes), sr=None)
        
        # حفظ الـ wav في الذاكرة أيضاً (بدون إنشاء ملف على القرص)
        wav_io = io.BytesIO()
        sf.write(wav_io, audio, sr_rate, format='wav')
        wav_io.seek(0)
        
        # التحويل للنص
        r = sr.Recognizer()
        with sr.AudioFile(wav_io) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ar-SA")
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
            
    except Exception as e:
        st.error(f"حدث خطأ برمجياً: {e}")
