from flask import Flask, render_template, request, jsonify
import base64, io, os
from PIL import Image

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    allowed = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'}
    ext = file.filename.rsplit('.', 1)[-1].lower()
    if ext not in allowed:
        return jsonify({'error': 'File type not supported'}), 400

    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert('RGBA')
    
    # Re-encode as PNG for consistent canvas rendering
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return jsonify({
        'image': f'data:image/png;base64,{b64}',
        'width': img.width,
        'height': img.height
    })

if __name__ == '__main__':
    app.run(debug=True)
