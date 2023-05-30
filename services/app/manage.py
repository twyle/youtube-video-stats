from flask.cli import FlaskGroup
from api import create_app
from api.helpers.add_channels import (
    save_to_channels, find_channel, create_channels, add_channel_playlists, add_palylist_items,
    get_video_comments
)

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("seed_db")
def seed_db():
    """Create the database records."""
    # file = 'kenyan_channels.json'
    # resp = create_channels(file)
    # add_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
    # add_palylist_items('PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3')
    get_video_comments('VSB2vjWa1LA')

if __name__ == "__main__":
    cli()