# import threading
# import time
# import logging
# import socket
# from http.server import BaseHTTPRequestHandler, HTTPServer

# # Configure logging
# logging.basicConfig(filename="interactions.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# # ==========================
# # 1. HTTP Server for Logging HTTP Interactions
# # ==========================
# class RequestLogger(BaseHTTPRequestHandler):
#     def do_GET(self):
#         client_ip = self.client_address[0]
#         log_entry = f"HTTP Request from {client_ip}: {self.path}"
#         logging.info(log_entry)
#         print(log_entry)

#         # Respond to the request
#         self.send_response(200)
#         self.send_header("Content-type", "text/plain")
#         self.end_headers()
#         self.wfile.write(b"HTTP request logged!")

# def start_http_server(port=9999):
#     server = HTTPServer(("192.168.29.230", port), RequestLogger)
#     print(f"[*] HTTP Server started on port {port}")
#     server.serve_forever()

# # ==========================
# # 2. DNS Server for Logging DNS Interactions
# # ==========================
# def start_dns_server(host="192.168.29.230", port=53):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((host, port))
#     print("[*] DNS Server started on port 53 (Requires root)")

#     while True:
#         data, addr = sock.recvfrom(512)  # Receive DNS query
#         domain = data[12:-4].decode(errors="ignore")  # Extract domain name
#         log_entry = f"DNS Request from {addr[0]} for {domain}"
#         logging.info(log_entry)
#         print(log_entry)

# # ==========================
# # 3. Log Monitor (Real-time Log Fetcher)
# # ==========================
# def monitor_logs():
#     print("[*] Monitoring interactions...\n")

#     while True:
#         try:
#             with open("interactions.log", "r") as log_file:
#                 logs = log_file.readlines()
#                 if logs:
#                     print("[*] Logs:")
#                     print("".join(logs))
#             time.sleep(1)  # Fetch logs every 5 seconds
#         except KeyboardInterrupt:
#             print("\n[*] Stopping log monitoring...")
#             break

# # ==========================
# # 4. Running All Services Simultaneously
# # ==========================
# if __name__ == "__main__":
#     # Start HTTP Server in a thread
#     http_thread = threading.Thread(target=start_http_server, daemon=True)
#     http_thread.start()

#     # Start DNS Server in a thread (Requires root)
#     dns_thread = threading.Thread(target=start_dns_server, daemon=True)
#     dns_thread.start()

#     # Start Log Monitoring in the main thread
#     monitor_logs()
import threading
import time
import logging
import socket
import ssl
import binascii
from http.server import BaseHTTPRequestHandler, HTTPServer

# ==========================
# 1. Configure Logging
# ==========================
logging.basicConfig(filename="interactions.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# ==========================
# 2. HTTP/HTTPS Server for Logging Requests
# ==========================
class RequestLogger(BaseHTTPRequestHandler):
    def log_request_data(self):
        """ Logs request data including headers and raw payload """
        client_ip = self.client_address[0]
        log_entry = f"Request from {client_ip}: {self.command} {self.path}\nHeaders:\n{self.headers}"
        logging.info(log_entry)
        print(log_entry)

    def do_GET(self):
        self.log_request_data()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Request logged!")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""
        decoded_data = post_data.decode(errors="ignore")
        log_entry = f"POST Data: {decoded_data}"
        logging.info(log_entry)
        print(log_entry)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST request logged!")

def start_http_server(port=9999):
    server = HTTPServer(("192.168.29.230", port), RequestLogger)
    print(f"[*] HTTP Server started on port {port}")
    server.serve_forever()


import ssl

def start_https_server(port=9443, cert="server.pem", key="server.pem"):
    server = HTTPServer(("0.0.0.0", port), RequestLogger)

    # Create an SSL context instead of using ssl.wrap_socket()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert, keyfile=key)

    server.socket = context.wrap_socket(server.socket, server_side=True)
    
    print(f"[*] HTTPS Server started on port {port} with SSL")
    server.serve_forever()

# ==========================
# 3. DNS Server for Logging DNS Requests
# ==========================
def parse_dns_query(data):
    """ Extract domain name from binary DNS query """
    domain_parts = []
    i = 12  # Start at byte 12 (standard DNS query structure)
    while i < len(data):
        length = data[i]
        if length == 0:
            break
        domain_parts.append(data[i+1:i+1+length].decode(errors="ignore"))
        i += length + 1
    return ".".join(domain_parts)

def start_dns_server(host="192.168.29.230", port=53):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print("[*] DNS Server started on port 53 (Requires root)")

    while True:
        data, addr = sock.recvfrom(512)  # Receive DNS query
        domain = parse_dns_query(data)  # Extract domain name
        log_entry = f"DNS Request from {addr[0]} for {domain}\nRaw Data: {binascii.hexlify(data).decode()}"
        logging.info(log_entry)
        print(log_entry)

# ==========================
# 4. Log Monitor (Real-time Log Fetcher)
# ==========================
def monitor_logs():
    print("[*] Monitoring interactions...\n")

    last_position = 0
    while True:
        try:
            with open("interactions.log", "r") as log_file:
                log_file.seek(last_position)
                logs = log_file.readlines()
                last_position = log_file.tell()

                if logs:
                    print("[*] New Logs:")
                    print("".join(logs))

            time.sleep(2)  # Check logs every 2 seconds
        except KeyboardInterrupt:
            print("\n[*] Stopping log monitoring...")
            break

# ==========================
# 5. Generate Self-Signed SSL Certificate (One-time Setup)
# ==========================
def generate_ssl_certificate(cert="server.pem", key="server.pem"):
    import subprocess
    print("[*] Generating self-signed SSL certificate...")
    subprocess.run([
        "openssl", "req", "-new", "-x509", "-keyout", key, "-out", cert,
        "-days", "365", "-nodes", "-subj", "/CN=localhost"
    ], check=True)

# ==========================
# 6. Running All Services Simultaneously
# ==========================
if __name__ == "__main__":
    # Generate SSL certificate if not present
    import os
    if not os.path.exists("server.pem"):
        generate_ssl_certificate()

    # Start HTTP Server
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    # Start HTTPS Server
    https_thread = threading.Thread(target=start_https_server, daemon=True)
    https_thread.start()

    # Start DNS Server
    dns_thread = threading.Thread(target=start_dns_server, daemon=True)
    dns_thread.start()

    # Start Log Monitoring
    monitor_logs()
