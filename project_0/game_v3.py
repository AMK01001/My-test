import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 #Создаём переменную-счётчик для учёта количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    predict = np.random.randint(1, 21) # предполагаемое число
    
    
    #Теперь пишем цикл, который будет позволять вводить и угадывать числа
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

   
print(f'Количество попыток: {game_core_v3()}')