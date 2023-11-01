# Midicka

Play magicka with MIDI

Use rtmidi2

## Installation on WSL W10 Ubuntu

Install basic development requirements:

```
sudo apt install python-pip
pip install tox
pip install pip-tools   # This one is optional for update environment only
```

Create virtual tox environment

```
make env-create
```

Requires MobaXterm for XServer and ALSA https://x410.dev/cookbook/wsl/enabling-sound-in-wsl-ubuntu-let-it-sing/

## Fedora

*TODO*

## Usage 

Each time you are going to develop you need to activate the environment:

```
source ./.tox/midicka/bin/activate
```

Check if works with any sample:

```
python midicka/bin/1_hello_midi.py
```

## Update dependencies

1. Update the `requirements.in`: Manual edition.
2. Regenerate `requirements.txt`: Execute `make env-compile`
2. Regenerate `tox environment`: Execute `make env-create`

## WSL

---> Not work by now. <----

No MIDI support in WSL AFAIK

Audio: https://github.com/Microsoft/WSL/issues/486

1. sudo add-apt-repository ppa:therealkenc/wsl-pulseaudio
2. sudo apt install pulseaudio
3. export PULSE_SERVER=tcp:localhostnumpy ipython
4. wget https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav
5. aplay StarWars3.wav
6. ln -s /usr/lib/x86_64-linux-gnu/alsa-lib/libasound_module_conf_pulse.so /usr/lib64/alsa-lib/libasound_module_conf_pulse.so
7. 
