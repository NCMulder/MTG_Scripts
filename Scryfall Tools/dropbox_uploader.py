import configparser
import re

import dropbox


def upload_to_dropbox(file, file_name):
    """Upload file to dropbox."""

    # Target location in Dropbox
    target_file = f'/TTS/Magic/{file_name}'

    # Get the API key from the config
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['Dropbox']['API_V2']
    if not api_key:
        raise NameError(
            'Dropbox API key not defined in config.ini\n'
            'See https://blogs.dropbox.com/developers/2014/05/'
            'generate-an-access-token-for-your-own-account/'
        )

    # Create a dropbox object using an API v2 key
    d = dropbox.Dropbox(api_key)

    d.files_upload(
        file,
        target_file,
        mode=dropbox.files.WriteMode('overwrite')
    )

    # Create a shared link
    link = d.sharing_create_shared_link_with_settings(target_file)

    # URL which can be shared
    url = link.url

    # Link which directly downloads by replacing ?dl=0 with ?dl=1
    dl_url = re.sub(r'\?dl=0', '?dl=1', url)
    return dl_url
