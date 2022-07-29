from gtts import *
from playsound import *
text="To change the overall look of your document, choose new Theme elements on the Page Layout tab. To change the looks available in the Quick Style gallery, use the Change Current Quick Style Set command. "
op=gTTS(text)
op.save("speak.mp3")
playsound("speak.mp3")
