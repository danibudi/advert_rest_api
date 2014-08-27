from __future__ import division

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
    total = sum(stat.values()) or 1
    errors = ((stat.get(dist, 0) / total / percent, -percent, dist, adv)
              for dist, percent, adv in details_list)
    score, score, dist, adv = min(errors)
    stat[dist] = stat.get(dist, 0) + 1
    return dist, random.choice(adv)


def __main__():
    distr_percent_advs_list = [('b', 10, [2, 4, 6, 7]),
                               ('a', 70, [1, 5, 8]),
                               ('c', 20, [9, 10, 11, 12])]
    advert_choisen = advert_choice(distr_percent_advs_list)
    print (advert_choisen)
    stat = {}
    for ppp in range(20):
        advert_choised = advert_choice_pid(distr_percent_advs_list, stat)
        print (advert_choised, stat)

if __name__ == '__main__':
    __main__()
