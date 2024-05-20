def reverse_complement(pattern: str) -> str:
    """Returns the reverse complement of a DNA pattern."""
    translation_table = str.maketrans("ACGT", "TGCA")
    translated_string = pattern.translate(translation_table)
    return translated_string[::-1]
