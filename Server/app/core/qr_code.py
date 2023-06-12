import base64
import os

import qrcode

from app.core.settings import settings


def create_qr_code(id: int):
    path = os.path.join(settings.QR_CODES_DIRECTORY, f"{id}.png")

    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr_code.add_data(base64.b64encode(str(id).encode("utf-8")))
    qr_img = qr_code.make_image(fill_color="black", back_color="white")
    qr_img.save(path)

    return path
