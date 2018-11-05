from functools import reduce


def keep_roll(roll_num, n_keep, n_skip):
    if roll_num >= 6:
        P = 1
    else:
        P = n_keep/((n_skip+n_keep + (1-roll_num))*1.0)
    return(P)


def last_roll(roll_num, n_keep, n_skip):
    P_vec = []
    for i in range(0, roll_num):
        if i < roll_num-1:
            P_vec.append(1-keep_roll(i+1, n_keep, n_skip))
        else:
            P_vec.append(keep_roll(i+1, n_keep, n_skip))
    Q = reduce(lambda x, y: x*y, P_vec)
    return(Q)


def expected_value(list_E, n_keep, n_skip):
    E = 0
    E += list_E * last_roll(1, n_keep, n_skip)
    for i in range(2, 7):
        E += list_E*last_roll(i, n_keep, n_skip)*(1 - 0.25*(i - 2))
    return(E)
