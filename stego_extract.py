from PIL import Image

def extract_data(stego_path):
    img = Image.open(stego_path)
    binary_data = ''
    for pixel in img.getdata():
        for n in range(3):
            binary_data += str(pixel[n] & 1)

    # Split into 8-bit chunks
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in bytes_data:
        char = chr(int(byte, 2))
        if char == '#':  # delimiter to stop extraction
            break
        message += char
    return message
