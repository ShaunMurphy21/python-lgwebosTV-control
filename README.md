
# Voice Control Older/Lower end WebOS TV's with python!

Python version > 3.11 from my testing doesn't work due to ssl and wrap_socket. I used 3.7.6 in development, so I'd recommend the same -> pyenv install 3.7.6 && pyenv local 3.7.6 && python -m venv env

Read requirements.txt - i think the only troublesome one was PyAudio - visit: https://pypi.org/project/PyAudio/0.2.12/ download your OS/system version and install with pip inside your venv and will be golden.




If anyone is in the habbit of losing their remote or not having your mobile handy to remote control it that way, this might be for you. 

Very simple to use, just edit the file and change ```client = WebOSClient("192.168.1.137", secure=True)``` to your TV's ip address (can either be found in your TV settings or through router panel) accept the prompts on your TV screen and good to go. 

I'm not entirely sure how long the client key lasts unfortunately so that could become a pain. I'd assume it's definitely over 24 hours though. 

Huge thanks to @klattimer and @supersaiyanmode for their collaborative work on developing the modules into what they are today. 

You can find the possible commands to integrate on: https://github.com/supersaiyanmode/PyWebOSTV

When integrating - take note of:
```
    self.client = client
    self.system = SystemControl(self.client)
    self.media = MediaControl(self.client)
    self.inp = InputControl(self.client)
    self.inp_connect = self.inp.connect_input()
    self.inp_disconnect = self.inp.disconnect_input()
    self.source_control = SourceControl(self.client)
    self.text = ''
```

Should be no need to do this twice.

Adding voice commands:

Locate the disgusting if/elif tree below

```
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
```

Then just edit the current commands or add-in your own. E.g, to add a volume one - at the bottom of the mess you'd add:

```
    elif self.text == 'TV volume up':
        self.media.volume_up()
```

Additionally, hotkeys can be changed by editing 
```
    def controls(self):
      
        keyboard.add_hotkey('ins', lambda: self.activate_voice())
        keyboard.wait()
```

Keyboard 'letters'/buttons can be found at:
https://github.com/boppreh/keyboard/blob/e277e3f2baf53ee1d7901cbb562f443f8f861b90/keyboard/_canonical_names.py#L12


This probably isn't that useful for anyone but me. Mainly for when I've lost my remote and my phone app only works half the time so when I get asked to turn the TV on or turn it down/rewind etc - it's a chore. By keepying this running in the background and only pressing the hotkey when needed it is a literal life saver
