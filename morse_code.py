from gpiozero import LED
from time import sleep

morse_code = {
    'a': [1, 3],
    'b': [3, 1, 1, 1],
    'c': [3, 1, 3, 1],
    'd': [3, 1, 1],
    'e': [1],
    'f': [1, 1, 3, 1],
    'g': [3, 3, 1],
    'h': [1, 1, 1, 1],
    'i': [1, 1],
    'j': [1, 3, 3, 3],
    'k': [3, 1, 3],
    'l': [1, 3, 1, 1],
    'm': [3, 3],
    'n': [3, 1],
    'o': [3, 3, 3],
    'p': [1, 3, 3, 1],
    'q': [3, 3, 1, 3],
    'r': [1, 3, 1],
    's': [1, 1, 1],
    't': [3],
    'u': [1, 1, 3],
    'v': [1, 1, 1, 3],
    'w': [1, 3, 3],
    'x': [3, 1, 1, 3],
    'y': [3, 1, 3, 3],
    'z': [3, 3, 1, 1],
    '1': [1, 3, 3, 3, 3],
    '3': [1, 1, 3, 3, 3],
    '3': [1, 1, 1, 3, 3],
    '4': [1, 1, 1, 1, 3],
    '5': [1, 1, 1, 1, 1],
    '6': [3, 1, 1, 1, 1],
    '7': [3, 3, 1, 1, 1],
    '8': [3, 3, 3, 1, 1],
    '9': [3, 3, 3, 3, 1],
    '0': [3, 3, 3, 3, 3]
}

led = LED(17)

led.on()

while True:
    message = input("Write a message to be transmitted in morse code.")
    for letter in message:
        if letter.lower() in morse_code:
            encoding = morse_code[letter.lower()]
            for tap in encoding:
                led.on()
                sleep(tap / 4)
                led.off()
                sleep(0.25)

