import FFDH_algorithm
import BFDH_algorithm
from FFDH_algorithm import itemList

import timeit


def time_compare():

    FF_stmt = FFDH_algorithm.packAndShow(itemList, 841, 1189)
    BF_stmt = BFDH_algorithm.packAndShow(itemList, 841, 1189)
    FFDH_time = min(timeit.Timer(lambda: FF_stmt).repeat(repeat=3))
    BFDH_time = min(timeit.Timer(lambda: BF_stmt).repeat(repeat=3))

    return(FFDH_time, BFDH_time)


def cost_compare(Sps, Nps, Sf, Nf, Np):                 # Spf - printing forms cost, Nps - number of printed sheets, Sf - fixing works cost, Sps - printed sheet cost,  Nf - number of fixes, Np - number of printed sides

    fixing_cost = (Sps + Sf + Sps*Nf)*Np
    printing_cost = Sps*Nps*Np
    result_cost = fixing_cost + printing_cost

    return result_cost


def algorithms_compare():
    res_doc = open('result.txt', 'w')

    FFDH_time, BFDH_time = time_compare()
    FFDH_cost = cost_compare(1, 2, 3, 4, 5)                          #вручную дописать параметры
    BFDH_cost = cost_compare(1, 2, 3, 4, 5)                          #вручную дописать параметры

    res_doc.write('FFDH algorithm: ' + '\n' + 'Time: ' + str(FFDH_time) + '\n' + 'Cost: ' + str(FFDH_cost) + '\n' + '\n')
    res_doc.write('BFDH algorithm: ' + '\n' + 'Time: ' + str(BFDH_time) + '\n' + 'Cost: ' + str(BFDH_cost) + '\n')

    res_doc.close()

    return res_doc

algorithms_compare()
