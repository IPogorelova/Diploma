def circulations_splitting(item_list):
    gcd = 500
    new_item_list = []
    for item in item_list:
        parts_amount = int(item[2] / gcd)
        item[2] = parts_amount

        for i in range(1, parts_amount):
            new_item_list.append(item)

    for item in new_item_list:
        item_list.append(item)

    return item_list

item_list = [[105, 148, 1000, 175897], [105, 148, 2000, 176939], [105, 148, 500, 177247], [148, 210, 500, 177259], [105, 148, 1000, 177295], [105, 148, 2000, 177372], [148, 210, 2000, 177407], [105, 148, 2000, 177473], [105, 148, 1000, 177479], [210, 297, 5000, 177501]]
print(circulations_splitting(item_list))
