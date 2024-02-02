def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as a:
            file = a.readlines()
            line = [int(line.split(",")[1]) for line in file]
            total = sum(line)
            average = total // len(line)
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print("Файл не знайден, вкажіть праильний шлях дл файлу.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")

total_salary("//Users//mac//Desktop/hw_4//zp.txt.txt")



