import unittest
from dictionary import Dictionary


class TestStorage(unittest.TestCase):
    def test_store(self):
        result1 = Dictionary("title","content","sender", "https://www.google.com")
        result2 = Dictionary("internet security", "Norton Internet Security gave you virus protection", "Samy", "https://en.wikipedia.org")
        result3 = Dictionary("AAA", "SSS", "DDD",
                          "https://en.Edia.org")
        self.assertEqual(result1.store(), {'title': 'title', 'sender': 'sender', 'content': 'content', 'url': 'https://www.google.com'})
        self.assertEqual(result2.store(),
                         {'title': 'internet security', 'sender': 'Samy',
                          'content': 'Norton Internet Security gave you virus protection',
                          'url': 'https://en.wikipedia.org'})
        #self.assertEqual(result3.store(),
                        # {'title': 'title', 'sender': 'sender', 'content': 'content', 'url': 'https://www.google.com'})


if __name__ == '__main__':
    unittest.main()