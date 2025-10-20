import random
import time
from tqdm import tqdm # установка библиотеки в PowShell


def generate_numbers_with_progress():
    n = 100  # кол-во чисел
    max_value = 1_000  # макс
    output_file = "numbers_with_progress.txt"  # имя файла

    # проверка диапазона
    if n > max_value:
        print(f"ошибка: невозможно сгенерировать {n} уникальных чисел в диапазоне от 1 до {max_value}!")
        return

    print("генерация чисел...")

    # генерация уникальных чисел за один вызов
    try:
        numbers = random.sample(range(1, max_value + 1), n)
    except ValueError as e:
        print(f"ошибка при генерации чисел: {e}")
        return

    # если работа выполнена, обрабатывем данные по частям для плавного заполнения
    batch_size = 10_000
    with tqdm(total=n, desc="обработка чисел") as pbar:
        for i in range(0, n, batch_size):
            pbar.update(min(batch_size, n - i))
            time.sleep(0.01)  # небольшая задержка для прогресса

    # запись в файл
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(' '.join(map(str, numbers)))
        print(f"файл '{output_file}' успешно создан с {n} уникальными числами.")
    except IOError as e:
        print(f"ошибка при записи в файл: {e}")


if __name__ == "__main__":
    generate_numbers_with_progress()