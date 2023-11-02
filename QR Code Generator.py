import os
import qrcode

def generate_qr_code(data, folder_path, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    file_path = os.path.join(folder_path, file_name)
    img.save(file_path)

if __name__ == "__main__":
    data = "https://www.google.com"  # Replace with your desired data
    folder_path = "F:\MADHAV\Python Projects"  # Replace with your desired folder path
    file_name = "my_qr_code.png"     # Output file name

    generate_qr_code(data, folder_path, file_name)
    print(f"QR code saved as {os.path.join(folder_path, file_name)}")
