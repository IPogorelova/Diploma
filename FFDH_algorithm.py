"""First Fit Decreasing algorithm"""
from parser import parseXML


class Paper(object):
    """ Container for items """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.items = []

    def append_level(self, level):             # добавляем все Level на лист Paper
        self.items.append(level)


class Level(Paper):
    """ Level in each container """
    def __init__(self):
        Paper.__init__(self)
        self.width = 0

    def append(self, item):             # добавляем item на уровень (Level)
        self.items.append(item)
        self.width += item[0]
        self.height += item[1]

    # def __str__(self):
    #    """ Printable representation """
    #    return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def pack(item_list, max_width):                             # max_width - задаётся вручную пока, ширина нынешнего формата
    # функция просто упаковки в контейнер и создания нового при нехватке места
    sorted(item_list, key=lambda i: i[1], reverse=True)
    levels_list = []

    new_level = Level()
    new_level.append(itemList[0])
    new_level.height = lambda item_list: item[1]
    new_level.width = lambda item_list: item[0]
    levels_list.append(new_level)
    level_counter = 1

    for item in item_list:
        # Try to fit item into a Level
        level_num = str('level' + str(level_counter))
        min_free_space = max_width

        for level in levels_list:
            free_space = max_width - (new_level.width + item[0])

            if free_space <= min_free_space:
                min_free_space = free_space
                if free_space < max_width:
                    new_level.append(item)
                else:
                    # контейнер не входит ни на один уровень - создаём новый
                    print('Level ' + level_num + ' is full. Creating a new level.')
                    new_level.append(levels_list)           # добавляет старый уровень в список уровней
                    new_level = Level()
                    new_level.append(item)
                    new_level.height = item[1]
                    new_level.width = item[0]
                    levels_list.append(new_level)
                    level_counter += 1

            levels_height_sum += new_level.height

    return levels_list


if __name__ == '__main__':

    def packAndShow(aList, maxWidth, maxHeight): # aList - здесь orders, maxValue - здесь формат листа бумаги
        """ Pack a list into bins and show the result """

        papers_list = []
        new_paper = Paper()
        papers_list.append(new_paper)

        levels_list = pack(aList, maxWidth)
        level_counter = len(levels_list)
        print('List with orders requires ', level_counter, ' levels')

        for new_paper in papers_list:
            levels_height_sum = 0
            paper_counter = 1
            for level in levels_list:
                levels_height_sum += level.height

                if new_paper.height + levels_height_sum <= maxHeight:
                    new_paper.append_level(level)
                else:
                    papers_list.append(new_paper)
                    new_paper = Paper()
                    new_paper.append_level(level)
                    paper_counter += 1

        print('All levels require ', paper_counter, ' pieces of paper')

        # for level in levels_list:
        #     print(level)


    itemList = parseXML('C:\\Users\\Инна\\Desktop\\Диплом\\SD_02856\\order1')
    packAndShow(itemList, 62370)
