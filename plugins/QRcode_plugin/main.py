import random
import string
import json
import io

import quart
import quart_cors
from quart import request
from openplugin.template import JSONTemplate, YAMLTemplate
import segno

json_template = JSONTemplate("./ai-plugin.json")
yaml_template = YAMLTemplate("./openapi.yaml")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

def generate_str(N=10) -> str:
    data = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    print("data:",data)
    return data

@app.get("/qrcode_image")
async def get_qr_code():
    qr_image_url = request.url_root+ "qr.png"
    return quart.Response(response=json.dumps({"message":qr_image_url,"status":"success"}), status=200)

@app.get("/qr.png")
async def qr_png():
    buff = io.BytesIO()
    segno.make(generate_str(), micro=False) \
        .save(buff, kind='png', scale=4, dark='darkblue',
              data_dark='#474747', light='#efefef')
    buff.seek(0)
    return await quart.send_file(buff, mimetype='image/png')

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/ai-plugin.json")
@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    text = json_template.render(request)
    return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    text = yaml_template.render(request)
    return quart.Response(text, mimetype="text/yaml")

@app.get("/")
@app.get("/info.json")
async def show_info():
    with open("info.json", "r") as f:
        text = f.read()
    return quart.Response(text, mimetype="text/json")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
