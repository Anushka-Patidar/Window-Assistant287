import speech_recognition as sr
import sounddevice as sd
import numpy as np

from input_processor import input_processor
from command_parser import command_parser
from validator import validator
from executor import execution


def handle_command(command: str):
    tokens = input_processor(command)
    if not tokens:
        return

    ir = validator(command_parser(tokens))
    if not ir.errors:
        execution(ir)


def record_audio(duration=5, samplerate=16000):
    print("Listening...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return recording


def listen():
    r = sr.Recognizer()

    audio_data = record_audio()

    audio = sr.AudioData(audio_data.tobytes(), 16000, 2)

    try:
        return r.recognize_google(audio).lower()
    except:
        return None


def run_voice():
    print("Voice active (say 'isha')...")

    while True:
        text = listen()

        if text and "isha" in text:
            print("Activated...")
            command = listen()

            if command:
                print("Command:", command)
                handle_command(command)