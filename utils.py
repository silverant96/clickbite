import sys


def parse_args():
    """Простой парсер аргументов"""
    args = sys.argv[1:]

    result = {
        'files': [],
        'report': 'clickbite',
        'delimiter': ',',  # разделитель по умолчанию
    }

    i = 0
    while i < len(args):
        if args[i] == '--files':
            i += 1
            while i < len(args) and not args[i].startswith('--'):
                result['files'].append(args[i])
                i += 1
        elif args[i] == '--report':
            i += 1
            if i < len(args) and not args[i].startswith('--'):
                result['report'] = args[i]
                i += 1
        elif args[i] == '--delimiter':
            i += 1
            if i < len(args) and not args[i].startswith('--'):
                delim = args[i]
                if delim == 'tab':
                    result['delimiter'] = '\t'
                elif delim == 'comma':
                    result['delimiter'] = ','
                else:
                    result['delimiter'] = delim
                i += 1
        else:
            i += 1

    return result