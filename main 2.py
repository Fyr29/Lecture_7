text = ["greetings, friends",
        "hello",
        "Greetings. Friends",
        "Greetings, friends.",
        "greetings, friends."]


def correct_sentence(text):
    text = text[:1].upper() + text[1:]
    if text[-1] != ".":
        text += "."
    return text


for i in text:
    print(correct_sentence(i))


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'


print('Good')