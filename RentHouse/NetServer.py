from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8000
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting NetServer on port: " + str(httpd.server_port))
httpd.serve_forever()
