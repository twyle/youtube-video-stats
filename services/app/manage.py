from api import create_app
from api.helpers.add_channels import (
    add_channel_playlists,
    add_palylist_items,
    create_channels,
    find_channel,
    get_video_comments,
    save_to_channels,
)
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('create_db')
def create_db():
    print('Create db')


@cli.command('seed_db')
def seed_db():
    """Create the database records."""
    # get_video_comments('VSB2vjWa1LA')
    # file = 'kenyan_channels.json'
    # resp = create_channels(file)
    add_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
    # add_palylist_items('PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3')


if __name__ == '__main__':
    cli()
