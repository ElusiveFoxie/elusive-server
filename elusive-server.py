#!/usr/bin/python3

import sys
import http.server
import socketserver
import ssl
import argparse
import logging

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

# certificate file
parser.add_argument('-cf', '--certificate-file', type=str,help='custom certificate file (default: ./server.pem)')

PORT = 8080
MODE = 'http'
CERTFILE = './server.pem'

if __name__ == '__main__':

    if len(sys.argv) == 1:
        parser.print_help()
        print(
            '''\nexample1: elusive-server.py -m http -p 8080 -rhf headers.txt\nexample2: elusive-server.py -m https -p 8443 -rh "test1:test2"\nexample3: elusive-server.py -m https -p 8080 -rhf .\headers.txt -cf ".\custom_server.pem"''')
        parser.exit()

    args = parser.parse_args()
    headers = {}
    

    if args.response_header:
        headers[args.response_header.split(":",1)[0]] = args.response_header.split(":",1)[1]

    if args.response_headers_file:
        with open(args.response_headers_file, 'r') as fd:
            headers = dict(line.rstrip().split(":",1) for line in fd)
    
    if args.certificate_file:
        CERTFILE = args.certificate_file

    class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
        server_version = "NameYouWant"
        sys_version = ""
             
        def end_headers(self):
            for key, value in headers.items():
                self.send_header(key, value)
            http.server.SimpleHTTPRequestHandler.end_headers(self)
        
        def do_POST(self):
            self.send_response(200)
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            print(post_data)
            self.end_headers()
        
        def do_OPTIONS(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
       
    try:
        MODE = args.mode
        PORT = int(args.port)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
            if (MODE == "https"):
                httpd.socket = ssl.wrap_socket(httpd.socket, certfile=CERTFILE, server_side=True)
            print("serving " + MODE + " at port", PORT)
            httpd.serve_forever()
    except IndexError:
        print(help)
