from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Experiment-1</title>
</head>
<body style="background-color: beige;text-align: center;color:brown; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;font-size: medium;">
    <h1 style="background-color: blanchedalmond;color:burlywood;font-weight: 200;font-size:xx-large;">List Of Protocols In TCP/IP Model</h1>
     <h2 style="background-color:blanchedalmond;">Application Layer : HTTP,FTP,DNS,Telnet<br>
         Transport Layer : TCP & UDP<br>
        Network Layer: IPV4/IPV6<br>
        Link Layer : Ethernet</h2>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()