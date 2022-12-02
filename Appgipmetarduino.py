from turtle import color
from smbus import SMBus
import PySimpleGUI as sg
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

#djgddf
drank_layout = [
    [sg.Button('Wodka energy')],
    [sg.Button('Wodka cola')],
    [sg.Button('Mojito')],
    [sg.Button('Cola')],
    [sg.Button('Energy')],

    ]

editdrankje_layout = [
    
    [sg.Text("Je hebt een keuze uit onderstaande punten:")],
    [sg.Button('-Cola')],
    [sg.Button('-Rum')],  
    [sg.Button('-Tonic')],
    [sg.Button('-Fanta')],
    [sg.Button('-Ijsblokjes')],
    [sg.Button('toevoegen',button_color='Red')]
    ]
information = []
headings = ['Jouw bestelling:']

bestelling_layout = [
    
    [sg.Text(text_color ='black',background_color = 'white')],
    [sg.Table(values = information, headings = headings, max_col_width=35,
    auto_size_columns=True,
    justification = 'right',
    key = '-TABLE-',
    row_height = 35)],
    [sg.Button('Submit'),sg.Button('Stop')]
   
    
 ]





tab_group = [
        [sg.TabGroup(
            [[
                    sg.Tab('Drankjes', drank_layout, background_color = 'white'),
                    sg.Tab('Maak je drankje',editdrankje_layout, background_color = 'white'),
                    sg.Tab('Bestelling',bestelling_layout, background_color = 'white')]],


                    tab_location = 'centertop',
                    title_color = 'White', 
                    tab_background_color = 'Purple',
                    selected_title_color='Black', 
                    selected_background_color='White'),
                    sg.Button('Exit',button_color='Red')
            ]]



window = sg.Window('Robotender',tab_group)

while True:
    event,values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-Cola':
        information.append("cola")
        window['-TABLE-'].update(values=information)
        
    if event == 'Wodka energy':
        information.append('Wodka energy')
        window['-TABLE-'].update(values=information)
    
    if event == 'Wodka cola':
        information.append("Wodka cola")
        window['-TABLE-'].update(values=information)
        
    if event == 'Mojito':
        information.append("Mojito")
        window['-TABLE-'].update(values=information)
        
    if event == 'Cola':
        information.append("Cola")
        window['-TABLE-'].update(values=information)
        
    if event == 'Energy':
        information.append("Energy")
        window['-TABLE-'].update(values=information)


        
    
    
    
    if event == 'Submit':
        ledstate = 1
        
        if ledstate == 1:
            bus.write_byte(addr, 0x1)
            
    if event == 'Stop':
        ledstate = 0
        
        if ledstate == 0:
            bus.write_byte(addr, 0x0)
            
            
                    
window.close()  

