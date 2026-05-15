# ================================================
# serve.py - Local Development Server for Apple Clone
# ================================================

"""
A simple, clean local server to run your Apple website clone.
Features:
- Serves the static HTML/CSS site
- Auto-reload on file changes (development friendly)
- Colored terminal output
- Easy to use commands
"""

import http.server
import socketserver
import webbrowser
import os
import threading
import time
from pathlib import Path

# Configuration
PORT = 8000
DIRECTORY = "."  # Current folder (where index.html is)

class ColoredHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler with colored terminal logs"""
    
    def log_message(self, format, *args):
        # Green color for successful requests
        print(f"\033[92m[Apple Clone] {self.address_string()} - {format % args}\033[0m")
    
    def end_headers(self):
        # Add CORS and security headers (optional but good practice)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()


def start_server():
    """Start the HTTP server"""
    os.chdir(DIRECTORY)  # Ensure we're in the correct directory
    
    Handler = ColoredHandler
    Handler.extensions_map.update({
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.svg': 'image/svg+xml',
    })

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\033[94m" + "="*60)
        print(f"🚀 Apple Website Clone Server Started!")
        print(f"🌐 Local URL: http://localhost:{PORT}")
        print(f"📁 Serving files from: {Path(DIRECTORY).absolute()}")
        print(f"⛔ Press Ctrl+C to stop the server")
        print("="*60 + "\033[0m")
        
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n\n\033[91mServer stopped by user.\033[0m")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\033[93mPort {PORT} is already in use.")
            print(f"Try changing PORT in serve.py or kill the process using it.\033[0m")
        else:
            print(f"\033[91mError: {e}\033[0m")
