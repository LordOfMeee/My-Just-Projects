 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 23:16:54 2021

@author: W. M. Oshen Samoda Wijesundara
"""

import PySimpleGUI as sg
import gtts
from playsound import playsound
new_file = open('COVID-19_FIGHTER.txt','a')
import sys

sg.theme('TealMono')  



layout = [
    [sg.Text('Please enter your Full Name', size =(15,2)),sg.InputText()],
    [sg.Text('Please enter your Address', size =(15,2)),sg.InputText()],
    [sg.Text('Were you affected with COVID-19 for pat 14 days (yes/no)', size =(15,8)),sg.InputText()],
    [sg.Text('Do you have fever, cough or throat pain (yes/no)', size =(15, 8)), sg.InputText()],
    [sg.Text('Did you met someone who had COVID-19 in past 14 days (yes/no)', size =(15, 8)), sg.InputText()],
    [sg.Text('Enter you temperature in Celsius', size =(15, 3)), sg.InputText()],
    [sg.Text('Have you got the 2 doses of vaccination (yes/no)', size =(15, 3)), sg.InputText()],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Text('I here by tell that every information I have given is True, if so click the submit button, then close the window after getting the message')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('COVID-19 data entry window', layout)

while True:
    
    event, values = window.read()
    
    
            
           
    tts = gtts.gTTS("You are safe to meet with the person", lang='en')
    tts.save("hello.mp3")
    tts = gtts.gTTS("Your can be a person infected by COVID-19 virus", lang="en")
    tts.save("hola.mp3")        
    if int(values[5])<37:
        if (values[2].lower(),values[3].lower(),values[4].lower(),values[6].lower()) == ('no','no','no','yes'):
            
            
            playsound("hello.mp3")
            
        else:
            
            
            playsound("hola.mp3")
            window.close()
            sys.exit()
        
        
   
    
    print('Full name:',values[0],'     Address:',values[1],'     Are you affected with COVID-19 for past 14 days: ',values[2],"     symptoms :",values[3],'   Contact with effected person in last 14 days: ', values[4], '    Temperature in Celsis: ',values[5], '     Have taken two doses of vaccinarion: ', values[6])
    with open('COVID-19_FIGHTER.txt', 'a') as f:
        f.write('Full name:'+values[0]+'     Address:'+values[1]+'     Are you affected with COVID-19 for past 14 days: '+values[2]+"     symptoms :"+values[3]+'   Contact with effected person in last 14 days: '+ values[4]+ '    Temperature in Celsis: '+values[5]+'     Have taken two doses of vaccinarion: '+ values[6]+'\n')
    break


window.close()

import cv2

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Wait for the 'c' key to be pressed to capture an image
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Save the captured image
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured!")

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()


import PySimpleGUI as sg

layout = [[sg.Text('hi')],
          [sg.Text('u may go in')],]

event, values =  sg.Window('Window Title', layout).read(close=True)

window.close()





