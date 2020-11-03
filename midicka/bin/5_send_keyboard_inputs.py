from midicka.core import Midicka

def main():
    core = Midicka()
    
    message = "Hello keyboard"
    for letter in message:
        core.send_to_keyboard(letter)

if __name__ == "__main__":
    main()
