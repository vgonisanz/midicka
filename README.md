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
