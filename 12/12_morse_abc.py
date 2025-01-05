# 12_morse_abc.py

alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

alphabet_reverse = {value: key for key, value in alphabet.items()}


class Morse:
    def encode(self, text):
        morse_code = ''
        for char in text:
            morse_code += alphabet[char] + ' '
        return morse_code
    
    def decode(self, morse):
       normal_text = ''
       morse = morse.split(' ')
       for char in morse:
            if char in alphabet_reverse:
               normal_text += alphabet_reverse[char]
            else:
               normal_text += ' '
       return normal_text

morse = Morse()
print(morse.encode('SOME TEXT HERE'))


print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))


# zde je tajná zakodáváná zpráva pro vás
print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))
