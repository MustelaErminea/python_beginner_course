# Без дуплетов. Играем в кости. Правила следующие:
#
# 1. Кидаем пару костей.
# 2. Складываем количество выпавших чисел и прибавляем к общему кол-ву очков
# 3. Повторяем пункты 1 и 2 трижды.
# 4. Если выпадает дуплет (на обоих костях одно и то же число), то кол-во очков обнуляется и последующие броски
# не считаются.
#
# Задание:
#
# Напишите функцию calc_dice_scores принимающую список кортежей и, возвращающую общее кол-во очков.
#
# Примеры вызовов и ожидаемый результат.
#
# ```
# calc_dice_scores ([(1, 2), (3, 4), (5, 6)]) -> 21
# calc_dice_scores ([(1, 1), (5, 6), (6, 4)]) -> 0
# calc_dice_scores ([(4, 5), (4, 5), (4, 5)]) -> 21
# ```
#
# Всегда передаются три кортежа по два элемента в каждом.
from typing import Tuple, List


def calc_dice_scores(dices: List[Tuple[int, int]]) -> int:
    amount: int = 0

    for dice in dices:
        if dice[0] == dice[1]:
            return 0
        else:
            amount += dice[0] + dice[1]

    return amount


def main():
    print(f"calc_dice_scores([(1, 2), (3, 4), (5, 6)]) -> {calc_dice_scores([(1, 2), (3, 4), (5, 6)])}")
    print(f"calc_dice_scores([(1, 1), (5, 6), (6, 4)]) -> {calc_dice_scores([(1, 1), (5, 6), (6, 4)])}")
    print(f"calc_dice_scores([(4, 5), (4, 5), (4, 5)]) -> {calc_dice_scores([(4, 5), (4, 5), (4, 5)])}")


if __name__ == "__main__":
    main()
