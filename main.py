from fractal_generator import generate_mandelbrot
from crypto_module import encrypt_message, decrypt_message, generate_key
from stego_embed import embed_data
from stego_extract import extract_data

def main():
    print("🔒 Fractal Veil: A Morphogenic Stego-Crypto System 🔒")

    key = generate_key()
    print("Generated AES Key:", key.hex())

    # Step 1: Generate fractal
    fractal_path = generate_mandelbrot()
    print(f"Fractal generated: {fractal_path}")

    # Step 2: Encrypt message
    message = "SecretMessage#"
    encrypted = encrypt_message(message, key)
    print("Encrypted message:", encrypted)

    # Step 3: Embed into fractal
    stego_path = "assets/output/stego_fractal.png"
    embed_data(fractal_path, encrypted, stego_path)
    print(f"Data embedded in {stego_path}")

    # Step 4: Extract data
    extracted = extract_data(stego_path)
    print("Extracted encrypted data:", extracted)

    # Step 5: Decrypt
    decrypted = decrypt_message(extracted, key)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
