import os
import http.server as server
import hashlib

HOSTNAME = 'localhost'
PORT = 8000

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """
    Add PUT & POST requests
    """

    def do_GET(self):
        """
        Send back a message to say that files can be uploaded with PUT & POST

        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        reply_body = 'Get the md5 hash of an uploaded file:  Use curl -XPUT or -XPOST'
        self.wfile.write(reply_body.encode('utf-8'))

    def do_PUT(self):
        """
        Hash a file following a PUT, I couldn't figure out how to do it without saving the file.
        """
        filename = os.path.basename(self.path)

        file_length = int(self.headers['Content-Length'])
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        with open(filename, 'rb') as hashable_file:
            bytes = hashable_file.read()  # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest();
            #print(readable_hash)
        self.send_response(201, 'Hashed')
        self.end_headers()
        reply_body = 'Hashed "%s"\n' % readable_hash
        self.wfile.write(reply_body.encode('utf-8'))
        os.remove(filename)

    def do_POST(self):
        self.do_PUT()


if __name__ == '__main__':
    #server.test(HandlerClass=HTTPRequestHandler)
    server_class = server.HTTPServer

    httpd = server_class((HOSTNAME, PORT), HTTPRequestHandler)
    print("Server Started on:", HOSTNAME, PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
