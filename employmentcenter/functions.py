_num_list = list(map(str,list(range(10)))) + ["+"]

def edit_nums(phone: str) -> str:
    """Converts phone to format +7xxxxxxxxxx"""
    converted = phone
    if phone[0] == "8":
        converted = "+7" + converted[1:]
    elif phone[0] == "9":
        converted = "+7" + converted
    return converted

def edit_name(fio_str : str) -> str:
    items = fio_str.split(" ")
    converted = ""
    for ind in [2, 0, 1]:
        if ind != 1:
            converted += items[ind] + " "
        else:
            converted += items[ind]
    return converted
    
def obtain_phone(string):
    """obtain phone number from parsed personal data"""
    phone_num = ""
    for char in string:
        if char in _num_list:
            phone_num += char
    return edit_nums(phone_num)

def obtain_name(string):
    """obtain name from parsed personal data"""
    char1 = ">"
    char2 = "<"
    for ind, char in enumerate(string):
        if char == char1:
            index = ind + 1
            break
    name, char = "", string[index]
    
    while char != char2:
        char = string[index]
        name += char
        index += 1
    return name[:-1]

def obtain_age_education(bs, name):
    table_rows = bs.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if row[0] == name:
            return row[1]

def employee_dict(person_list):
    myit = iter(person_list)
    key_list = ['Город', 'ФИО', 'Пол', 'Дата рождения', 'Возраст', 'Телефон', 'Email', 'Должность','Желаемая зарплата', 'Занятость', 'Образование']
    temp_dict = dict.fromkeys(key_list)
    for key, _ in temp_dict.items():
        temp_dict[key] = next(myit)
    return temp_dict
    