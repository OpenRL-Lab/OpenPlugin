import json

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS = {}


@app.get("/ikun_image")
async def get_ikun_image():
    ikun_image_url = request.url_root+ "ikun.png"
    return quart.Response(response=json.dumps({"message":ikun_image_url,"status":"success"}), status=200)

@app.get("/ikun.png")
async def plugin_logo():
    filename = 'ikun.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        ROOT_URL = request.url_root
        if ROOT_URL.endswith('/'):
            ROOT_URL = ROOT_URL[:-1]
        text = text.replace("{% ROOT_URL %}", ROOT_URL)
        print(request.url_root)
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
