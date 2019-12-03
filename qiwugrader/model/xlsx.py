# -*- coding:utf-8 -*-
import xlrd as xlrd


def xlsx(file_name):

    table = xlrd.open_workbook(file_name).sheet_by_name('Sheet1')

    rows = table.nrows
    test_sentence_list = {}
    start = 1

    for row in range(1, rows):
        test_sentence = table.cell(row, 1).value
        test_sentence_list[start] = test_sentence
        start = start + 1

    return test_sentence_list


if __name__ == '__main__':
    xlsx("C:\\Users\\tech2\Documents\GitHub\QiwuGrader\\testcases\\test.xlsx")
