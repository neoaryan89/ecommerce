import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import model.product

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send.response(200)
        self.send_header('Content-type' , 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        headphones = model.product.Product()
        headphones._set_type("simple")
        headphones.set_name("headphones")
        json.dump(headphones,self.wfile)

#run server
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('',port)
    httpd = server_class(server_address, handler_class)
    print "Starting httpd..."
    httpd.serve_forever()

if __name__ == "__main__":
    run()   