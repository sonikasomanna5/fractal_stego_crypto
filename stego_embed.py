from PIL import Image

def embed_data(image_path, data, output_path):
    img = Image.open(image_path)
    binary_data = ''.join(format(ord(i), '08b') for i in data)
    data_len = len(binary_data)
    img_data = img.getdata()

    new_pixels = []
    data_index = 0
    for pixel in img_data:
        if data_index < data_len:
            pixel = list(pixel)
            for n in range(3):
                if data_index < data_len:
                    pixel[n] = pixel[n] & ~1 | int(binary_data[data_index])
                    data_index += 1
            new_pixels.append(tuple(pixel))
        else:
            new_pixels.append(pixel)

    img.putdata(new_pixels)
    img.save(output_path)
    return output_path
