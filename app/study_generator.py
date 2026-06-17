# ============================================================
# Study Generator — Script principal
# ============================================================
# Uso: python study_generator.py imagem.jpg
#      python study_generator.py --all
# ============================================================

import sys
import os
import base64
from pathlib import Path
from datetime import datetime

from config import load_config
from ai_interpreter import interpret_image
from markdown_builder import build_study_material


def encode_image_base64(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_image_mime(image_path: str) -> str:
    ext = Path(image_path).suffix.lower()
    return {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
            ".gif": "image/gif", ".webp": "image/webp", ".bmp": "image/bmp"}.get(ext, "image/jpeg")


def process_image(image_path: str, output_dir: str, config: dict) -> str:
    print(f"\n{'='*50}")
    print(f"📸 Processando: {Path(image_path).name}")
    print(f"{'='*50}")

    image_b64 = encode_image_base64(image_path)
    mime_type = get_image_mime(image_path)

    print("  → Enviando para IA...")
    analysis = interpret_image(image_b64, mime_type, config)

    if not analysis:
        print("  ❌ Erro: IA não retornou análise.")
        return None

    filename = Path(image_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{filename}_{timestamp}.md")

    markdown_content = build_study_material(analysis, Path(image_path).name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"  ✅ Salvo: {output_path}")
    return output_path


def main():
    config = load_config()
    base_dir = Path(__file__).parent.parent
    images_dir = base_dir / "imagens"
    output_dir = base_dir / "output"
    images_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    if len(sys.argv) < 2:
        print("""
╔════════════════════════════════════════════════╗
║  📸 STUDY GENERATOR                           ║
╠════════════════════════════════════════════════╣
║  python study_generator.py <imagem>           ║
║  python study_generator.py --all              ║
╚════════════════════════════════════════════════╝
""")
        return

    if sys.argv[1] == "--all":
        exts = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}
        images = [f for f in images_dir.iterdir() if f.suffix.lower() in exts]
        if not images:
            print(f"❌ Nenhuma imagem em: {images_dir}")
            return
        results = [process_image(str(img), str(output_dir), config) for img in sorted(images)]
        print(f"\n🎉 {sum(1 for r in results if r)}/{len(images)} materiais gerados.")
    else:
        image_path = sys.argv[1]
        if not os.path.isabs(image_path) and not os.path.exists(image_path):
            image_path = str(images_dir / image_path)
        if not os.path.exists(image_path):
            print(f"❌ Não encontrado: {image_path}")
            return
        process_image(image_path, str(output_dir), config)


if __name__ == "__main__":
    main()
