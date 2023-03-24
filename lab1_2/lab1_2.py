from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x):
    return x.value

A = list(map(getvalue, sheet['A'][1:]))
C = map(getvalue, sheet['C'][1:])
D = map(getvalue, sheet['D'][1:])


# print(list(A))
# print(list(C))
# print(list(D))

pyplot.plot(A, list(C))
pyplot.plot(A, list(D))
pyplot.show()
