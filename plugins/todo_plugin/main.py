import json

import quart
import quart_cors
from quart import request
from openplugin.template import JSONTemplate, YAMLTemplate

json_template = JSONTemplate("./ai-plugin.json")
yaml_template = YAMLTemplate("./openapi.yaml")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS = {}

@app.post("/todos/<string:username>")
async def add_todo(username):
    request = await quart.request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append("test:"+request["todo"])
    return quart.Response(response='OK', status=200)

@app.get("/todos/<string:username>")
async def get_todos(username):
    return quart.Response(response=json.dumps(_TODOS.get(username, [])), status=200)

@app.delete("/todos/<string:username>")
async def delete_todo(username):
    request = await quart.request.get_json(force=True)
    todo_idx = request["todo_idx"]
    # fail silently, it's a simple plugin
    if 0 <= todo_idx < len(_TODOS[username]):
        _TODOS[username].pop(todo_idx)
    return quart.Response(response='OK', status=200)

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
