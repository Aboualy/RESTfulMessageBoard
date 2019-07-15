from dicttoxml import dicttoxml

messages = [
    {
        'title': 'First message',
        'sender': 'Aboualy Mahmoud',
        'content': 'The text of an electronic mail message ',
        'url': 'https://github.com/Aboualy/'
    },
    {
        'title': 'Second message',
        'sender': 'Samy Laine',
        'content': 'An object that specifies the message contents ',
        'url': 'https://www.youtube.com/'
    }
]


class Database:
    def __init__(self, dictofmessages=None):
        if dictofmessages is None:
            dictofmessages = messages
        self.dictofmessages = dictofmessages

    #Returning all the messages from the database
    @staticmethod
    def give_dict():
        return messages

    #Adding a new message the database
    def add_to_dict(self):
        if self.dictofmessages != messages:
            x = messages.insert(0, self.dictofmessages)
        return x

    # The url field is dropped from the dictionary as asked
    def dict_to_json(self):
        json_format = [{x: d[x] for x in d if x != 'url'} for d in self.dictofmessages]
        return json_format

    def dict_to_xml(self):
        xml_format = dicttoxml(self.dictofmessages, custom_root='items', attr_type=False)
        return xml_format
