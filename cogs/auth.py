import config
import json

# Class used to store and handle onlyfans auths. This allows the scraper to handle multiple profiles at once.


class Auth:
    # auth_file expects a pathlib object to a json file.
    def __init__(self,auth_file):
        self.auth_file = auth_file
        self.auth_details = json.load(self.auth_file.read_bytes())
        self.auth = {
            "sess" : self.auth_details["sess"],
            "auth_id" : self.auth_details["auth_id"],
            "x-bc" : self.auth_details["x-bc"],
            "user-agent" : self.auth_details["user-agent"],

        }
