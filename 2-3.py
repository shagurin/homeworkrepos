password=str(input("Придумайте пароль: "))

while len(password)<7:
    print("Пароль должен быть длиннее 8 символов")
    password=str(input("Придумайте пароль: "))
else:
    while password.isupper() or password.islower() or password.isdigit():
        print("Пароль должен содержать заглавные и строчные буквы")
        password=str(input("Придумайте пароль: "))
print("Пароль принят")