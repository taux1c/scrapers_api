# onlyfans_api

An API that you can import into your scraper that will handle most onlyfans functions and can handle multiple profiles at once.

More documentation coming soon, the overall thought is that you can pass an auth file to the api, the api will go handle all locating everything and return an object containing a list of objects. For example Messages will return an object with a list of message objects. This allows you to access any data from a message. For example: 

for message in Messages.messages:
    for item in message.media:
        print(item.source)
        
