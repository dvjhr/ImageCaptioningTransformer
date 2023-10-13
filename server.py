from flask import Flask, request, jsonify
from my_model import generate_caption, decode_and_resize

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        image_file = request.files['image']
        image_data = image_file.read()
        # print(type(image_data))
        image = decode_and_resize(image_data)
        caption = generate_caption(image)
        return jsonify({"caption": caption}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=False)