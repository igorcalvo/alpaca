def get_dropdown_key(key_word: str, row: int, column: int) -> str:
    number_of_columns = 3
    return f"{key_word}_{row * number_of_columns + column}"
