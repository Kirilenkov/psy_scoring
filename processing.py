class Colors:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.ENDC = '\033[0m'


class RangeNoMatch(Exception):
    pass


def manual_input(content, band):
    cl = Colors()
    min_ans = int(band[0])
    max_ans = int(band[1])
    while True:
        try:
            answer = int(input(content + '\n'))
            if answer < min_ans or answer > max_ans:
                raise RangeNoMatch
        except ValueError:
            print(cl.FAIL + 'Ошибка ввода, введите числовое значение' + cl.ENDC)
            continue
        except RangeNoMatch:
            print(cl.FAIL + 'Ошибка ввода, ответ должен быть в диапазоне'
                            ' [{0}; {1}]'.format(min_ans, max_ans) + cl.ENDC)
            continue
        else:
            return answer


def core(df):
    band = (df.loc[0, 'range_min'], df.loc[0, 'range_max'])
    for i in range(df.__len__()):
        df.loc[i, 'answer'] = manual_input(df.loc[i, 'qwest'], band)
        print(df)

