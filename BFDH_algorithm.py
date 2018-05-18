"""Best Fit Decreasing algorithm"""
import my_parser
import math
from operator import itemgetter



class Paper(object):
    """ Container for items """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.items = []

    def append_level(self, level):             # добавляем все Level на лист Paper
        self.items.append(level)

    def __str__(self):
        """ Printable representation """
        return 'Levels on paper: %s' % (str(self.items))

class Level(Paper):
    """ Level in each container """
    def __init__(self):
        Paper.__init__(self, height=0, width=0)

    def append(self, item):             # добавляем item на уровень (Level)
        self.items.append(item)
        self.width += item[0]

    def __str__(self):
        """ Printable representation """
        return 'Items on level: %s; level_width: %d; level_height: %d' % (str(self.items), self.width, self.height)


def gcd_finding(item_list):
    circulations_list = []

    for item in item_list:
        circulations_list.append(item[2])

    circulations_list.sort(reverse=False)
    gcd_result = circulations_list[0]

    for i in circulations_list:
        gcd_result = math.gcd(i, gcd_result)

    if gcd_result % 500 != 0:
        gcd_result = 1

    return gcd_result

def circulations_splitting(item_list):
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


def pack(item_list, max_width):                                      # max_width - задаётся вручную пока, ширина нынешнего формата
    # функция просто упаковки в контейнер и создания нового при нехватке места
    sorted(item_list, key=itemgetter(1, 3), reverse=True)
    item_list = circulations_splitting(item_list)
    levels_list = []
    free_spaces_list = []

    new_level = Level()
    levels_list.append(['level_1', new_level, max_width])            # [номер уровня, уровень, свободное место на уровне]
    level_counter = 1

    for item in item_list:
        # Try to fit item into a Level
        level_num = str('level_' + str(level_counter))

        for level in levels_list:
            free_space = level[2] - item[0]
            free_spaces_list.append(free_space)

        try:
            min_free_space = min([i for i in free_spaces_list if i >= 0])
            min_free_space_index = free_spaces_list.index(min_free_space)       #индекс уровня с наименьшим количеством свободного места после упаковки текущего item

        except ValueError:                                                      # item не вхожит ни на один из уровней - создаём новый
            print('No level with enough free space. Creating a new level.')
            print(level)
            new_level = Level()
            level_counter += 1
            level_num = str('level_' + str(level_counter))
            levels_list.append([level_num, new_level, 841])                # добавляет новый уровень в список уровней
            level = levels_list[-1]

            new_level.append(item)
            new_level.height = item[1]
            new_level.width = item[0]
            level[2] = (841 - item[0])

        else:                                                                    # нашли лучший уровень - кладём item туда
            new_level = levels_list[min_free_space_index]
            nes_level = new_level[1]
            nes_level.append(item)
            level[2] = level[2] - item[0]

        free_spaces_list = []

    for level in levels_list:
        items_on_level = level[1].__dict__['items']
        max_circulation = max(item[2] for item in items_on_level)
        level.append(max_circulation)

    return levels_list


def packAndShow(aList, maxWidth, maxHeight): # aList - здесь orders, maxValue - здесь формат листа бумаги
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

        for new_paper in papers_list:
            if new_paper.height + levels_height_sum <= maxHeight:
                new_paper.append_level(level)
                break
            else:
                papers_list.append(new_paper)
                new_paper = Paper(0, 0)
                new_paper.append_level(level)
                levels_height_sum = 0
                paper_counter += 1
                break

    print('All levels require ', paper_counter, ' pieces of paper to lay on.')

    for paper in papers_list:
        new_papers_list = []
        levels_on_paper = paper.__dict__['items']
        max_circulation = max(level[3] for level in levels_on_paper)

    for i in range(0, (max_circulation)):
        new_papers_list.append(paper)
    print('Printing all orders requires ', len(new_papers_list), ' pieces of paper.')

    return new_papers_list


itemList = my_parser.parseXML('C:\\Users\\Инна\\Desktop\\Диплом\\Данные\\SD_02856\\test')

packAndShow(itemList, 841, 1189)

# BFDH_result = open('FFDH_result.txt', 'w')
# BFDH_result.write(packAndShow(itemList, 841, 1189))
# BFDH_result.close()
