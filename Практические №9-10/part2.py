def ex1():
    school = {
        "1a": 20,
        "1b": 19,
        "2a": 22,
        "2b": 13,
        "3a": 27,
        "3b": 15,
        "4a": 30
    }
    print(school)

    school["3a"] = 25
    school["4b"] = 10
    school.pop("2b")
    print(school)

    summ = 0
    for v in school.values():
        summ += v
    print(summ)


ex1()


def ex2():
    def convert(dict_items):
        new_dict = {}
        for key, value in dict_items:
            new_dict[value] = key
        return new_dict

    dict = {
        1: "один",
        2: "два",
        3: "три"
    }
    print(dict)
    new_dict = convert(dict.items())
    print(new_dict)


ex2()

