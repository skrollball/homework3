
def ticket_total(count, price=12):# Считаем полную цену без скидок (по умолчанию билет стоит 12)
    return count * price
def final_price(count, is_school_group=False):# Считаем итоговую цену (если школьники — делаем скидку 25%)
    total = ticket_total(count)
    if is_school_group:
        return total * 0.75 
    return total
print(final_price(3))
print(final_price(4, is_school_group=True))
print(ticket_total(2, price=15))

