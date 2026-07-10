from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import socket

class DualStackServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6

if __name__ == '__main__':
    server = DualStackServer(('::', 8080), SimpleHTTPRequestHandler)
    print("Serving dual-stack HTTP on port 8080 (IPv4 & IPv6 localhost) ...")
    server.serve_forever()
