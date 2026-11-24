def analyze_scores(*scores):
    count = len(scores)
    if count == 0:# Если баллы не передали, сразу возвращаем нули
        return 0, 0, 0
    total = sum(scores)
    mid = total / count
    return total, count, mid
def print_report(team_name, **info):# Печатаем название команды и все переданные данные о ней
    print("Команда:", team_name)
    for key, value in info.items():
        print(key, ":", value)
print(analyze_scores(8, 10, 7, 9))# Проверяем на разных наборах баллов
print(analyze_scores(5, 5))
print(analyze_scores())
print()  # пустая строка для красоты
print_report("Комета", coach="Иванов", city="Минск")# Выводим отчет по команде
