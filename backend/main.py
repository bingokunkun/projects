import json
import base64
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/get_image', methods=['GET'])
def get_image():
    # 获取参数text，尽管这个例子中我们不会使用这个参数
    text = request.args.get('text', '')
    if text == "1":
        selected_image_path = "1.png"
    elif text == "2":
        selected_image_path = "2.png"
    else:
        return json.dumps({"image": ""}), 404

    # 读取图片并转换为base64编码
    with open(selected_image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # 返回图片的base64编码
    return json.dumps({'image': encoded_string})


if __name__ == '__main__':
    app.run(debug=True)
