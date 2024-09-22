import os
index = 0
while index <= 1000:
    new_dir = f"Петя гей {index}"
    parent_dir = rf"C:\Users\vladm\Documents\Для_пети"#C:\Users\vladm\Documents\Для пети
    path = os.path.join(parent_dir, new_dir)
    os.mkdir(path)
    print(f'Директория {new_dir} создана')
    index += 1