import base64, io, json
from PIL import Image
from lambda_function import lambda_handler

def test_resize():
    img = Image.new("RGB", (800, 600), "red")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    event = {"body": json.dumps({
        "image": base64.b64encode(buf.getvalue()).decode(),
        "width": 200, "height": 200, "format": "PNG"})}
    res = lambda_handler(event, None)
    assert res["statusCode"] == 200
    assert json.loads(res["body"])["size"][0] == 200