from django.test import TestCase, Client

# Create your tests here.


class Testes(TestCase):
    def test_a(self):

        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
