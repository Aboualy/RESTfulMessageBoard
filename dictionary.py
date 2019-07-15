class Dictionary:

    # A simple class to maintain each message in a dictionary

    def __init__(self, title, content, sender, url):
        self.title = title
        self.content = content
        self.sender = sender
        self.url = url

    def store(self):
        x = dict(title=self.title, sender=self.sender, content=self.content, url=self.url)
        return x

