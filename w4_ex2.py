def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None

    for line in lines:
        try:
            id, name, age = line.strip().split(",")
            cat = {
                "id": id,
                "name": name,
                "age": age
            }
            cats_list.append(cat)
        except ValueError:
            print(f"Помилка у рядку: '{line.strip()}'")
            continue
    return cats_list

path = input("Введіть шлях до файлу: ")
result = get_cats_info(path)
if result is None:
    print("Немає доступних даних.")
else:
    print(result)


