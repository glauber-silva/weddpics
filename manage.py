from flask.cli import FlaskGroup
from app import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command
def about():
    return "Wedding photo gallery"


if __name__ == '__main__':
    cli()

