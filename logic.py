from re import split as re_split

def get_dropdown_key(key_word: str, number_of_rows: int, row: int, column: int) -> str:
    number_of_columns = 2
    # return f"{key_word}_{row * number_of_columns + column}"
    return f"{key_word}_{row + column * number_of_rows}"

def get_dropdown_text(key_word: str, number_of_rows:int, row: int, column: int) -> str:
    key = get_dropdown_key(key_word, number_of_rows, row, column)
    result = key.replace(f"{key_word}_", "")
    result = int(result) + 1
    result = str(result)
    return result if int(result) >= 10 else f"0{result}"

def human_sort(list_to_sort: list) -> None:
    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        '''
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        '''
        return [atoi(c) for c in re_split(r"(\d+)", text)]
    list_to_sort.sort(key=natural_keys)

def read_text_from_dic(values_dic: dict, dic: dict, dropdown_keyword: str) -> str:
    keys = [k for k in dic.keys() if dropdown_keyword in k]
    human_sort(keys)

    result = ""
    for k in keys:
        if dic[k] != "":
            result += values_dic[dic[k]]

    return result
