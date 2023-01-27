import streamlit as st
import speech_recognition as sr
from datetime import datetime

st.set_page_config(page_title="Audio Transcription", page_icon=":microphone:", layout="wide")

def transcribe_audio():
    st.set_header("Transcribing Audio")
    audio_file = st.file_uploader("Upload an audio file in WAV format", type=["wav"])
    if audio_file is None:
        st.warning("Please upload an audio file")
    else:
        st.success("Audio file uploaded")
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text, language='en-US')
                st.success("Transcription complete!")
                st.text(text)
                # create a download button
                download_button = st.button("Download Transcription")
                if download_button:
                    # use st.download() to export the file to the user's downloads folder
                    st.download(text, "Transcription_"+str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+".txt")
                    st.success("Transcription downloaded!")
            except:
                st.error("Sorry, something went wrong. Please try again.")

if __name__ == '__main__':
    st.title("Audio Transcription App")
    transcribe_audio()
