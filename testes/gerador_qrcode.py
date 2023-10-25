import os
import unittest

from projetos.gerador_qrcode import GeradorQRCode


class TestGeradorQRCode(unittest.TestCase):
    def setUp(self):
        # Crie uma instância do GeradorQRCode para cada teste
        self.gerador = GeradorQRCode()

    def test_geracao_qrcode(self):
        url = "https://www.example.com"
        save_path = "qrcode_test.png"

        # Gere o QR code
        qrcode_img = self.gerador.gerar_qrcode(url, save_path=save_path)

        # Verifique se o arquivo foi criado
        self.assertTrue(os.path.exists(save_path))

        # Verifique se a imagem é do tipo Pillow
        self.assertTrue(isinstance(qrcode_img, type(self.gerador.gerar_qrcode(url))))

    def tearDown(self):
        # Exclua o arquivo de teste após o teste
        save_path = "qrcode_test.png"
        if os.path.exists(save_path):
            os.remove(save_path)


if __name__ == "__main__":
    unittest.main()
