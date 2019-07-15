import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_about(self):
        c = app.test_client(self)
        response = c.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        home = app.test_client(self)
        resp = home.get('/home', content_type='html/text')
        self.assertEqual(resp.status_code, 200)

    def test_show_messages(self):
        msg = app.test_client(self)
        res = msg.get('/message-service')
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
        unittest.main()