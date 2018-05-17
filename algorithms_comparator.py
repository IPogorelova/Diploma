import FFDH_algorithm
from FFDH_algorithm import itemList
import BFDH_algorithm
import time


def time_compare():

    FFDH_start_time = time.clock()
    FFDH_algorithm.packAndShow(itemList, 841, 1189)
    FFDH_time = (time.clock() - FFDH_start_time)

    BFDH_start_time = time.time()
    BFDH_algorithm.packAndShow(itemList, 841, 1189)
    BFDH_time = (time.time() - BFDH_start_time)

    return(FFDH_time, BFDH_time)


def cost_compare(Sps, Nps, Sf, Nf, Np):                 # Spf - printing forms cost, Nps - number of printed sheets, Sf - fixing works cost, Sps - printed sheet cost,  Nf - number of fixes, Np - number of printed sides

    fixing_cost = (Sps + Sf + Sps*Nf)*Np
    printing_cost = Sps*Nps*Np
    result_cost = fixing_cost + printing_cost

    return result_cost


def algorithms_compare():
    res_doc = open('result.txt', 'w')

    FFDH_time, BFDH_time = time_compare()
    FFDH_cost = cost_compare()                          #вручную дописать параметры
    BFDH_cost = cost_compare()                          #вручную дописать параметры

    res_doc.write('FFDH algorithm: ', '/n', 'Time:' + FFDH_time, '/n', 'Cost: ' + FFDH_cost, '/n')
    res_doc.write('BFDH algorithm: ', '/n', 'Time:' + BFDH_time, '/n', 'Cost: ' + BFDH_cost, '/n')

    res_doc.close()

    return res_doc

algorithms_compare()