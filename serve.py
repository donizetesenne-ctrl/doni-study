"""
Servidor local para testar o PWA no celular.

Uso:
    python serve.py

Depois acesse no celular (mesmo WiFi):
    http://IP-DO-SEU-PC:8080

Para instalar como app no celular:
    1. Abra no Chrome/Edge do celular
    2. Menu (3 pontinhos) → "Instalar app" ou "Adicionar à tela inicial"
    3. Pronto! Ícone aparece na home.

Para HTTPS (necessário em alguns navegadores):
    Use ngrok ou cloudflare tunnel (veja README).
"""

import http.server
import socketserver
import socket
import os

PORT = 8080

# Mudar para pasta do PWA
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PWAHandler(http.server.SimpleHTTPRequestHandler):
    """Handler com MIME types corretos para PWA."""
    
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.json': 'application/json',
        '.js': 'application/javascript',
        '.webmanifest': 'application/manifest+json',
    }

    def end_headers(self):
        # Headers necessários para PWA/Service Worker
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()


def get_local_ip():
    """Pega o IP local da máquina na rede."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"


if __name__ == "__main__":
    ip = get_local_ip()
    
    with socketserver.TCPServer(("", PORT), PWAHandler) as httpd:
        print(f"""
╔══════════════════════════════════════════════════════════╗
║  📸 Doni Study PWA — Servidor Local                     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  🖥️  PC:      http://localhost:{PORT}                    ║
║  📱 Celular: http://{ip}:{PORT}              ║
║                                                          ║
║  Certifique-se que PC e celular estão na mesma WiFi!     ║
║                                                          ║
║  Para instalar no celular:                               ║
║  1. Abra o link acima no Chrome/Edge                     ║
║  2. Menu → "Instalar app" ou "Adicionar à tela inicial" ║
║  3. Pronto! Aparece como app na home.                    ║
║                                                          ║
║  Ctrl+C para parar o servidor.                           ║
╚══════════════════════════════════════════════════════════╝
""")
        httpd.serve_forever()
