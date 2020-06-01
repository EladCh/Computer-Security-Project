import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
"""

sg.theme('Dark Red')

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]


weaknesses = [['All letters:', 'true'],['All digits','true'],['Repeated characters:', 'true'],['Consecutive uppercase letters','true'],
            ['Consecutive lowercase letters:', 'true'],['Consecutive digits','true'],['Sequential letters:', 'true'],['Sequential digits','true']]

strengthes = [['Length:', 0],['Upper case letters',0],['Lower case letters:', 0],['Digits',0],
            ['Symbols:', 0],['Digits & Symbols in the middle',0]]

headings2 = ['property', 'exists']                    
# ------ Window Layout ------
layout = [[sg.Table(values=strengthes[1:][:], max_col_width=5, headings=headings2,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table',
                    )]
          ]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,
                   # font='Helvetica 25',
                   )

# ------ Event Loop ------
while True:
    print(1)
    event, values = window.read()
    #print(event, values)
    # if event == sg.WIN_CLOSED:
    #     break
    # if event == 'Double':
    #     for i in range(len(data)):
    #         data.append(data[i])
    #     window['-TABLE-'].update(values=data)
    # elif event == 'Change Colors':
    #     window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

window.close()