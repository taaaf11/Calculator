from buttons import *
import flet as ft


def main(page):
    page.title = 'Calculator'
    page.window_width = 310
    page.window_height = 350
    
    page.theme_mode = 'light'
    
    entry_label = ft.TextField(value='0',read_only=True)
    row_1 = ft.Row([button_C, button_AC, button_empty, button_add])
    row_2 = ft.Row([button_7, button_8, button_9, button_sub])
    row_3 = ft.Row([button_4, button_5, button_6, button_mul])
    row_4 = ft.Row([button_1, button_2, button_3, button_div])
    row_5 = ft.Row([button_0, button_point, button_empty, button_equals])
    
    view = ft.Column([
        entry_label,
        row_1,
        row_2,
        row_3,
        row_4,
        row_5
    ])
    
    page.add(view)


if __name__ == '__main__':
    ft.app(target=main)
