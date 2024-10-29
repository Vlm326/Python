with open(fr"C:\Users\vladm\Downloads\26.txt", 'r') as file:
    lines = file.readlines()

n = int(lines[0])

items = {}

for line in lines[1:]:
    article, weight, status = map(int, line.split())
    if article not in items:
        items[article] = {'общая_масса': 0, 'количество': 0, 'на_складе': 0, 'отгружено': 0}
    
    items[article]['общая_масса'] += weight
    items[article]['количество'] += 1
    if status == 1:
        items[article]['на_складе'] += 1
    else:
        items[article]['отгружено'] += 1

# Вычисление средней массы с обычным делением
total_weight_sum = sum(item['общая_масса'] for item in items.values())
total_count = sum(item['количество'] for item in items.values())
average_weight = total_weight_sum / total_count

# Отбор только тяжёлых товаров с учетом точного деления
heavy_items = {k: v for k, v in items.items() if v['общая_масса'] / v['количество'] > average_weight}

# Инициализация лидера
leader_article = None
leader_shipped = float('-inf')
leader_weight = float('-inf')
leader_on_stock = float('inf')

# Выбор лидера по условиям задачи
for article, data in heavy_items.items():
    current_weight = data['общая_масса'] / data['количество']
    
    if (data['отгружено'] > leader_shipped or
        (data['отгружено'] == leader_shipped and current_weight > leader_weight) or
        (data['отгружено'] == leader_shipped and current_weight == leader_weight and data['на_складе'] < leader_on_stock)):
        
        leader_article = article
        leader_shipped = data['отгружено']
        leader_weight = current_weight
        leader_on_stock = data['на_складе']

# Округление для итоговой массы
total_shipped_weight = round(leader_shipped * leader_weight)
print(total_shipped_weight, leader_on_stock)
