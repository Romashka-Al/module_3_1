def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    count_calls()
    return tuple((len(string), string.upper(), string.lower()))


def is_contains(string, list_to_search):
    count_calls()
    a = 0
    for el in list_to_search:
        if string.lower() == el.lower():
            a = 1
            break
    if a == 1:
        return True
    else:
        return False


calls = 0
print(is_contains("Qiqi", ['Klee', 'QiQi', 'YaoYao', 'Diona', 'Sayu', 'Sigewinne', 'Dori']))
print(string_info('~AvAdAKiDaVrA~'))
print(is_contains('Loli', ['Venti', 'Lisa', 'Jean', 'La Sinjora']))
print(calls)
