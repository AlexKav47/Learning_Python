import os
import re


def make_filename_safe(text: str) -> str:
    safe = re.sub(r'[^A-Za-z0-9_-]+', '_', text).strip('_')
    return safe or 'qr_code'


def generate_qr_code(data: str, filename: str = 'qr_code.png') -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color='black', back_color='white')
    image.save(filename)
    return filename


def get_output_filename(base_name: str) -> str:
    base_root, base_ext = os.path.splitext(base_name)
    if not base_ext:
        base_ext = '.png'
    candidate = f'{base_root}{base_ext}'
    counter = 1
    while os.path.exists(candidate):
        candidate = f'{base_root}_{counter}{base_ext}'
        counter += 1
    return candidate


def main() -> None:
    print('QR Code Generator')
    print('Enter text, a URL, or any data to encode as a QR code.')

    data = input('Text to encode: ').strip()
    if not data:
        print('No text entered. Exiting.')
        return

    suggested_name = make_filename_safe(data[:32]) + '.png'
    filename = input(f'Output file name [{suggested_name}]: ').strip() or suggested_name
    filename = get_output_filename(filename)

    output_path = generate_qr_code(data, filename)
    print(f'QR code saved to: {output_path}')


if __name__ == '__main__':
    main()
