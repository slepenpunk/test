def open_file(name):
    text = open(name, 'r', encoding='utf-8')
    text = text.read()
    return text


def total_repeats(name_file):
    d = {}
    k = (' ', '.', ',', '...', '!', ':', '""', '-', '…', '—', '?', '')
    for i in name_file:
        if i not in d:
            d[i] = 1
        elif i in k:
            pass
        else:
            d[i] += 1
    return d


def main():
    the_file = open_file('file.txt')
    repeats = total_repeats(the_file)

    for i in repeats:
        if repeats[i] > 1:
            print(i, '-', repeats[i])
main()



