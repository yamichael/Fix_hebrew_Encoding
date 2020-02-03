def shift_bytes(xbytes):
    value = int.from_bytes(xbytes[:2], 'big')
    value += 5104
    return value.to_bytes((value.bit_length() + 7) // 8, 'big')


encoding = 'UTF-8'


def fix_phrase(phrase):
    ignore_set = {'\''}  # add more?
    words = phrase.split()
    new_phrase = []
    for word in words:
        shifted_word = bytearray()
        for letter in word:
            if letter in ignore_set:
                shifted_word.append(letter.encode(encoding)[0])
                continue
            bytes_origin = letter.encode(encoding)
            shifted_letter = shift_bytes(bytes_origin)
            shifted_word.append(shifted_letter[0])
            shifted_word.append(shifted_letter[1])
        translated = shifted_word.decode(encoding)
        new_phrase.append(translated)

    return " ".join(new_phrase)


def create_dict():
    phrase = 'אבגדהוזחטיכךלמםנןסעפףצץקרשת'
    phrase_gibrish = 'àáâãäåæçèéëêìîíðïñòôóöõ÷øùú'
    gibrish_to_hebrew = dict()
    for heb, gib in zip(phrase, phrase_gibrish):
        gibrish_to_hebrew[gib] = heb
    return gibrish_to_hebrew


def fast_fix(phrase):
    gibrish_to_hebrew = {'à': 'א', 'á': 'ב', 'â': 'ג', 'ã': 'ד', 'ä': 'ה', 'å': 'ו', 'æ': 'ז', 'ç': 'ח', 'è': 'ט',
                         'é': 'י', 'ë': 'כ', 'ê': 'ך', 'ì': 'ל', 'î': 'מ', 'í': 'ם', 'ð': 'נ', 'ï': 'ן', 'ñ': 'ס',
                         'ò': 'ע', 'ô': 'פ', 'ó': 'ף', 'ö': 'צ', 'õ': 'ץ', '÷': 'ק', 'ø': 'ר', 'ù': 'ש', 'ú': 'ת'}

    translated = ""
    for letter in phrase:
        if letter in gibrish_to_hebrew:
            translated += gibrish_to_hebrew[letter]
        else:
            translated += letter
    return translated
