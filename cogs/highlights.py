import config
import cogs.auth
import cogs.media

# Should the module log errors? (True/False)
log_on = True
# Where should the module log errors?
log_file = pathlib.Path(r"~/logs/highlights.log").expanduser()


# Where should downloads be saved?
download_dir = pathlib.Path(r"~/downloads").expanduser()

# The module's name
name = "onlyfans_api_highlights"
# The module's description
description = "Highlights"

# The module's version
version = "0.0.1_BETA"

# The module's author
author = "Taux1c"

def highlight_notify(message):
    if log_on:
        with open(log_file, 'a') as f:
            f.write(message + '\n')

highlight_endpoints = {

"":"",

}
def highlightEndPoints(location):
    if location not in highlight_endpoints:
        raise Exception("Invalid location")
    return highlight_endpoints[location]

# Class used to store and handle all Highlight objects. Each user can have their own Highlights object.
# This way data can be stored in memory, database, json, etc. without waiting for downloads or slower parts of the scraper.
class Highlights:
    def __init__(self):
        # List of Highlight objects
        self.highlights = []

    def parse(self):
        pass





# Class used for individual highlights. Allowing for each highlight to have its own settings, methods, etc.
class Highlight:
    def __init__(self):
        # List of HighlightMedia objects
        self.media = []




    # Download all media files from the source.
    def download_all(self):
        try:
            for media in self.media:
                if not media.download():
                    highlight_notify("Failed to download media: " + media.url)
            return True
        except Exception as e:
            highlight_notify("Error with highlight.download_all(): " + str(e))
            return False


# Class used for individual media. Allowing for each media to have its own settings, methods, etc.
class HighlightMedia:
    def __init__(self):
        # Source file location of the media file.
        self.source = None

    # Download the media file from the source.
    def download(self):
        with httpx.client() as client:
            try:
                r = client.get(self.source)
                with open(download_dir / self.source.split('/')[-1], 'wb') as f:
                    f.write(r.content)
                return True
            except Exception as e:
                highlight_notify("Error with highlight.download(): " + str(e))
                return False