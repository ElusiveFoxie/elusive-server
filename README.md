# elusive-server 3.0 by ElusiveFox
```
usage: elusive-server.py [-h] [-m MODE] [-p PORT] [-rh RESPONSE_HEADER] [-rhf RESPONSE_HEADERS_FILE]
                         [-cf CERTIFICATE_FILE]

simple http/https server with ability to set custom request headers

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  http or https (default: http)
  -p PORT, --port PORT  port number (default: 8080)
  -rh RESPONSE_HEADER, --response-header RESPONSE_HEADER
                        custom response header (header_name:header_value)
  -rhf RESPONSE_HEADERS_FILE, --response-headers-file RESPONSE_HEADERS_FILE
                        custom response headers file (file path)
  -cf CERTIFICATE_FILE, --certificate-file CERTIFICATE_FILE
                        custom certificate file (default: ./server.pem)

example1: elusive-server.py -m http -p 8080 -rhf headers.txt
example2: elusive-server.py -m https -p 8443 -rh "test1:test2"
example3: elusive-server.py -m https -p 8080 -rhf .\headers.txt -cf ".\custom_server.pem"
```
you can generate your own server.pem with the following command:
```
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```
  
