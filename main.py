def say_hi(name, age):
    # if age <= 35:
    #     return f"Привет {name}, тебе {age} лет!\nВы достаточно молоды"
    #
    # else:
    #     return f"Привет {name}, тебе {age} лет!\nВы уже через многое прошли"

    return f"Привет {name}, тебе {age} лет!"


name = input("Введите ваше имя: ")

while not name.isalpha():
    name = input("Вы ввели не верное значение\nВведите ваше имя: ")


age = input("Введите ваш возраст: ")

while not age.isdigit():
    age = input("Вы ввели не верное значение\nВведите ваш возраст: ")
else:
    age = int(age)



# assert say_hi(name, age) == f"Привет {name}, тебе {age} лет!\nВы достаточно молоды" and f"Привет {name}, тебе {age} лет!\nВы уже через многое прошли", "test1"
assert say_hi(name, age) == f"Привет {name}, тебе {age} лет!", "Test1"

print(say_hi(name, age))