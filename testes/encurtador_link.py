import unittest

from projetos.encurtador_link import EncurtadorURL


class TestEncurtadorURL(unittest.TestCase):
    def setUp(self):
        self.encurtador = EncurtadorURL()

    def test_encurtar_e_redirecionar_url(self):
        url_longa = "https://www.example.com/seu/link/longo"

        url_curta = self.encurtador.encurtar_url(url_longa)
        self.assertIsInstance(url_curta, str)

        url_redirecionada = self.encurtador.redirecionar_url(url_curta)
        self.assertEqual(url_longa, url_redirecionada)

    def test_redirecionar_url_inexistente(self):
        url_curta = "url_inexistente"

        url_redirecionada = self.encurtador.redirecionar_url(url_curta)
        self.assertIsNone(url_redirecionada)


if __name__ == "__main__":
    unittest.main()
