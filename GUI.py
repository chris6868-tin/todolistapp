import function
import FreeSimpleGUI as sg

label = sg.Text("Nhập vào một việc cần làm: ")
input_box = sg.InputText(tooltip="Nhập")
add_button = sg.Button("Thêm")


window = sg.Window('My TO-DO app', layout=[[label], [input_box, add_button]])
window.read()
window.close()