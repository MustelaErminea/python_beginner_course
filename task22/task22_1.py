# 1. Клиент покупает кофе в кафе. За каждые 6 чашек, 1 чашка даётся в качестве
# бонуса.
# Задача: запросить у пользователя кол-во чашек на покупку, вычислить
# полагающееся кол-во бонусных чашек кофе и вывести это число на консоль.

cup_count: int = int(input("Введите количество чашек для покупки: "))
bonus_cup = int(cup_count / 6)
print(f"Количество бонусных чашек: {bonus_cup}")
