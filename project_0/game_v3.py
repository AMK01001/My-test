import numpy as np

def game_core_v3(number: int = 1 ) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 #Создаём переменную-счётчик для учёта количества попыток
    # Задаёте нижнюю и верхнюю границы поиска
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число
 
    #Создаёте вечный цикл
    while True:
        count += 1 #увеличиваете количество попыток
        
        # определяете предположение как половину отрезка
        if predict_number > number:
            # если число больше предположения, нижнюю границу переодределяем как предположение.
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        # Иначе если число меньше предположения, верхнюю границу переодределяем как предположение
        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        
        # Иначе (что значит предположение рано число) прерываем цикл
        else:
            break  # конец игры, выход из цикла

    return count #Возвращаем значение количество попыток

print(f'Количество попыток: {game_core_v3()}')