import pathlib
import dropbox
import re
import configparser


def upload_to_dropbox(file, file_name):
    # target location in Dropbox
    target = "/TTS/Magic/"            # the target folder
    targetfile = target + file_name  # the target path and file name

    # Get the API key from the config
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_key = config['Dropbox']['API_V2']
    if not api_key:
        print("Please specify your Dropbox API key in config.ini")
        print("See https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/")
        return

    # Create a dropbox object using an API v2 key
    d = dropbox.Dropbox(api_key)

    d.files_upload(file, targetfile,
                   mode=dropbox.files.WriteMode("overwrite"))

    # create a shared link
    link = d.sharing_create_shared_link(targetfile)

    # url which can be shared
    url = link.url

    # link which directly downloads by replacing ?dl=0 with ?dl=1
    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
    return dl_url
