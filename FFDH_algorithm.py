"""First Fit Decreasing algorithm"""
import my_parser
import math
from operator import itemgetter



class Paper(object):
    """ Container for items """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.items = []

    def append_level(self, level):                                  # добавляем все Level на лист Paper
        self.items.append(level)

    def __str__(self):
        """ Printable representation """
        return 'Levels on paper: %s' % (list([str(x) for x in self.items]))         #TODO: строковый вывод объекта уровня

class Level(Paper):
    """ Level in each container """
    def __init__(self):
        Paper.__init__(self, height=0, width=0)

    def append(self, item):                                         # добавляем item на уровень (Level)
        self.items.append(item)
        self.width += item[0]
        # self.height = item[1]

    def __str__(self):
        """ Printable representation """
        return 'Items on level: %s; level_width: %d; level_height: %d' % (str(self.items), self.width, self.height)


gcd = 0


def gcd_finding(item_list):
    circulations_list = []

    for item in item_list:
        circulations_list.append(item[2])

    circulations_list.sort(reverse=False)
    gcd_result = circulations_list[0]

    for i in circulations_list:
        gcd_result = math.gcd(i, gcd_result)

    if gcd_result % 100 != 0:
        gcd_result = 1

    return gcd_result


def circulations_splitting(item_list):
    global gcd
    gcd = gcd_finding(item_list)
    new_item_list = []
    for item in item_list:
        parts_amount = int(item[2] / gcd)
        item[2] = parts_amount

        for i in range(1, parts_amount):
            new_item_list.append(item)

    for item in new_item_list:
        item_list.append(item)

    return item_list


def pack(item_list, max_width):                                     # max_width - задаётся вручную пока, ширина нынешнего формата
    # функция просто упаковки в контейнер и создания нового при нехватке места
    item_list = circulations_splitting(item_list)
    item_list = sorted(item_list, key=itemgetter(1, 3), reverse=True)
    levels_list = []

    new_level = Level()
    new_level.height = item_list[0][1]
    levels_list.append(['level_1', new_level, max_width])            # [номер уровня, уровень, свободное место на уровне]

    for item in item_list:
       # Try to fit item into a Level
        for level in levels_list:
            free_space = level[2] - item[0]

            if free_space > 0:
                new_level.append(item)
                level[2] = free_space

            else:
                # контейнер не входит ни на один уровень - создаём новый
                level_num = str('level_' + str(len(levels_list)))
                print('Level ' + level_num + ' is full. Creating a new level.')
                new_level = Level()

                new_level.append(item)
                new_level.height = item[1]
                new_level.width = item[0]
                level[2] = (841 - item[0])
                levels_list.append([level_num, new_level, (free_space + item[0])])          # добавляет старый уровень в список уровней
            break

    for level in levels_list:
        items_on_level = level[1].__dict__['items']
        max_circulation = gcd_finding(item_list)                              # max(item[2] for item in items_on_level)
        level.append(max_circulation)

    levels_list.pop(0)

    return levels_list


def packAndShow(aList, maxWidth, maxHeight):                    # aList - здесь orders, maxValue - здесь формат листа бумаги
    """ Pack a list into bins and show the result """

    papers_list = []
    new_paper = Paper(0, 0)
    papers_list.append(new_paper)
    levels_list = pack(aList, maxWidth)
    level_counter = len(levels_list)
    print('List with orders requires', level_counter, 'levels')

    levels_height_sum = 0
    paper_counter = 1
    for level in levels_list:
        levels_height_sum += level[1].height

        if new_paper.height + levels_height_sum <= maxHeight:
            new_paper.append_level(level)

        else:
            print(new_paper)
            papers_list.append(new_paper)
            new_paper = Paper(0, 0)
            new_paper.append_level(level)
            levels_height_sum = level[1].height
            paper_counter += 1
            break

    if len(papers_list) > 1:
        papers_list.pop(0)
        paper_counter = paper_counter-1

    print('All levels require ', paper_counter, ' pieces of paper to lay on.')

    for paper in papers_list:
        levels_on_paper = paper.__dict__['items']
        max_circulation = max(level[3] for level in levels_on_paper)*gcd
        papers_amount = paper_counter*gcd

    print('Printing all orders requires ', papers_amount, ' pieces of paper in general.')

    return papers_list


itemList = my_parser.parseXML('C:\\Users\\Инна\\Desktop\\Диплом\\Данные\\SD_02856\\test')

print(list([str(x) for x in packAndShow(itemList, 841, 1189)]))

# FFDH_result = open('FFDH_result.txt', 'w')
# FFDH_result.write(str(list([str(x) for x in packAndShow(itemList, 841, 1189)])))
# FFDH_result.close()
