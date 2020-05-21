import V7xStyle
from gtts import gTTS
import os
os.system("clear")
Square = V7xStyle.Style('T','E','X','T').Square()
Figlet = V7xStyle.Text('to mp3').Figlet()
print (f"{Square}\n{Figlet}")
V7xStyle.Animation.SlowText('[+]3idkom mobarek\n\n')
text=input("[+]enter your text:#")
print ("")
language=input("[+]Enter the code for your language :#")
output=gTTS(text,lang=language,slow=False )
os.system("clear")
print ("[+] wating the ")
V7xStyle.Animation.Loading()
output.save("output.mp3")
print ("[+] done....")
os.system("mv output.mp3 /sdcard")
