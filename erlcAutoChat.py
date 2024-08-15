import keyboard
import sounddevice as sd
from scipy.io.wavfile import write
import openai
import os
import time
import numpy as np

# Set your OpenAI API key
openai.api_key = '' # INSER KEY

recording = None
fs = 30000  # Increased sample rate
filename = "recording.wav"
is_recording = False
is_writing   = False

def writeInChat(message):
    global is_writing
    is_writing = True
    keyboard.press_and_release("t")
    time.sleep(0.05)
    keyboard.press_and_release("#")
    time.sleep(0.1)
    keyboard.press_and_release("backspace")
    keyboard.write(message,0.005)
    time.sleep(0.05)
    keyboard.press_and_release("enter")
    is_writing = False

def start_recording():
    global recording, is_recording
    if not is_recording and not is_writing:
        print("Recording started...")
        recording = sd.rec(int(60 * fs), samplerate=fs, channels=1, dtype='int16')  # Record for a long duration
        is_recording = True

def stop_recording():
    global recording, is_recording
    if is_recording:
        print("Recording stopped.")
        sd.stop()
        recording = np.trim_zeros(recording)  # Trim silence from the recording
        write(filename, fs, recording)  # Save as WAV file
        send_to_whisper(filename)
        os.remove(filename)  # Clean up the file after sending
        is_recording = False

def send_to_whisper(filename):
    with open(filename, 'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        print("Transcription:", transcript['text'])
        writeInChat(transcript["text"])
        

def on_key_event(event):
    if event.name == 'b' and event.event_type == 'down':
        start_recording()
    elif event.name == 'b' and event.event_type == 'up':
        stop_recording()


# Listen for the key press
#keyboard.hook(on_key_event)

# Keep the script running
#keyboard.wait('esc')  # Change 'esc' to the key you want to use to stop the script
