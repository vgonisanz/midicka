from midicka.core import Midicka
from midicka.models import MidiNote

def main():
    core = Midicka()
    core.select_out_port(1)

    c3 = MidiNote('C', 3)
    velocity = 100
    core.send_message_out(c3, velocity)

if __name__ == "__main__":
    main()