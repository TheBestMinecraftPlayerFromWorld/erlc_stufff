import whisper
import speech_recognition as sr
import numpy as np
import wave
import time

# Load Whisper model
model = whisper.load_model("base.en")

# Buffer to accumulate audio data
audio_buffer = []

def callback(recognizer, audio):
    global audio_buffer
    try:
        # Append new audio data to the buffer
        audio_buffer.append(audio.get_wav_data())

        # If buffer length exceeds a certain threshold, process it
        if len(audio_buffer) >= 10:  # Adjust this value as needed
            # Concatenate all audio data in the buffer
            combined_audio = b''.join(audio_buffer)
            audio_buffer = []  # Clear the buffer

            # Save combined audio to a temporary file
            with open("temp.wav", "wb") as f:
                f.write(combined_audio)

            # Transcribe audio using Whisper
            result = model.transcribe("temp.wav")
            print("You said: " + result["text"])
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper service; {0}".format(e))

recognizer = sr.Recognizer()
microphone = sr.Microphone(3)

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)

stop_listening = recognizer.listen_in_background(microphone, callback)

# Keep the program running indefinitely
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

# Stop the background listening
stop_listening(wait_for_stop=False)
