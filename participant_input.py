from datetime import datetime as dt


class NoMatch(Exception):
    pass


class LenNoMatch(NoMatch):
    pass


KEY = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
EOI = 'Ошибка ввода. '


def letter_encoder(letter, decoding):
    result = str(decoding.find(letter) + 1)
    if len(result) == 1:
        result = '0' + result
    return result


def exc_check(sequence, key):
    e = 0
    for letter in sequence:
        if not letter.upper() in key:
            print(EOI + 'Недопустимый символ: "{0:s}"'.format(letter))
            e += 1
    if e != 0:
        raise NoMatch


def input_checker(content):
    while True:
        output = input('{} \n'.format(content)).upper()
        try:
            exc_check(output, KEY)
        except NoMatch:
            continue
        break
    return output


def full_name_input():
    parts = ['фамилию ', 'имя ', 'отчество ']
    full_name = ''
    for p in parts:
        full_name += input_checker('Введите ' + p + 'пациента:') + ' '
    return full_name[:-1]


def check_date(*messages, check_range=False):
    mess = messages
    date = ''
    while True:
        try:
            date = input(mess[0])
            if len(date) != 10:
                raise LenNoMatch
        except ValueError:
            print(EOI + 'Недопустимые символы')
            continue
        except LenNoMatch:
            print(EOI + 'Длина ввода должна был 10 символов вместе с разделителями')
            continue
        else:  # Изёвая проверка корректности даты. Можно строже.
            if int(date[0:2]) < 1 or int(date[0:2]) > 31:
                print(EOI + 'Число месяца должо быть в диапазоне [1, 31].')
                continue
            if int(date[3:5]) < 1 or int(date[3:5]) > 12:
                print(EOI + 'Месяц должен быть в диапазоне [1, 12].')
                continue
                # Обсудить рамки возраста тестируемых
            year = dt.today().year
            if check_range and (int(date[6:]) < year - 110 or int(date[6:]) > year - 10):
                print(EOI + mess[1].format(year - 110, year - 10))
                continue
        break

    return date


def sex_input():
    while True:
        sex = input('Введите пол испытуемого (м/ж):\n')
        if sex in 'мж':
            return sex
        else:
            print(EOI + 'Вы ввели недопустимое значение: {}'.format(sex))


def report():
    full_name = full_name_input()
    dob_mess = ('Введите день и месяц и год рождения испытуемого в формате дд.мм.гггг: \n',
                'Год рождения должен быть в диапазоне [{0:d}, {1:d}].')
    dob = check_date(*dob_mess, check_range=True)
    fd_mess = ('Введите дату заполнения опросников в формате дд.мм.гггг: \n',)
    filling_date = check_date(*fd_mess)

    print('Вы ввели ФИО: {!r}'.format(full_name.upper()))
    print('Вы ввели дату рождения: {!r}'.format(dob))
    print('Вы ввели дату заполнения опросников {!r}'.format(filling_date))
    print('Нажмите Enter для продолжения.')
    input()
    return {'full_name': full_name, 'dob': dob, 'filling_date': filling_date}


def visit_input():
    visit = 0
    while True:
        try:
            visit = int(input('Введите номер визита (от 1 до 3): \n'))
            if visit < 1 or visit > 3:
                print(EOI + 'Номер визита должен быть в диапазоне [1, 3]')
                continue
        except ValueError:
            print(EOI + 'Введите ЧИСЛО от 1 до 3.')
            continue
        break
    return visit


def main():
    primary = report()
    primary['visit'] = str(visit_input())
    primary['sex'] = str(sex_input())
    return primary


if __name__ == '__main__':
    main()
