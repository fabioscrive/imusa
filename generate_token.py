#!/usr/bin/env python3
"""Genera token.json criptato per I-Musa"""
import base64
import json
import sys

def xor_encrypt(text, key):
    encrypted = bytearray()
    key_bytes = key.encode('utf-8')
    for i, char in enumerate(text.encode('utf-8')):
        encrypted.append(char ^ key_bytes[i % len(key_bytes)])
    return base64.b64encode(encrypted).decode('utf-8')

def main():
    if len(sys.argv) != 2:
        print("Uso: python generate_token.py ghp_tuo_token")
        sys.exit(1)

    token = sys.argv[1]
    key = "imusa2026"
    encrypted = xor_encrypt(token, key)

    data = {
        "v": "1.0",
        "data": encrypted,
        "key_hint": "imusa2026",
        "repo": "fabioscrive/imusa",
        "branch": "main"
    }

    print(json.dumps(data, indent=2))
    print("\n--- Salva questo come token.json su GitHub ---")

if __name__ == "__main__":
    main()
