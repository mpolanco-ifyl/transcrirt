import streamlit as st
import os
from pocketsphinx import LiveSpeech

def transcribe_audio():
    st.title("Transcribing Audio")
    audio_file = st.file_uploader("Upload an audio file in WAV format", type=["wav"])
    if audio_file is None:
        st.warning("Please upload an audio file")
    else:
        st.success("Audio file uploaded")
        # set the language model to use
        language_model = st.selectbox("Select Language Model", ["en-US", "es-ES"])
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(
                "pocketsphinx-data", "model", language_model, "hmm"
            ),
            lm=os.path.join(
                "pocketsphinx-data", "model", language_model, "lm.bin"
            ),
            dic=os.path.join(
                "pocketsphinx-data", "model", language_model, "dict"
            ),
        )
        # transcribe the audio
        text = ""
        for phrase in speech:
            text += phrase
        st.success("Transcription complete!")
        st.text(text)
        # create a download button
        download_button = st.button("Download Transcription")
        if download_button:
            # use st.download() to export the file to the user's downloads folder
            st.download(text, "Transcription_"+str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+".txt")
            st.success("Transcription downloaded!")

if __name__ == '__main__':
    st.title("Audio Transcription App")
    transcribe_audio()
