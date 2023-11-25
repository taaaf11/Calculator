import flet as ft


def main(page):
    page.title = 'Calculator'
    page.window_width = 310
    page.window_height = 350
    
    page.theme_mode = 'light'
    
    button_C = ft.ElevatedButton(text='C')
    button_AC = ft.ElevatedButton(text='AC')
    button_empty = ft.ElevatedButton(text=' ')
    button_add = ft.ElevatedButton(text='+')
    button_sub = ft.ElevatedButton(text='-')
    button_mul = ft.ElevatedButton(text='x')
    button_div = ft.ElevatedButton(text='÷')
    button_equals = ft.ElevatedButton(text='=')
    
    button_7 = ft.ElevatedButton(text='7')
    button_8 = ft.ElevatedButton(text='8')
    button_9 = ft.ElevatedButton(text='9')
    
    button_4 = ft.ElevatedButton(text='4')
    button_5 = ft.ElevatedButton(text='5')
    button_6 = ft.ElevatedButton(text='6')
    
    button_1 = ft.ElevatedButton(text='1')
    button_2 = ft.ElevatedButton(text='2')
    button_3 = ft.ElevatedButton(text='3')
    
    button_0 = ft.ElevatedButton(text='0')
    button_point = ft.ElevatedButton(text='.')
    button_empty = ft.ElevatedButton(text=' ')
    
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
