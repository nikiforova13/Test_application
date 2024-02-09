import click
from app.main import app


@click.group()
def cli():
    pass


@cli.command()
@click.option("--host", default="0.0.0.0", help="Host for running app")
@click.option("--port", default=8000, help="Port to listen on")
def serve(host: str, port: int):
    app.run(host=host, port=port)


if __name__ == "__main__":
    cli()
