import PySimpleGUI as sg
from logic import *

sg.theme('DarkBlue2')

FONTS = {
    "cat": ("Cascadia Mono", 13, "bold"),
    "ckb": ('Consolas', 11),
    "btn": ("Verdana", 9, "bold"),
    "pop": ("Arial", 11, "bold")
}


def DropdownRow(row: int, combo_values: list, dropdown_keyword: str) -> list:
    dropdown_size = 15
    dropdown_padding = 5
    dropdown_font = FONTS["ckb"]
    dropdown_spacing = 25
    return [
        sg.Combo(values=combo_values,
                 # default_value='>',
                 key=get_dropdown_key(dropdown_keyword, row, 0),
                 size=dropdown_size,
                 pad=dropdown_padding,
                 auto_size_text=True,
                 font=dropdown_font,
                 change_submits=True,
                 enable_events=True,
                 ),
        sg.Text(" " * dropdown_spacing),
        sg.Combo(values=combo_values,
                 # default_value='>',
                 key=get_dropdown_key(dropdown_keyword, row, 1),
                 size=dropdown_size,
                 pad=dropdown_padding,
                 auto_size_text=True,
                 font=dropdown_font,
                 change_submits=True,
                 enable_events=True
                 ),
    ]


def CreateLayout(generate_text: str, clean_text: str, copy_text: str, max_rows: int, combo_values: list,
                 dropdown_keyword: str, textarea_key: str) -> list:
    button_size = 15
    button_padding = 50
    buttons_layout = [
        sg.Button(generate_text,
                  font=FONTS["btn"],
                  size=button_size,
                  pad=((button_padding, 0), (button_padding // 2, 0))
                  ),
        sg.Push(),
        sg.Button(clean_text,
                  font=FONTS["btn"],
                  size=button_size,
                  pad=((0, 0), (button_padding // 2, 0))
                  ),
        sg.Push(),
        sg.Button(copy_text,
                  font=FONTS["btn"],
                  size=button_size,
                  pad=((0, button_padding), (button_padding // 2, 0))
                  )
    ]

    dropdown_layout = [DropdownRow(row, combo_values, dropdown_keyword) for row in range(max_rows)]

    text_area = [
        sg.Multiline(size=(400, 20),
                     key=textarea_key,
                     pad=((button_padding, button_padding), (button_padding // 2, button_padding // 2))
                     )
    ]

    window_layout = [dropdown_layout, buttons_layout, text_area]
    return window_layout


def MainWindow(generate_text: str, clean_text: str, copy_text: str, max_rows: int, combo_values: list,
               dropdown_keyword: str, textarea_key: str):
    layout = CreateLayout(generate_text, clean_text, copy_text, max_rows, combo_values,
                          dropdown_keyword, textarea_key)
    return sg.Window(title="Alpaca",
                     layout=layout,
                     use_custom_titlebar=True,
                     titlebar_icon="alpaca.png",
                     size=(500, 500),
                     element_justification='c')
