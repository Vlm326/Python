import os
for x in range(0,1000):
    index = 0
    while index <= 500:
        new_dir = f"Петя гей {index}"
        parent_dir = rf"C:\Users\vladm\Documents\Для_пети\Петя гей {x}"
        path = os.path.join(parent_dir, new_dir)
        os.mkdir(path)
        print(f'Директория {new_dir} создана')
        index += 1
def main():
    print("nigger")