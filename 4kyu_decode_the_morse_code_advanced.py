def decode_bits(bits):
    bits = bits.strip('0')
    unit = 0
    for bit in bits:
        if bit != '0':
            unit += 1
        else:
            break


    count = 1
    for i in range(1, len(bit)):
        if bits[i] == bits[i - 1]:
            count += 1
        else:
            if count < unit :
                unit = count
                count = 1
            else:
                count = 1
    morse_code = ''


    words = bits.split('0' * 7 * unit )
    for word in words :
        characters = word.split('0' * 3 * unit )
        for character in characters :
            signs = character.split('0' * unit )
            for sign in signs :
                if sign == '1' * 3 * unit :
                    morse_code += '-'
                else:
                    morse_code += '.'
            morse_code += ' '
        morse_code += '   '
    return morse_code


def decode_morse(morse_code):
    morse_code.strip()
    result = ''
    characters = morse_code.split(' ')
    for character in characters :
        if character != '':
            result += MORSE_CODE[character]
        else:
            result += ' '
    return ' '.join(result.split())
