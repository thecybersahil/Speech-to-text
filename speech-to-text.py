import speech_recognition as sr
import tkinter as tk

# Initialize recognizer
r = sr.Recognizer()

# Record audio from microphone
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

# Recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    # Create a tkinter window and display the output in a label
    window = tk.Tk()
    label = tk.Label(window, text=text)
    label.pack()
    window.mainloop()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
