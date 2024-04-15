from pywebostv.discovery import *    
from pywebostv.connection import *
from pywebostv.controls import *
import ast
import keyboard
import speech_recognition as sr

class Commands:

    def __init__(self, client):
        self.client = client
        self.system = SystemControl(self.client)
        self.media = MediaControl(self.client)
        self.inp = InputControl(self.client)
        self.inp_connect = self.inp.connect_input()
        self.inp_disconnect = self.inp.disconnect_input()
        self.source_control = SourceControl(self.client)
        self.text = ''

    def controls(self):
      
        keyboard.add_hotkey('ins', lambda: self.activate_voice())
        keyboard.wait()


    def activate_voice(self):

        r = sr.Recognizer()  
        with sr.Microphone() as source:   
            r.adjust_for_ambient_noise(source, duration=2)
            print("Say your command:")     
            audio = r.listen(source)  

            try: 
                text = r.recognize_google(audio, language='en-US', show_all=True)
                self.text = str(text['alternative'][0]['transcript'])
                print(self.text)

                if self.text == 'TV turn off':
                    print(self.text)
                    self.system.screen_off()
                elif self.text == 'TV turn on':
                    self.system.screen_on()
                elif self.text == 'TV pause':
                    self.media.pause()
                elif self.text == 'TV play':
                    self.media.play()
                elif self.text == 'TV rewind':
                    self.media.rewind()
                elif self.text == 'TV fast forward':
                    self.media.fast_forward()

            except sr.UnknownValueError:  
                print("Can't understand!!")  
            except sr.RequestError as e:  
                print("Error :(  -> {0}".format(e))



def your_custom_storage_is_empty():
    with open("store.txt", "r") as f:
        if len(f.readlines()) < 1:
            return True
def load_from_your_custom_storage():
    with open("store.txt", "r") as f:
        data = f.read()

    try:
        my_dict = ast.literal_eval(data)
    except SyntaxError:
        print("Error: Invalid dictionary format in file")
        my_dict = {}

    print(my_dict)
    return my_dict
def persist_to_your_custom_storage(store):
    with open("store.txt", "w") as f:
        print(store, file=f)
def initiate_remote():

    if your_custom_storage_is_empty():
        store = {}
    else:
        store = load_from_your_custom_storage()

    client = WebOSClient("192.168.1.137", secure=True)
    client.connect()
    for status in client.register(store):
        if status == WebOSClient.PROMPTED:
            print("Accept Prompt on TV!")
        elif status == WebOSClient.REGISTERED:
            print("Registration with TV sucessful")
    print(store) 

    persist_to_your_custom_storage(store)
    return client
     
client = initiate_remote()
new_input = Commands(client)
new_input.controls()



