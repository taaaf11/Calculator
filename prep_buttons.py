buttons = ['C', 'AC', ' ', '+',
           '7', '8',  '9', '-',
           '4', '5',  '6', 'x',
           '1', '2',  '3', '÷',
           '0', '.',  ' ', '=']

for button in buttons:
    if button == '.':
        print(f"button_point = ft.ElevatedButton(text='{button}', )")
        continue
    if button == ' ':
        print(f"button_empty = ft.ElevatedButton(text='{button}', )")
        continue
    print(f"button_{button} = ft.ElevatedButton(text='{button}', on_click=lambda _)")
   