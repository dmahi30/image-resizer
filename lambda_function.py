import base64, io, json
from PIL import Image

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        img = Image.open(io.BytesIO(base64.b64decode(body["image"])))
        width = int(body.get("width", 300))
        height = int(body.get("height", 300))
        fmt = body.get("format", "JPEG").upper()

        if fmt == "JPEG":
            img = img.convert("RGB")
        img.thumbnail((width, height))  # keeps aspect ratio

        buf = io.BytesIO()
        img.save(buf, format=fmt)
        out = base64.b64encode(buf.getvalue()).decode()

        return {"statusCode": 200,
                "body": json.dumps({"image": out, "format": fmt,
                                    "size": img.size})}
    except Exception as e:
        return {"statusCode": 400, "body": json.dumps({"error": str(e)})}