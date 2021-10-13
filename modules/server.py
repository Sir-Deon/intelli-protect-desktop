from http.server import HTTPServer, BaseHTTPRequestHandler
import modules.configs as configs
import json


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        s = json.dumps(data, indent=4, sort_keys=True)
        id = json.loads(s)
        with open('user.txt', 'r+') as file:
            file.write(id['userId'])
        self.send_response(200)


print(f"server listening on {configs.app_port}")
httpd = HTTPServer(('localhost', configs.app_port), Serv)
httpd.serve_forever()
