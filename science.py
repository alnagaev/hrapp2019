import snowballstemmer as snb
import re
import csv


def process(string):
    string = re.sub(r'[^\w\s]', ' ', string.lower())
    tokens = string.split()
    return tokens


def find_worker(vacancy, n=10):
    with open('data/datafinal.csv', 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))[:-1]

    max_score = (0, 0)
    scores = []
    stemmer = snb.stemmer('russian')
    for i, datum in enumerate(data):
        print(i)
        total, positive = 0, 0
        first = stemmer.stemWords(process(datum[1]))
        first_need = stemmer.stemWords(process(vacancy['first']))
        c = set(first).intersection(set(first_need))
        if len(c) == 0:
            total += 1
        else:
            positive += len(c)
            total += len(c)
        if (vacancy['second'] != '') and (datum[2] != ''):
            salary = int(vacancy['second']) - int(datum[2])
            if salary < 10000:
                positive += salary / 10000
            total += 1
        if vacancy['fourth'].lower() == datum[5].lower():
            positive += 1
        total += 1
        if vacancy['fifth'].lower() == datum[6].lower():
            positive += 1
        total += 1
        first = stemmer.stemWords(process(datum[7]))
        first_need = stemmer.stemWords(process(vacancy['sixth']))
        c = set(first).intersection(set(first_need))
        if len(c) == 0:
            total += 1
        else:
            positive += len(c)
            total += len(c)
        first = stemmer.stemWords(process(datum[8]))
        first_need = stemmer.stemWords(process(vacancy['seventh']))
        c = set(first).intersection(set(first_need))
        if len(c) == 0:
            total += 1
        else:
            positive += len(c)
            total += len(c)
        score = positive / total
        if score > max_score[1]:
            max_score = (i + 1, score)
            scores.append(max_score)

    scores = sorted(scores, key=lambda k: -k[1])[:n]
    out = [{'first': data[score[0] - 1][1], 'second': data[score[0] - 1][2], 'third': data[score[0] - 1][4],
             'fourth': data[score[0] - 1][5], 'fifth': data[score[0] - 1][6], 'sixth': data[score[0] - 1][7],
             'seventh': data[score[0] - 1][8], 'score': score[1]} for score in scores]
    return max_score, out
