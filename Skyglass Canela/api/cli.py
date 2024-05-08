import click
import time
import subprocess

@click.command()
def cli():
    while True:
        subprocess.run(['python', 'C:/api/demo.py'])

        time.sleep(30)

if __name__ == '__main__':
    cli()