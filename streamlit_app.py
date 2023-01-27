import speech_recognition as sr
import os
import shutil

def transcribe_audio(language):
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()

    # Abrir el archivo de audio
    with sr.AudioFile('audio.wav') as source:
        audio = recognizer.record(source)

    # Transcribir el audio
    if language == "es":
        text = recognizer.recognize_google(audio, language='es-ES')
        filename = "transcription_es.txt"
    elif language == "en":
        text = recognizer.recognize_google(audio, language='en-US')
        filename = "transcription_en.txt"

    # Escribir el texto en el archivo
    with open(filename, "w") as file:
        file.write(text)
        
    # Mover el archivo a la carpeta de descargas del usuario
    home = os.path.expanduser("~")
    download_folder = os.path.join(home, "Downloads")
    shutil.move(filename, download_folder)
        
    return text

# Ejemplo de uso
text_es = transcribe_audio("es")
print(text_es)
text_en = transcribe_audio("en")
print(text_en)
