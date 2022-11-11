import config
import cogs.auth
import cogs.media


# Class used to store and handle all Message objects. Each user can have their own Messages object.
# This way data can be stored in memory, database, json, etc. without waiting for downloads or slower parts of the scraper.

class Messages:
    def __init__(self):
        self.messages = []

    def parse(self):
        pass


# Each message is stored as a Message object. This allows for each message to have its own settings, methods, etc.
# We  can then pull all information from a message and scrapers can access any of it.
Class Message:
    def __init__(self):
        self.media = []
