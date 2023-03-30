from ui import MainWindow
from pyperclip import copy as copy_to_clipboard
from logic import read_text_from_dic, xlsx_to_dic
from PySimpleGUI import WIN_CLOSED

max_rows = 5
xlsx_filename = 'assets/dados.xlsx'

generate_text = "Gerar texto"
clean_text = "Limpar"
copy_text = "Copiar"
dropdown_keyword = "dropdown"
textarea_key = "textarea"

data = xlsx_to_dic(xlsx_filename)
text = ""

window = MainWindow(generate_text, clean_text, copy_text, max_rows, list(data.keys()),
                    dropdown_keyword, textarea_key)
while True:
    event, dic = window.read()
    if event == generate_text:
        text = read_text_from_dic(data, dic, dropdown_keyword)
        window[textarea_key].update(text)
    if event == clean_text:
        window.close()
        text = ""
        window = MainWindow(generate_text, clean_text, copy_text, max_rows, list(data.keys()), dropdown_keyword,
                            textarea_key)
    if event == copy_text:
        copy_to_clipboard(text)
    # if dropdown_keyword in event:
    #     print("dropdown\n", dic)
    if event == WIN_CLOSED:
        window.close()
        break
# if __name__ == '__main__':
#     print('PyCharm')

# TODO
# consult about theme
