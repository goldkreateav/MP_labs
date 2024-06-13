from map import AVLMap

def main():
    avl_map = AVLMap()

    # Вставка элементов
    avl_map.insert(10, "Значение для 10")
    avl_map.insert(20, "Значение для 20")
    avl_map.insert(5, "Значение для 5")

    # Получение значений по ключам
    print(f"Значение для ключа 10: {avl_map[10]}")
    print(f"Значение для ключа 20: {avl_map[20]}")
    print(f"Значение для ключа 5: {avl_map[5]}")

    # Обновление значения по ключу
    avl_map[10] = "Обновленное значение для 10"
    print(f"Обновленное значение для ключа 10: {avl_map[10]}")

    # Удаление элемента по ключу
    avl_map.delete(20)
    print("Удален ключ 20")

    # Попытка получения значения для удаленного ключа
    try:
        print(avl_map[20])
    except KeyError as e:
        print(e)

    print("Очистка мапа")
    avl_map.clear()
    print(f"Мап пуст: {avl_map.is_empty()}")

    # Повторная вставка элементов
    avl_map.insert(30, "Значение для 30")
    avl_map.insert(40, "Значение для 40")

    # Итерация по элементам карты
    for key, value in avl_map:
        print(f"Ключ: {key}, Значение: {value}")

if __name__ == "__main__":
    main()
