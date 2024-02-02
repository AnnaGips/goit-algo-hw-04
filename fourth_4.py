def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Контакт додано"
    else:
        return "Невірна команда. Будь ласка, вкажіть як ім'я, номер телефону."

def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Контакт оновлено"
        else:
            return "Контакт не знайдено"
    else:
        return "Невірна команда. Будь ласка, вкажіть як ім'я, новий номер телефону."

def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Контакт не знайдено"
    else:
        return "Невірна команда. Будь ласка, вкажіть ім'я."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Немає збережених контактів."

def main():
    contacts = {}
    print("Ласкаво просимо до бота-асистента!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда. Будь ласка, спробуйте знову.")

if __name__ == "__main__":
    main()