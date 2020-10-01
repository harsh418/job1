
import os
import pyttsx3
print("-----------------------------Welcome to speach reognition System----------------------------------")
pyttsx3.speak("Hello Welcome To The Contact Service Of a Company. Company Welcome's You ")

print()
print("Press 1 For Chrome")
print("Press 2 For Notepad")
print()

print ("Enter yours Choice: ",end='')
p=input()

if int(p)==1:
   os.system("chrome")
if int(p)==2:
   os.system("notepad")
