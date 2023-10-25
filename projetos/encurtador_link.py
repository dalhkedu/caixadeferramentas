import random
import string


class EncurtadorURL:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}

    def encurtar_url(self, url_longa):
        if url_longa in self.url_to_short:
            return self.url_to_short[url_longa]

        caracteres_permitidos = string.ascii_letters + string.digits
        url_curta = ''.join(random.choice(caracteres_permitidos) for _ in range(6))

        self.url_to_short[url_longa] = url_curta
        self.short_to_url[url_curta] = url_longa

        return url_curta

    def redirecionar_url(self, url_curta):
        if url_curta in self.short_to_url:
            return self.short_to_url[url_curta]
        else:
            return None


if __name__ == "__main__":
    pass
