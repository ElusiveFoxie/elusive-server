#!/usr/bin/python3

import sys
import http.server
import socketserver
import ssl
import argparse

# generate server.pem with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

parser = argparse.ArgumentParser(description='simple http/https server with ability to set custom request headers')

# mode
parser.add_argument('-m','--mode', type=str,help='http or https (default: http)')

# port
parser.add_argument('-p','--port', type=str,help='port number (default: 8080)')

# custom header
parser.add_argument('-rh', '--response-header', type=str,help='custom response header (header_name:header_value)')

# custom header file
parser.add_argument('-rhf', '--response-headers-file', type=str,help='custom response headers file (file path)')

PORT = 8080
MODE = 'http'

if __name__ == '__main__':

    if len(sys.argv) == 1:
        parser.print_help()
        print(
            '''\nexample1: simple-server.py -m http -p 8080 -rhf headers.txt\nexample2: simple-server.py -m https -p 8443 -rh "test1:test2"''')
        parser.exit()

    args = parser.parse_args()
    headers = {}

    if args.response_header:
        headers[args.response_header.split(":",1)[0]] = args.response_header.split(":",1)[1]

    if args.response_headers_file:
        with open(args.response_headers_file, 'r') as fd:
            headers = dict(line.rstrip().split(":",1) for line in fd)

    class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            for key, value in headers.items():
                self.send_header(key, value)
            http.server.SimpleHTTPRequestHandler.end_headers(self)

    try:
        MODE = args.mode
        PORT = int(args.port)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
            if (MODE == "https"):
                httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
            print("serving " + MODE + " at port", PORT)
            httpd.serve_forever()
    except IndexError:
        print(help)