from flask import Flask, render_template, request, send_file, url_for
import qrcode
import io
import os
from datetime import datetime

app = Flask(__name__)

# Ensure the static/qr_codes directory exists
os.makedirs('static/qr_codes', exist_ok=True)

def generate_qr_code(data, filename):
    """Generate a QR code from the input data and save it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img_path = os.path.join('static', 'qr_codes', filename)
    img.save(img_path)
    
    return img_path

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_path = None
    if request.method == 'POST':
        data = request.form.get('qr_data', '')
        if data:
            # Generate a unique filename using timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'qr_{timestamp}.png'
            qr_code_path = generate_qr_code(data, filename)
            # Convert the path to use forward slashes for URL
            qr_code_path = qr_code_path.replace('\\', '/')
    
    return render_template('index.html', qr_code_path=qr_code_path)

@app.route('/download/<path:filename>')
def download_qr(filename):
    # Ensure the filename is safe and within the allowed directory
    safe_filename = os.path.basename(filename)
    file_path = os.path.join('static', 'qr_codes', safe_filename)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return "File not found", 404
    
    return send_file(
        file_path,
        as_attachment=True,
        download_name=f'qr_code_{safe_filename}'
    )

if __name__ == '__main__':
    app.run(debug=True) 