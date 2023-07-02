import json

import quart
import quart_cors
from quart import request
from openplugin.template import JSONTemplate, YAMLTemplate

json_template = JSONTemplate("./ai-plugin.json")
yaml_template = YAMLTemplate("./openapi.yaml")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.get("/ikun_image")
async def get_ikun_image():
    ikun_image_url = request.url_root+ "ikun.png"
    return quart.Response(response=json.dumps({"message":ikun_image_url,"status":"success"}), status=200)

@app.get("/ikun.png")
async def plugin_logo():
    filename = 'ikun.png'
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

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
