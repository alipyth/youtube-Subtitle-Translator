#pip install deep_translator
from deep_translator import GoogleTranslator


def read_sbv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def translate_text(text, target_language='fa'):
    translator = GoogleTranslator(target=target_language)
    translated = translator.translate(text)
    return translated


def write_sbv(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def translate_sbv(input_file, output_file, target_language='fa'):
    lines = read_sbv(input_file)
    translated_lines = []

    for line in lines:
        if '-->' in line or line.strip() == '':
            translated_lines.append(line)
        else:
            translated_text = translate_text(line.strip(), target_language)
            translated_lines.append(translated_text + '\n')

    write_sbv(output_file, translated_lines)


# Example usage:
input_sbv = 'captions.sbv'
output_sbv = 'translated_output.sbv'
translate_sbv(input_sbv, output_sbv, 'fa')
