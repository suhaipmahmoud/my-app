import streamlit as st
import speech_recognition as sr
import os

st.title("🎙️ محول الصوت السريع")

uploaded_file = st.file_uploader("ارفع ملف صوتي (يفضل .wav لضمان العمل بدون مشاكل)")

if uploaded_file is not None:
    file_path = "temp_file.wav"
    
    # حفظ الملف المرفوع مباشرة
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("جاري المعالجة...")
    
    try:
        r = sr.Recognizer()
        
        # قراءة الملف مباشرة بدون تحويل معقد
        with sr.AudioFile(file_path) as source:
            # تقليل حجم البيانات المأخوذة لتسريع العملية
            audio_data = r.record(source)
            
            # التحويل باستخدام سيرفرات جوجل (سريع جداً)
            text = r.recognize_google(audio_data, language="ar-SA")
            
            st.success("تم التحويل!")
            st.text_area("النص:", text, height=300)
            
    except Exception as e:
        st.error("حدث خطأ. تأكد أن الملف ليس طويلاً جداً أو بصيغة غير مدعومة.")
        st.write("نصيحة: إذا استمرت المشكلة، جرب رفع ملف بصيغة WAV فقط.")
    
    # تنظيف
    if os.path.exists(file_path):
        os.remove(file_path)
