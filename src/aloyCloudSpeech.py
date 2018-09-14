import threading
import requests
import time

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

threads = []

def play_tinkle():
    aiy.audio.play_wave("/home/pi/aloyVK/assets/googlestart.wav")

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_hotword(hotword_list=['Aloy', 'Ok Google', 'Ok Aloy'])

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Listening...waiting for hotword.')
        text = recognizer.recognize()
        print('Got hotword.')
        task = threading.Thread(target=play_tinkle)
        threads.append(task)
        task.start()
        if text is None:
            print('Sorry, I did not hear you.')
            aiy.audio.say('Lo siento, no te he escuchado', lang='es-ES')
        else:
            print('You said "', text, '"')



if __name__ == '__main__':
    main()
