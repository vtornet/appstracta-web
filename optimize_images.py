#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para optimizar imágenes de Appstracta Web.
Requiere: pip install Pillow

Uso:
    cd E:\Appstracta\Web
    python optimize_images.py
"""

import os
import sys
from pathlib import Path

# Configurar codificación para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow no esta instalado.")
    print("   Instalalo con: pip install Pillow")
    exit(1)

def optimize_png(input_path, quality=85):
    """Optimiza un PNG reduciendo su tamaño."""
    img = Image.open(input_path)

    # Convertir a RGB si tiene canal alpha (transparencia)
    if img.mode in ('RGBA', 'LA', 'P'):
        img.save(input_path, optimize=True, compress_level=9)
    else:
        img.save(input_path, optimize=True, compress_level=9)

    return os.path.getsize(input_path)

def create_webp(input_path, quality=85):
    """Crea una version WebP de la imagen."""
    img = Image.open(input_path)
    webp_path = input_path.with_suffix('.webp')

    # Mantener transparencia si la hay
    if img.mode == 'RGBA':
        img.save(webp_path, 'WEBP', quality=quality, method=6, lossless=False)
    else:
        img.save(webp_path, 'WEBP', quality=quality, method=6)

    return os.path.getsize(webp_path)

def main():
    web_dir = Path(__file__).parent
    originals = []

    # Encontrar todas las imagenes PNG y JPG
    for pattern in ['*.png', '*.jpg', '*.jpeg']:
        originals.extend(web_dir.glob('**/' + pattern))

    print(f"[+] Encontradas {len(originals)} imagenes para optimizar\n")

    total_saved = 0

    for img_path in originals:
        if img_path.name.endswith('.webp'):
            continue

        rel_path = img_path.relative_to(web_dir)
        original_size = os.path.getsize(img_path)
        original_kb = original_size / 1024

        print(f"[*] {rel_path}")
        print(f"    Original: {original_kb:.1f} KB")

        # Optimizar PNG/JPG
        new_size = optimize_png(img_path)
        optimized_kb = new_size / 1024
        saved = original_size - new_size

        # Crear version WebP
        webp_size = create_webp(img_path)
        webp_kb = webp_size / 1024
        webp_saved = original_size - webp_size

        print(f"    [OK] Optimizado: {optimized_kb:.1f} KB (ahorrado {saved/1024:.1f} KB)")
        print(f"    [WEBP] WebP: {webp_kb:.1f} KB (ahorrado {webp_saved/1024:.1f} KB)\n")

        total_saved += saved

    print(f"[!] Espacio total ahorrado: {total_saved/1024:.1f} KB")

if __name__ == '__main__':
    main()
