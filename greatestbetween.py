from gtts import *
from playsound import *

op = gTTS("Enter First number")
op.save("best.mp3")
playsound("best.mp3")

a=int(input("Enetr First number"))

op = gTTS("Enter First number")
op.save("best1.mp3")
playsound("best1.mp3")
b=int(input("enter Second number"))
if a>b:
    print("a is greatest")
    op = gTTS("a is greatest")
    op.save("test.mp3")
    playsound("test.mp3")
else:
    print("b is greatest")
    op = gTTS("b is greatest")
    op.save("test.mp3")
    playsound("test.mp3")