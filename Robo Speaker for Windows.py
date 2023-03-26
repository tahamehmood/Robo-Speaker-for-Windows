# First install gtts from cmd by running command 'pip install gtts' in cmd.
import os
from gtts import gTTS
print("Welcome to Robo Speaker 1.0")
y="I am a robo speaker program developed by taha mahmood enjoy the program"
output=gTTS(text=y)
output.save("y.mp3")
os.system("y.mp3")
while(True):
    x=input("Input to Speak: ")
    if x=="quit":
        print("Program Ended Successfully.")
        break
    output=gTTS(text=x)
    output.save("x.mp3")
    os.system("x.mp3")