from ui import *

max_rows = 5
data = {
    "A": "aaaaa",
    "B": "bbbbb",
    "C": "ccccc",
    "D": "ddddd",
}
generate_text = "Gerar texto"
clean_text = "Limpar"
copy_text = "Copiar"
dropdown_keyword = "dropdown"
textarea_key = "textarea"

window = MainWindow(generate_text, clean_text, copy_text, max_rows, list(data.keys()),
                    dropdown_keyword, textarea_key)
while True:
    event, dic = window.read()
    if event == generate_text:
        print("set text to a variable and show it")
    if event == clean_text:
        print("clean variable and update")
    if event == copy_text:
        print("copy and visual feedback, popup?")
    if event == sg.WIN_CLOSED:
        neglected_window.close()
        break
# if __name__ == '__main__':
#     print('PyCharm')

# TODO
# read csv for data
# add function to buttons
# consult about theme
# dynamic row count?

