"""First Fit Decreasing algorithm"""
import my_parser


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
        return 'Levels on paper: %s' % (list([str(x) for x in self.items]))

class Level(Paper):
    """ Level in each container """
    def __init__(self):
        Paper.__init__(self, height=0, width=0)

    def append(self, item):                                         # добавляем item на уровень (Level)
        self.items.append(item)
        self.width += item[0]
        self.height += item[1]

    def __str__(self):
        """ Printable representation """
        return 'Items on level: %s; level_width: %d; level_height: %d' % (str(self.items), self.width, self.height)


def pack(item_list, max_width):                                     # max_width - задаётся вручную пока, ширина нынешнего формата
    # функция просто упаковки в контейнер и создания нового при нехватке места
    item_list.sort(key=lambda i: i[1], reverse=True)
    levels_list = []

    new_level = Level()
    #new_level.append(item_list[0])
    levels_list.append(['level_1', new_level, max_width])            # [номер уровня, уровень, свободное место на уровне]

    for item in item_list:
        # Try to fit item into a Level

        for level in levels_list:
            free_space = level[2] - item[0]                         # для BFDH
            # min_free_space = max_width
            if free_space > 0:                                      # if all([(free_space > 0), (free_space <= min_free_space)]): - for BFDH_alghorithm
                new_level.append(item)                              # min_free_space = free_space
                level[2] = free_space
            else:
                # контейнер не входит ни на один уровень - создаём новый
                level_num = str('level_' + str(len(levels_list) + 1))
                print('Level ' + level_num + ' is full. Creating a new level.')
                new_level = Level()

                new_level.append(item)
                new_level.height = item[1]
                new_level.width = item[0]
                level[2] = (841 - item[0])
                levels_list.append([level_num, new_level, (free_space + item[0])])          # добавляет старый уровень в список уровней
                break

                # levels_height_sum += new_level.height

    return levels_list


if __name__ == '__main__':

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
#print(itemList)

print(list([str(x) for x in packAndShow(itemList, 841, 1189)]))
