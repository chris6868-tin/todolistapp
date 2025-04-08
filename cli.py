import function

data = function.load_data()

print("Chào mừng đến với chương trình quản lý todo-list!")
print("Chức năng: Thêm, Xem, Sửa, Xóa, Thoát")

while True:
    user_choice = input("Nhap lua chon: ").lower()
    match user_choice:
        case "thêm":
            data.append(input("Nhập nhiệm vụ mới: "))
        case "xem":
            for index, item in enumerate(data):
                print(f"{index+1} - {item}\n")
        case "sửa":
            try:
                edit_index = int(input("Nhập việc đã hoàn thành (vị trí): ")) - 1
                if 0<=edit_index < len(data):
                    data[edit_index] = input("Nhập nhiệm vụ thay thế: ")
                    function.save_data()
                else:
                    print("Vị trí không hợp lệ!")
            except ValueError:
                print("Lỗi, Bạn không nhập một số hợp lệ!")
        case "xóa":
            try:
                del_index = int(input("Nhập việc đã hoàn thành (vị trí): "))
                if 0<=edit_index < len(data):
                    data.pop(del_index-1)
                    print("Đã hoàn thành nhiệm vụ")
                else:
                    print("Vị trí không hợp lệ!")
            except ValueError:
                print("Lỗi, Bạn không nhập một số hợp lệ!")
        case "thoát":
            break
function.save_data(data)
print("Byebye! Good luck and see you tomorow!")