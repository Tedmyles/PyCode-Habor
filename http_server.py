import http.server
import socketserver
import requests

PORT = 8080  # The port your reverse proxy will run on

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.copy_request_to_backend()
        
    def do_POST(self):
        self.copy_request_to_backend()
        
    def do_PUT(self):
        self.copy_request_to_backend()
        
    def do_DELETE(self):
        self.copy_request_to_backend()
        
    def copy_request_to_backend(self):
        url = f'http://localhost:5500{self.path}' #Port of the site you want to expose to the internet
        method = self.command.lower()
        
        # Forward the request to the React app
        response = requests.request(method, url, headers=self.headers, data=self.rfile.read(int(self.headers.get('Content-Length', 0))))
        
        # Send the response back to the client
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.content)

with socketserver.TCPServer(("", PORT), Proxy) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
