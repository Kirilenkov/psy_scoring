import sys


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


def core(df, scale_name):
    clr = Colors()
    counter = 0
    dfl = df.__len__()
    min_range = int(df.loc[0, 'range_min'])
    max_range = int(df.loc[0, 'range_max'])
    band = ''
    for n in range(min_range, max_range + 1):
        band += str(n)
    print(clr.OKBLUE + 'Опросник {}'.format(scale_name) + clr.ENDC)
    print(clr.OKBLUE + 'Допустимый диапазон ответов от {0:d} до {1:d}'.format(min_range, max_range) + clr.ENDC)
    while True:
        if counter < 0:
            counter = 0
        sys.stdout.write(str(df.loc[counter, 'quest']) + ':\n')
        key = input().lower()
        if (key == 'q' or key == 'й') and counter != 0:
            counter -= 1
            print(clr.OKBLUE + 'Переход к ' + clr.BOLD + 'предыдущему вопросу' + clr.ENDC)
        elif key == 'w' or key == 'ц':
            if counter + 1 == dfl:
                print(clr.FAIL + 'Это последний вопрос в данном опроснике\n'
                                 'переход к следующему вопросу невозможен' + clr.ENDC)
            else:
                print(clr.OKBLUE + 'Переход к ' + clr.BOLD + 'следующему вопросу' + clr.ENDC)
                counter += 1
        elif key.__len__() == 1 and key in band:
            df.loc[counter, 'answer'] = key
            if counter + 1 == dfl:
                break
            counter += 1
        else:
            print(clr.FAIL + 'Допустимый диапазон ответов от {0:d}'
                             ' до {1:d}'.format(min_range, max_range) + clr.ENDC)
    print(df.loc[:, ['seq', 'quest', 'answer']])
    return df
