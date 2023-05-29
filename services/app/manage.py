from flask.cli import FlaskGroup
from api import create_app
from api.helpers.add_channels import save_to_channels, find_channel, create_channels, add_channel_playlists

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("seed_db")
def seed_db():
    """Create the database records."""
    # file = 'kenyan_channels.json'
    # resp = create_channels(file)
    add_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')

if __name__ == "__main__":
    cli()