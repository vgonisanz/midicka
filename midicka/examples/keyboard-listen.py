from pynput import keyboard
import typer

app = typer.Typer()

def on_press(key):
    try:
        typer.echo(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        typer.echo(f'Special key {key} pressed')

def on_release(key):
    typer.echo(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

@app.command()
def listen_to_keys():
    typer.echo("Listening keyboard... Press ESC to end")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    app()
