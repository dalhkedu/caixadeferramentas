import qrcode


class GeradorQRCode:
    def __init__(self, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4):
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border

    def gerar_qrcode(self, url, fill_color="black", back_color="white", save_path=None):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        if save_path:
            img.save(save_path)
        return img


if __name__ == "__main__":
    pass
