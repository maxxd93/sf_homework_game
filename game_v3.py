import numpy as np

lowest_number = 1 #Нижняя граница диапозона
highest_number = 101 #Верхняя граница диапозона
size = 1000 #Количество повторений
def guess_number(number:int=1) -> int:
    """Функция угадывания числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    mid_number = int(np.mean([lowest_number, highest_number])) #Среднее арифмитическое диапозона угадывания
    step = int(np.ceil(mid_number/2)) #Шаг изменения ср. ар. диапазона угадывания
    while True:
        count += 1
        if number < mid_number:
            mid_number = mid_number - step
            step = int(np.ceil(step/2))
        elif number > mid_number:
            mid_number = mid_number + step
            step = int(np.ceil(step/2))
        else:
            break
    return(count) #Выход из цикла при угадывании

def score_game(guess_number) -> int:
    """Функция запуска функции определенное число раз

    Args:
        guess_number (_type_): Функция угадывания числа

    Returns:
        int: Среднее количество попыток
    """
    count_ls = [] #Список количества угадываний
    np.random.seed(1) #Фиксированный SEED
    random_array = np.random.randint(lowest_number, highest_number, size) #Загадываемые числа
    for number in random_array:
        count_ls.append(guess_number(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
#RUN
if __name__ == '__main__':
    score_game(guess_number)