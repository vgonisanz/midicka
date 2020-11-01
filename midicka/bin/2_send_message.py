from midicka.core import Midicka

def main():
    core = Midicka()
    core.select_out_port(1)
    core.send_message_out()

if __name__ == "__main__":
    main()