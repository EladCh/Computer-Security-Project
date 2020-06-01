import PySimpleGUI as sg
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Sizer
from bloom_test import test_bloom_filter
from bloomfilter import BloomFilter
from password_strength_rules import password_rules
# All the stuff inside your window. This is the PSG magic code compactor...
# https://pysimplegui.readthedocs.io/en/latest/#layouts
# https://opensource.com/article/18/8/pysimplegui
# https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

sg.theme('LightGray1')   # Add a little color to your windows

main_title_col = [sg.Text('     Bloom Filter & Password Strength Checker' , size=(40, 1), font=("Helvetica", 20))]

col1 = Column([
    [Frame('New Password:',
            [[Button('Insert new password', enable_events= True), InputText(key='-NEW-PASSWORD-' ,size=(15, 1))],
            [Button('Show complete password strength analysis', enable_events= True)]],)]
])

col2 = Column([
    [Frame('Bloom Filter:',
            [[Text('K'), sg.InputText(key='-K-', size=(5, 1)), Text('N'), InputText(key='-N-',size=(5, 1)), Button('Enter', enable_events= True)],
            [Text('Current filter params: K={} N={}'.format(5,7))],
            [Text('Insert Counter: {}'.format(0)), Text('Marked Bits Counter: {}'.format(0))]],)]
])

col3 = Column([
    [Frame('Password Check:', 
            [[Text('Insert password to check'), InputText(key='-PASSWORD-TO-CHECK-',size=(15, 1))],
            [Text('In Dictionary 1: {}'.format('NO')), Text('In Dictionary 2: {}'.format('NO'))],
            [Button('Test check of previously known dictionary', enable_events= True)]],)]
])

col4 = Column([
    [Frame('Filter Visualization', [[Text('Full visual of the actual filter')]],)]
])

layout = [main_title_col,[col1, col2], [col3, col4]]

# Create the Window
main_window = Window('Double Bloom Filter & Password Strength Checker', layout)

# 10-million-password-list from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
# read it once in the begining and than use it to prevent those passwords
password_corpus = [line.strip() for line in open("files/10-million-password-list-top-1000000.txt", 'r')]

# set default values of the bfilters.
# TODO remove default and raise a popup if an action is done before the settings
bloomf_1 = BloomFilter(10,0.01)
bloomf_2 = BloomFilter(10,0.01)

# Event Loop to process "events"
while True:             
    event, values = main_window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enter':
        # update the bfilers. note that the action erases the previous filters with all the data (TODO add a pop up saying that)
        max_num_of_items = int(values['-K-'])
        max_fp_rate = float(values['-N-'])
        bloomf_1 = BloomFilter(max_num_of_items,max_fp_rate)
        bloomf_2 = BloomFilter(max_num_of_items,max_fp_rate)
    elif event == 'Insert new password':
        try:
            # first make sure that the password doesnt apear in the password_corpus
            if values['-NEW-PASSWORD-'] not in password_corpus:
                _a, _b, _c, popup_msg, ruls_violation = password_rules(values['-NEW-PASSWORD-'])
                if ruls_violation == True:
                    sg.PopupError(popup_msg)
                    continue
                # check that the password is new and not in one of the filters
                if (not bloomf_1.check(values['-NEW-PASSWORD-']) and not bloomf_2.check(values['-NEW-PASSWORD-'])):
                    # check if insertion to bfilt 1 is allowed
                    if bloomf_1.is_add_allowed():
                        bloomf_1.add(values['-NEW-PASSWORD-'])
                    # else check if insertion to bfilt 2 is allowed
                    elif bloomf_2.is_add_allowed():
                        bloomf_2.add(values['-NEW-PASSWORD-'])
                    # this is a new password and the two bfilters are full- add the password to the filter with the minimum
                    # element number. if they are equal enter to bfilter 1
                    else:
                        if bloomf_1.get_element_count() <= bloomf_2.get_element_count():
                            bloomf_1.add(values['-NEW-PASSWORD-'])
                        else:
                            bloomf_2.add(values['-NEW-PASSWORD-'])
            else:
                sg.PopupError("Plese enter non trivial password\nFor guidness check out the analysis")
        except: # invalid data or mistake
            pass
    elif event == 'Show complete password strength analysis':
        try:
            weaknesses, strengths, score, popup_msg, ruls_violation = password_rules(values['-NEW-PASSWORD-'])

            headings = ['property', 'exists']   

            subject_pass_to_analysis_col = [sg.Text('                     Password: {}'.format(values['-NEW-PASSWORD-']), size=(30, 1), font=("Helvetica", 25))]               

            strength_analysis_col = Column([
                [Frame('Password Strength Parameters',
                        [
                        [sg.Table(values=strengths[1:][:], max_col_width=60, headings=headings,
                        # background_color='light blue',
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='left',
                        num_rows=7,
                        alternating_row_color='lightyellow',
                        key='-STRENGTH-TABLE-',
                        row_height=35,
                        )]
                        ],
                )]
            ])

            weaknesses_analysis_col = Column([
                [Frame('Password weaknesses Parameters',
                        [
                        [sg.Table(values=weaknesses[1:][:], max_col_width=60, headings=headings,
                        # background_color='light blue',
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='left',
                        num_rows=7,
                        alternating_row_color='lightyellow',
                        key='-STRENGTH-TABLE-',
                        row_height=35,
                        )]
                        ],
                )]
            ])

            ok_col = [Button('Ok', enable_events= True),
                      Text("Password strength: {}".format(score))] 

            analysis_layout = [subject_pass_to_analysis_col,[weaknesses_analysis_col ,strength_analysis_col], ok_col]
            
            analisys_window = Window('Password Strength Analysis', analysis_layout)

            while True:             
                ana_event, ana_values = analisys_window.read()
                if ana_event == sg.WIN_CLOSED or ana_event == 'Ok':
                    break
            analisys_window.close()
            pass
        except: # invalid data or mistake
            pass
    elif event == 'Test check of previously known dictionary':
        try:
            test_bloom_filter(int(values['-K-']),float(values['-N-']))
        except: # invalid data or mistake
            pass

main_window.close()