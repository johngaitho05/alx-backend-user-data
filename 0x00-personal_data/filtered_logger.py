import re


def filter_datum(fields, redaction, message, separator):
    """obfuscate a log datum"""
    return re.sub(
        f'(?:(?<=^)|(?<={separator}))({"|".join(fields)}){separator}',
        f'{redaction}{separator}', message)
