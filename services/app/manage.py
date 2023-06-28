"""This script launches the application."""
from api import create_app
# from api.helpers.add_channels import (
#     add_channel_playlists,
#     add_palylist_items,
#     create_channels,
#     find_channel,
#     get_video_comments,
#     save_to_channels,
# )
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("seed_db")
def seed_db():
    """Create the database records."""
    # add_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')


if __name__ == "__main__":
    cli()
