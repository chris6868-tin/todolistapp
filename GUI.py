import function
import FreeSimpleGUI as sg
import time

sg.theme('Black')

label_time = sg.Text("", key='lbtime')
label = sg.Text("Nhập vào một việc cần làm: ")
input_box = sg.InputText(tooltip="Nhập", key="todo")
add_button = sg.Button("Thêm")
list_box = sg.Listbox(values=function.load_data(), key='todo_edit', 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Sửa")
complete_button = sg.Button("Hoàn thành")
exit_button = sg.Button("Thoát")

window = sg.Window('My TO-DO app', 
                   layout=[ [label_time],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))

while True:
    todo = function.load_data()

    event, value = window.read(timeout=200)
    if event == "Thoát" or event == sg.WIN_CLOSED:
        break

    window['lbtime'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Thêm":
            todo.append(value['todo'])
            function.save_data(todo)
            window['todo_edit'].update(values=todo)
        case "todo_edit":
            window['todo'].update(value['todo_edit'][0])
        case "Sửa":
            if value['todo_edit']:
                print(todo.index(value['todo_edit'][0]))
                todo[todo.index(value['todo_edit'][0])] = value['todo']
                function.save_data(todo)
                window['todo_edit'].update(values=todo)
            else:
                sg.popup("Chọn 1 todo!", font=('Helvetica', 20))
        case "Hoàn thành":
            if value['todo_edit']:
                todo_completed = value['todo_edit'][0]
                todo.remove(todo_completed)
                function.save_data(todo)
                window['todo_edit'].update(values=todo)
                window['todo'].update(value='')
            else:
                sg.popup("Chọn 1 todo!", font=('Helvetica', 20))
    

window.close()