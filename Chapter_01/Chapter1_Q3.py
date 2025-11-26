# Install an external module and use it to perform an operation of your interest
import pyjokes
import pyttsx3

a=pyjokes.get_joke()
print("joke of the day")
print(a)

engine=pyttsx3.init()
engine.say(a)
engine.runAndWait()