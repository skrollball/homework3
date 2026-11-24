def average_grade(a, b, c):# Считаем среднее из трех оценок
    return (a + b + c) / 3
def grade_message(average):# Выбираем текст в зависимости от балла
    if average >= 4.5:
        return "Отлично"
    if average >= 3.5:
        return "Хорошо"
    return "Нужно повторить материал"
res1 = average_grade(5, 4, 5)# Проверяем на пятерках и четверке
print(round(res1, 2))  # округляем до 2 знаков после запятой
print(grade_message(res1))
res2 = average_grade(3, 4, 3)# Проверяем на тройках и четверке
print(round(res2, 2))
print(grade_message(res2))
