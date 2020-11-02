from midicka.core import Midicka

def main():
    core = Midicka()
    core.select_in_port(1)
    core.receive_message_blocking()

if __name__ == "__main__":
    main()