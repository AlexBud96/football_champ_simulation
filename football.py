import random

commands = ['ФК Торпедо Москва',
            'Ротор',
            'ФК Алания',
            'ФК Черноморец Новороссийск',
            'Текстильщик',
            'Машук КВМ',
            'Ангушт',
            'Авангард',
            'Витязь',
            'ФК Сатурн Раменское',
            'Армавир',
            'СКА',
            'Металлург',
            'ФК Динамо Брянск',
            'КАМАЗ',
            'Тосно']


def sortition(commands):
    random.shuffle(commands)
    pairs = []
    for i in range(0, len(commands), 2):
        pairs.append(commands[i:i + 2])
    return pairs


def match(pair):
    result = {}
    score_1 = random.randint(0, 5)
    score_2 = random.randint(0, 5)
    while score_2 == score_1:
        score_2 = random.randint(0, 5)
    if score_1 > score_2:
        result = {pair[0]: 'win', pair[1]: 'loss', 'score': '%d/%d' % (score_1, score_2)}
    else:
        result = {pair[1]: 'win', pair[0]: 'loss', 'score': '%d/%d' % (score_2, score_1)}
    return result


def event(pairs):
    stage = len(pairs)        # len(pairs[0]) == 2
    matches = []
    for pair in pairs:
        matches.append(match(pair))
    if stage != 1:
        results = {'1/%d'% (stage): matches}
    else:
        results = {'final': matches}
    return results


def command_list_refresh(results):
    commands = []
    values = list(results.values())[0]
    for value in values:
        for key, val in value.items():
            if val == 'win':
                commands.append(key)
    return commands


def print_event_result(word, final_result):
    if final_result.get(word) is not None:
        print(final_result[word])
        return not None
    else:
        return None


def print_command_result(word, final_result):
    flag = 0
    for key, val in final_result.items():
        for v in val:
            if v.get(word) is not None:
                print('Этап турнира: %s' % (key))
                print(v)
                flag += 1
    if flag == 0:
        print('Вы неверно ввели название команды')


if __name__ == '__main__':
    final_result = {}
    print('Вы можете запросить этап турнира, например "1/4" или "1/8" или "final".')
    print('Или вы можете напечатать название команды.')
    word = input("Введите этап турнира или команду: ")
    while len(commands) != 1:
        pairs = sortition(commands)
        event_results = event(pairs)
        final_result.update(event_results)
        commands = command_list_refresh(event_results)
    if print_event_result(word, final_result) is None:
        print_command_result(word, final_result)
