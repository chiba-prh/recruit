import http.server
import socketserver
import os

os.chdir("/Users/yokouchi/Desktop/recruit")

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8080), handler) as httpd:
    print("Serving on port 8080")
    httpd.serve_forever()
