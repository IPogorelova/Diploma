"""First Fit Decreasing algorithm"""
import my_parser


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


def pack(item_list, max_width):                                      # max_width - задаётся вручную пока, ширина нынешнего формата
    # функция просто упаковки в контейнер и создания нового при нехватке места
    item_list.sort(key=lambda i: i[1], reverse=True)
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

    return levels_list


if __name__ == '__main__':

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
        for element in levels_list:
            level = element[1]
            levels_height_sum += level.height

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
        print('All levels require ', paper_counter, ' pieces of paper')
        return papers_list

itemList = my_parser.parseXML('C:\\Users\\Инна\\Desktop\\Диплом\\SD_02856\\test')
print(itemList)

print(packAndShow(itemList, 841, 1189))