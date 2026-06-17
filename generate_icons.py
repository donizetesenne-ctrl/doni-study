"""Gera ícones PNG para o PWA a partir de HTML Canvas."""
import os

# Criar um HTML que gera os ícones via canvas e salva
# Alternativa mais simples: usar um PNG placeholder de 1 cor

def create_simple_png(size, filepath):
    """Cria um PNG simples sem dependências externas.
    Usa formato PNG mínimo com cor sólida + texto simulado."""
    
    import struct
    import zlib
    
    # PNG com fundo #1a1a2e (azul escuro)
    width = height = size
    
    # Pixel RGBA
    bg = (26, 26, 46, 255)  # #1a1a2e
    accent = (233, 69, 96, 255)  # #e94560
    
    # Criar imagem simples (fundo com círculo central)
    rows = []
    center = size // 2
    radius = size // 3
    
    for y in range(height):
        row = b'\x00'  # filter byte
        for x in range(width):
            # Distância do centro
            dx = x - center
            dy = y - center
            dist = (dx*dx + dy*dy) ** 0.5
            
            if dist < radius:
                # Círculo rosa/vermelho no centro
                row += bytes(accent)
            else:
                # Fundo
                row += bytes(bg)
        rows.append(row)
    
    raw_data = b''.join(rows)
    
    # Comprimir
    compressed = zlib.compress(raw_data)
    
    # Construir PNG
    def make_chunk(chunk_type, data):
        chunk = chunk_type + data
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xffffffff)
    
    # IHDR
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)  # 8bit RGBA
    
    png = b'\x89PNG\r\n\x1a\n'
    png += make_chunk(b'IHDR', ihdr_data)
    png += make_chunk(b'IDAT', compressed)
    png += make_chunk(b'IEND', b'')
    
    with open(filepath, 'wb') as f:
        f.write(png)
    
    print(f"  ✅ Criado: {filepath} ({size}x{size})")


if __name__ == "__main__":
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    os.makedirs(icons_dir, exist_ok=True)
    
    print("📸 Gerando ícones do PWA...\n")
    create_simple_png(192, os.path.join(icons_dir, "icon-192.png"))
    create_simple_png(512, os.path.join(icons_dir, "icon-512.png"))
    print("\n✅ Ícones gerados! Agora pode rodar: python serve.py")
