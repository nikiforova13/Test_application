import click
from app.main import app


@click.group()
def cli():
    pass


@cli.command()
@click.option("--host", default="0.0.0.0", help="ssss")
@click.option("--port", default=8000)
def serve(host: str, port: int):
    app.run(host=host, port=port)


if __name__ == "__main__":
    cli()
