import click

@click.command()
@click.option('--name', prompt='Your name',help='User name.')
@click.option('--age', prompt='Your age', help = 'User age.')

def greet(name,age):
    click.echo(f'Hello, {name}! You are {age} years old.')

if __name__ == '__main__':
    greet()
