from operator import itemgetter

def circulations_splitting(item_list):
    gcd = 500
    for item in item_list:
        if gcd != 1:
            parts_amount = int(item[2] / gcd)
            item[2] = parts_amount

        for i in range(parts_amount-1):
            item_list.append(item)

    return item_list



item_list = [[210, 298, 1000, 175897], [105, 148, 2000, 176939], [148, 210, 500, 177247]]
item_list = circulations_splitting(item_list)
print(sorted(item_list, key=itemgetter(1, 3), reverse=True))

