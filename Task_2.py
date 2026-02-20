import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
        
    results_set = set()
    while len(results_set) < quantity:
        results_set.add(random.randrange(min, max + 1))

    return sorted(list(results_set))


if __name__ == "__main__":
    f = get_numbers_ticket(2, 28, 50)
    print(f)
