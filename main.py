import names


def full_name():
    name1 = names.get_full_name()
    return name1


print(full_name())

def full_name_male():
    name2 = names.get_full_name(gender='male')
    return name2


print(full_name_male())

def first_name_female():
    name3 = names.get_first_name(gender='female')
    return name3


print(first_name_female())
