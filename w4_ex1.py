

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None

    for line in lines:
        try:
            name, salary_str = line.strip().split(",")
            salary = float(salary_str)
            total += salary
            count += 1
        except ValueError:
            print(f"Помилка у рядку: '{line.strip()}'")
            continue


    average = total/count if count > 0 else 0
    return total, average


path = input("Введіть шлях до файлу: ")
result = total_salary(path)
if result is None:
    print("Розрахунок не вдалося виконати.")
else:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

