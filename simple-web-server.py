import http.server
import socketserver
import urllib.parse
port = 8080

class handler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        par = urllib.parse.parse_qsl(urllib.parse.urlparse(self.path).query)
        s = " OK {"+str(par) + "}"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('X-ACK', s)
        self.end_headers()

        print(self.client_address)
        print(self.requestline)
        print(self.path)
        
server_address = ('', 8080)
httpd = socketserver.TCPServer(server_address, handler)
print("starting http server..")
httpd.serve_forever()
