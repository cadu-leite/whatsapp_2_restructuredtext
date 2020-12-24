import re
import os

CWD = r'<basepath>'

REGEX_DATESENDER = r'^(?:[0-3][0-9])\/(?:[0-1][0-9])\/(?:[0-9]{2,4})(?:\s([0-2][0-9]:[0-6][0-9]))*(\s-\s[ \w]*:)*'
REGEX_IMAGE = r'(IMG-\d{8}-WA\d{4}.jpg)\s*(\(\b.*\))'  # find `IMG-20201027-WA0021.jpg (arquivo anexado)`
REGEX_AUDIO = r'(PTT-\d{8}-WA\d{4}.opus)\s*(\(\b.*\))'  # find  `PTT-20201027-WA0026.opus (arquivo anexado)`
FILE_PATH = f'{CWD}/Conversa do WhatsApp com Marcelo Cunha.txt'


def treat_rst_mixup(text):

    return text.replace('---', '- - -')


def format_audio(text):
    regcomp = re.compile(REGEX_AUDIO)
    mat = regcomp.search(text)
    rst_audio = ''
    if mat:
        audio_name = mat.groups()[0]
        rst_audio = f'\n\t.. warning:: Audio file {audio_name}'
    return rst_audio


def format_image(text):
    regcomp = re.compile(REGEX_IMAGE)
    mat = regcomp.search(text)
    rst_img = ''
    if mat:
        img_name = mat.groups()[0]
        img_alt = '- '.join(mat.groups())
        rst_img = f'\n\t.. image:: {CWD}/{img_name}\n\t\t:alt: {img_alt}\n\t\t:width: 300px'

    return rst_img


def extract_date_sender(text):
    '''
    ... for a file containng this lines ...

    11/11/2020 10:59 - Author Name: message message
    message message

    return a tuple (<date sender>, <message>)

    => ('11/11/2020 10:59 - Author Name:', 'message message')
    => (None, 'message message')

    '''
    date_sender = ''
    message = text.lstrip()  # .replace('\n', '')

    recomp = re.compile(REGEX_DATESENDER)
    mat = recomp.search(message)

    if mat is not None:
        poss = mat.span()  # position tuple

        part_date_sender = mat.group().lstrip()
        part_message = message[poss[1]:]  # extract date & sender
        part_message = part_message.lstrip()

        date_sender = f'\n\n{part_date_sender}\n'
        message = part_message
    return (f'{date_sender}', f'    {message}')


def main():
    outputfile = open('output.rst', 'w')

    with open(FILE_PATH, 'r') as whatsappfile:
        line = None
        line_num = 0
        while line != '':
            line = whatsappfile.readline()
            line_num += 1
            line = treat_rst_mixup(line)
            texts = ''.join(extract_date_sender(line))
            texts += format_image(line)
            texts += format_audio(line)
            outputfile.write(''.join(texts))

    outputfile.close()


if __name__ == '__main__':
    main()
