import os

FILENAME = "travel_diary.txt"

def add_entry():
    date = input("Введіть дату (YYYY-MM-DD): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст нотатки: ")

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("-" * 40 + "\n")
    print("Запис додано!")

def search_entries():
    query = input("Введіть дату або ключове слово для пошуку: ").lower()
    if not os.path.exists(FILENAME):
        print("Щоденник ще не створено.")
        return

    found = False
    with open(FILENAME, "r", encoding="utf-8") as file:
        entry = ""
        for line in file:
            if line.strip() == "-" * 40:
                if query in entry.lower():
                    print(entry + "-" * 40)
                    found = True
                entry = ""
            else:
                entry += line
    if not found:
        print("Записи не знайдено.")

def analytics():
    if not os.path.exists(FILENAME):
        print("Щоденник ще не створено.")
        return

    locations = set()
    total_entries = 0
    total_words = 0

    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Локація:"):
                locations.add(line.strip().split(":")[1].strip())
            if line.startswith("Текст:"):
                text = line.strip().split(":", 1)[1].strip()
                total_words += len(text.split())
            if line.strip() == "-" * 40:
                total_entries += 1

    print(f"Кількість записів: {total_entries}")
    print(f"Унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів: {total_words}")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати запис")
        print("2. Пошук запису")
        print("3. Аналітика")
        print("4. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            analytics()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
