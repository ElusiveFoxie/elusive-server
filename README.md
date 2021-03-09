# simple-server 1.0 by ElusiveFox
```
usage: simple-server.py [-m] [-p]

-m, --mode 	http or https (default: http)
-p, --port  	port number
```
you can generate your own server.pem with the following command:
```
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```
  
