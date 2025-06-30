from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 8000
server = HTTPServer(('', port), SimpleHTTPRequestHandler)
print(f"Serving on http://localhost:{port}")
server.serve_forever()