import typer
import time
from pynput.keyboard import Controller

app = typer.Typer()

@app.command()
def press_key(key: str):
    keyboard = Controller()
    typer.echo(f"Lets push {key} after 3s...")
    time.sleep(3)
    with keyboard.pressed(key):
        typer.echo(f"Pressed {key}")

if __name__ == "__main__":
    app()
