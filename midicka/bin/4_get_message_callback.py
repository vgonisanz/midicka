from midicka.core import Midicka

def callback(msg, timestamp):
    message = Message(msg)
    msg_type, note, octave = message.get()
    if msg_type:
        logger.info("got_message", note=note, octave=octave, msg_type=msg_type)

def main():
    core = Midicka()
    core.select_in_port(1)
    core.receive_message_blocking()

if __name__ == "__main__":
    main()