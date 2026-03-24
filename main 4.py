def common_elements():
    dictionary_3 = set()
    dictionary_5 = set()

    for i in range(101):

        if i % 3 == 0:
            dictionary_3.add(i)

        if i % 5 == 0:
            dictionary_5.add(i)


    print(dictionary_3 & dictionary_5)
    return dictionary_3 & dictionary_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


print('Good')