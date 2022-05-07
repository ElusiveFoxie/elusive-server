# elusive-server 2.0 by ElusiveFox
```
usage: elusive-server.py [-h] [-m MODE] [-p PORT] [-rh RESPONSE_HEADER] [-rhf RESPONSE_HEADERS_FILE]

simple python3 http/https server with ability to set custom request headers

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  http or https (default: http)
  -p PORT, --port PORT  port number (default: 8080)
  -rh RESPONSE_HEADER, --response-header RESPONSE_HEADER
                        custom response header (header_name:header_value)
  -rhf RESPONSE_HEADERS_FILE, --response-headers-file RESPONSE_HEADERS_FILE
                        custom response headers file (file path)

example1: simple-server.py -m http -p 8080 -rhf headers.txt
example2: simple-server.py -m https -p 8443 -rh "test1:test2"
```
you can generate your own server.pem with the following command:
```
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```
  
