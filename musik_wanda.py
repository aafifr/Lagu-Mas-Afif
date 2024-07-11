import sys
from time import sleep

def print_lyrics():
    lines = [
        ("lembut tutur katamu, merdu tawamu", 0.08),
        ("parasmu yang menawan", 0.07),
        ("buat diriku tak bisa lupa...", 0.10),
        ("dari banyaknya insan di dunia", 0.08),
        ("mengapa dirimu yang aku sangka?", 0.06),
    ]
    delays = [1.5, 2,5, 8.5, 8.5, 3.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()
