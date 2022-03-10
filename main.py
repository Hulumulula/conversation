"""Обе функции выполнены в виде рекурсии, обходим двоичное дерево."""


def analyse(boxs=None, stack=None, energy=0):
    # Чтобы переменная не была изменчива, избегаем ошибок
    stack = stack or []
    # Создаём массив всех выгружаемых ящиков, чтобы немного упростить их погрузку
    if energy == 0:
        global unload
        unload = []
        stack = []
        for j in boxs:
            if j[0].lower() == "выгрузить":
                unload.append(j[1])

    for box in boxs:
        box = list(box)
        if len(stack) == 0:         # Если склад пустой, то заносим первым ящик
            stack.append(box[1])
            energy = 1 + energy
        elif box[0].lower() == "принять" and box[1] not in unload:      # Если принимаем ящик, который не выгружается,
            stack.insert(0, box[1])                                     # пихаем его сразу на вход.
            energy = 1 + energy                                         # Так как ящики забираем только на выходе,
        else:                                                           # он будет только мешатся при выгрузке
            if box[0].lower() == "принять":         # Погружаем все выгружаемые в будущем ящики
                st1 = stack.copy()                  # Дальше проверяем что будет меньше энергозатратно,
                st2 = stack.copy()                  # поставить ящик на вход или сразу на выход.
                st1.insert(0, box[1])
                st2.append(box[1])
                energy = 1 + energy
                boxs = boxs[boxs.index(tuple(box))+1:]
                en1 = analyse(boxs, st1, energy)
                en2 = analyse(boxs, st2, energy)
                if en1 >= en2:
                    energy = en2
                else:
                    energy = en1
                return energy
            elif box[0].lower() == "выгрузить":  # Выгружаем ящики
                x = stack.index(box[1])
                energy = ((len(stack)-x-1)*2+1) + energy
                del stack[x]
    return energy


def calculate(m, n, p, day=1, bonuses=0, level=1, maxb=0):
    bonus1 = bonuses + p[level-1]
    lvl1 = level + 1
    if lvl1 > n:                        # Просто смотрим до конца дерева и считаем бонусы.
        lvl1 = 1                        # Максимальный сохраняем и сравниваем.
    d1 = day + 1
    bonus2 = bonuses
    lvl2 = 1
    d2 = day + 1

    if d1 <= m:
        bon1 = calculate(m, n, p, day=d1, bonuses=bonus1, level=lvl1, maxb=maxb)    # Если нажали в этот день
        bon2 = calculate(m, n, p, day=d2, bonuses=bonus2, level=lvl2, maxb=maxb)    # Если не нажали в этот день
        maxb = max(maxb, bon1, bon2)
        return maxb

    else:
        if bonus1 > maxb:
            maxb = bonus1
            return maxb

        else:
            return maxb


if __name__ == "__main__":
    print(analyse([('принять', 1), ('принять', 2), ('выгрузить', 1), ('принять', 3), ('принять', 4), ('выгрузить', 3)]))
    print(calculate(5, 4, [5, 7, 1, 1]))
