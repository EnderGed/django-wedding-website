import http.server
import socketserver

class myHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(301)
        new_path = '%s%s'%('http://rauan-and-bartek.grinvest.pl', self.path)
        self.send_header('Location', new_path)
        self.end_headers()

PORT = 5544
handler = socketserver.TCPServer(("", PORT), myHandler)
print("serving at port 5544")
handler.serve_forever()
