import re
import os
import xml.etree.ElementTree as ET


def parseXML(dir):
    files_list = os.listdir(dir)
    orders = []

    for file_name in files_list:
        file_path = os.path.join(dir, file_name)
        tree = ET.parse(file_path)

        root = tree.getroot()

        for element in root:
            amount = element.attrib['Amount']
            content_data = element.attrib['ContentData']
            paper_size = re.search('\d?\d\dx\d?\d?\d\d', content_data).group(0).split('x')
            jobID = element.attrib['JobID']

            order_parameters = [int(paper_size[0]), int(paper_size[1]), int(amount), int(jobID)]

        orders.append(order_parameters)

    print(orders)
    return orders


parseXML('C:\\Users\\Инна\\Desktop\\Диплом\\Данные\\SD_02856\\test')


