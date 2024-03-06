import numpy as np
from math import *
from PIL import Image, ImageOps

img_matrix = np.zeros((4000, 4000, 3), dtype=np.uint8)

# img_matrix[0:300, 0:400, 0] = 0
# img_matrix[0:300, 0:400, 0] = 255
# img_matrix[0:300, 0:400, 2] = 255

"""
Первый пункт последний абзац
for i in range(300):
    for j in range(400):
        img_matrix[i, j, 2] = (i + j) % 256
img = Image.fromarray(img_matrix, mode='RGB')
"""

# Алгоритм 1

"""
def dotted_line(image, x0, y0, x1, y1, count, color):
    step = 1.0/count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color


for i in range(0, 13):
    a = 2 * pi * i / 13
    first_coord = 100 + 95 * cos(a)
    second_coord = 100 + 95 * sin(a)
    dotted_line(img_matrix, 100, 100, first_coord, second_coord, 100, 255)
"""

# Небольшой Фикс

"""def dotted_line(image, x0, y0, x1, y1, count, color):
    count = sqrt(pow((x0 - x1), 2) + pow((y0 - y1), 2))
    step = 1.0/count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color


for i in range(0, 13):
    a = 2 * pi * i / 13
    first_coord = 100 + 95 * cos(a)
    second_coord = 100 + 95 * sin(a)
    dotted_line(img_matrix, 100, 100, first_coord, second_coord, 100, 255)
"""

# Вполне РАБОЧИЙ вариант Брезенхема

"""

def x_loop_line(image, x0, y0, x1, y1, color):
    xchange = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2 * abs(y1 - y0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)

        if xchange:
            image[x, y] = color
        else:
            image[y, x] = color

        derror += dy
        if (derror > (x1 - x0)):
            derror -= 2 * (x1 - x0)
            y += y_update

        #image[y, x] = color

for i in range(0, 13):
    a = 2 * pi * i / 13
    first_coord = int (100 + 95 * cos(a))
    second_coord = int (100 + 95 * sin(a))
    x_loop_line(img_matrix, 100, 100, first_coord, second_coord, 255)

"""

# Задание 4
"""
f = open('model_1.obj')
a = []
b = []
i = 0
for line in f:
    splitted_line = line.split()
    if splitted_line[0] == 'v':
        a.append(float(splitted_line[1]))
        a.append(float(splitted_line[2]))
        a.append(float(splitted_line[3]))
        b.append(a.copy())
        a.clear()
print(b[0], b[1], b[2], sep='\n')
"""

"""
f = open('model_1.obj')
a = []
b = []
for line in f:
    splitted_line = line.split()
    if splitted_line[0] == 'v':
        a.append(float(splitted_line[1]))
        a.append(float(splitted_line[2]))
        b.append(a.copy())
        a.clear()

i = 0
for i in range(len(b)):
    img_matrix[int(5000 * b[i][1] - 700), int(5000 * b[i][0] + 500), 2] = 255

img = Image.fromarray(img_matrix, mode='RGB')
img = ImageOps.flip(img)
img.save('filename.png')
#img.show()
"""


# 5 Задание


def x_loop_line(image, x0, y0, x1, y1, color):
    xchange = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2 * abs(y1 - y0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)

        if xchange:
            image[x, y] = color
        else:
            image[y, x] = color

        derror += dy
        if (derror > (x1 - x0)):
            derror -= 2 * (x1 - x0)
            y += y_update

        # image[y, x] = color


str1 = "v1/vt1/vn1"
ab = str1.split('/')
print(ab)
f = open('model_1.obj')
a, vertices, local_mas = [], [], []
polygons, local_counter = [], 0
i = 0
for line in f:
    splitted_line = line.split()
    if splitted_line[0] == 'v':
        a.append(float(splitted_line[1]))
        a.append(float(splitted_line[2]))
        a.append(float(splitted_line[3]))
        vertices.append(a.copy())
        a.clear()
    if splitted_line[0] == 'f':
        str1 = splitted_line[1].split('/')
        str2 = splitted_line[2].split('/')
        str3 = splitted_line[3].split('/')
        local_mas.append(int(str1[0]))
        local_mas.append(int(str2[0]))
        local_mas.append(int(str3[0]))
        polygons.append(local_mas)
        local_mas = []

for i in polygons:
    x0 = int(vertices[i[0] - 1][0] * 20000) + 2000
    y0 = int(vertices[i[0] - 1][1] * 20000) + 1320
    x1 = int(vertices[i[1] - 1][0] * 20000) + 2000
    y1 = int(vertices[i[1] - 1][1] * 20000) + 1320
    x2 = int(vertices[i[2] - 1][0] * 20000) + 2000
    y2 = int(vertices[i[2] - 1][1] * 20000) + 1320

    x_loop_line(img_matrix, x0, y0, x1, y1, 255)
    x_loop_line(img_matrix, x1, y1, x2, y2, 255)
    x_loop_line(img_matrix, x2, y2, x0, y0, 255)
    local_counter += 1

print(polygons[1], sep='\n')

img = Image.fromarray(img_matrix, mode='RGB')
img = ImageOps.flip(img)
img.save('filename.png')
# img.show()