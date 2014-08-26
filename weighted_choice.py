import random


#test - 1000 pass
def weighted_choice(choices):
    """Like random.choice, but each element can have \
    a different chance of being selected."""
    total = sum(dpa[1] for dpa in choices)
    r = random.uniform(0, total)
    upto = 0
    for dpa in choices:
        upto += dpa[1]
        if r < upto:
            break
    return dpa


def advert_choice(distributors_list):
    dist_details = weighted_choice(distributors_list)
    advert = random.choice(dist_details[2])
    return (dist_details[0], advert)


def advert_choice_pid(details_list, stat):
    pass


def __main__():
    distr_percent_advs_list = [(2, 10, [2, 4, 6, 7]), (1, 70, [1, 5, 8]),
                               (3, 20, [9, 10, 11, 12])]
    advert_choised = advert_choice(distr_percent_advs_list)
    stat = {}
    advert_choised = advert_choice_pid(distr_percent_advs_list, stat)
    print (advert_choised)


if __name__ == '__main__':
    __main__()
