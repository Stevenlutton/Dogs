def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(result)

yell("you are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY")