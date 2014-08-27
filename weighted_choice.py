from __future__ import division

import random


def weighted_choice(choices):
    """Like random.choice, but each element can have
    a different chance of being selected."""
    total = sum(dpa[1] for dpa in choices)
    if total == 0:
        raise ValueError('total 0')
    r = random.uniform(0, total)
    upto = 0
    for dpa in choices:
        upto += dpa[1]
        if r < upto:
            break
    return dpa


def advert_choice(distributors_list):
    """random adverts for a distributor"""
    distributors_list = [dist_details for dist_details
                         in distributors_list if dist_details[2]]
    dist_details = weighted_choice(distributors_list)
    advert = random.choice(dist_details[2])
    return (dist_details[0], advert)


def advert_choice_pid(details_list, stat):
    """PID controller with i=d=0
    random adverts;
    stat: persistent dict for the statistics {distr: count_of_choosen_adverts}
    better approach for distributor & advert then advert_choice()"""
    details_list = [dist_details for dist_details
                    in details_list if dist_details[2]]
    if details_list == []:
        raise ValueError('total 0')
    total = sum(stat.values()) or 1
    errors = ((stat.get(dist, 0) / total / percent, -percent, dist, adv)
              for dist, percent, adv in details_list)
    score, score, dist, adv = min(errors)
    stat[dist] = stat.get(dist, 0) + 1
    return dist, random.choice(adv)
