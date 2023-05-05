import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Record audio from microphone
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

# Recognize speech using Google Speech Recognition
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
