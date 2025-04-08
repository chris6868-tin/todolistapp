def save_data(data):
    with open("data.txt", "w", encoding="utf8") as f:
        for item in data:
            f.write(item + "\n")

def load_data():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            data = [line.strip() for line in file]
        return data    
    except FileNotFoundError:
        print("Dữ liệu không có trước, To do list rỗng")