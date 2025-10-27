import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return 'Щось не так'
    results_set = set()
    while len(results_set) < quantity:
        results_set.add(random.randrange(min, max + 1))

    result_list =  sorted(list(results_set))
    return result_list

f = get_numbers_ticket(2, 28, 50)
print(f)