import pygame
import math
import random
pygame.init()
pygame.display.set_caption("Balls Game")
width = 1100
height = 600
win = pygame.display.set_mode((width, height))
nn = 3

r = []
m = []
x = []
y = []
a = []
v = []
c = []

for i in range(nn + 1):
    r.append(50)
    m.append(100)
    x.append(random.randint(100,1000))
    y.append(random.randint(10,500))
    a.append(random.random() * 2 * math.pi)
    v.append(random.randint(5,10))
    c.append(0)
    c[i] = int(0),int(150),int(190)



var_ = True
while var_:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_ = False
        elif event.type == pygame.MOUSEBUTTONUP:
            nn += 1
            x1, y1 = pygame.mouse.get_pos()
            r.append(50)
            m.append(100)
            x.append(x1)
            y.append(y1)
            a.append(random.random() * 2 * math.pi)
            v.append((random.randint(5, 10)))
            c.append((int(0),int(150),int(190)))
            pygame.draw.circle(win, c[i], (x1, y1), r[i])

    win.fill((0,0,0))

    for i in range(1, nn + 1):
        if v[i] < 5:
            c[i] = (int(227),int(184),int(27))
        if 5 <= v[i] < 8:
            c[i] = (int(32),int(201),int(182))
        if 8 <= v[i] < 10:
            c[i] = (int(0), int(255), int(26))
        if v[i] >= 10:
            c[i] = (int(255), int(0), int(0))

        x[i] += v[i] * math.cos(a[i])
        y[i] += v[i] * math.sin(a[i])
        pygame.draw.circle(win, c[i],(x[i],y[i]),r[i])

    pygame.time.delay(10)
    pygame.display.update()

    for i in range(1, nn + 1):
        if v[i] > 0:
            v[i] = v[i] - 0.0003

    for i in range(1, nn + 1):
        if pygame.key.get_pressed()[pygame.K_UP]:
            v[i] = v[i] + 0.1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            v[i] = v[i] - 0.1

    for i in range(1, nn + 1):
        if x[i] <= r[i] and (a[i] > math.pi / 2 or a[i] < -math.pi / 2):
            a[i] = math.pi - a[i]
        if x[i] >= width - r[i] and (a[i] > -math.pi / 2 and a[i] < math.pi / 2):
            a[i] = math.pi - a[i]
        if y[i] <= r[i] and (a[i] < 0 and a[i] > -math.pi):
            a[i] = -a[i]
        if y[i] >= height - r[i] and (a[i] > 0 and a[i] < math.pi):
            a[i] = -a[i]
        while a[i] > math.pi: a[i] -= 2 * math.pi
        while a[i] < -math.pi: a[i] += 2 * math.pi

    for i in range(1, nn + 1):
        for j in range(i + 1, nn + 1):
            dist = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if dist <= r[i] + r[j]:
                x1New = x[i] + v[i] * math.cos(a[i])
                y1New = y[i] + v[i] * math.sin(a[i])
                x2New = x[j] + v[j] * math.cos(a[j])
                y2New = y[j] + v[j] * math.sin(a[j])
                distNew = ((x1New - x2New) ** 2 + (y1New - y2New) ** 2) ** 0.5
                if dist > distNew:
                    angle = math.atan((y[j] - y[i])/(x[j]-x[i]))
                    if (x[j] - x[i]) < 0:
                        angle += math.pi
                        while angle > math.pi / 2: angle -= 2 * math.pi
                        while angle < -math.pi / 2: angle += 2 * math.pi
                    k1 = a[i] - angle
                    k2 = a[j] - angle

                    V1 = v[i] * math.cos(k1)
                    V2 = v[j] * math.cos(k2)
                    Vt1 = v[i] * math.sin(k1)
                    Vt2 = v[j] * math.sin(k2)

                    V1 = (2 * m[j] * v[j] * math.cos(k2) + (m[i] - m[j]) * v[i] * math.cos(k1)) / (m[i] + m[j])
                    V2 = (2 * m[i] * v[i] * math.cos(k1) + (m[j] - m[i]) * v[j] * math.cos(k2)) / (m[i] + m[j])

                    v[i] = (V1 ** 2 + Vt1 ** 2) ** 0.5
                    v[j] = (V2 ** 2 + Vt2 ** 2) ** 0.5

                    k1 = math.atan(Vt1 / V1)
                    if V1 < 0:
                        k1 += math.pi
                    k2 = math.atan(Vt2 / V2)
                    if V2 < 0:
                        k2 += math.pi

                    a[i] = angle + k1
                    while a[i] > math.pi: a[i] -= 2 * math.pi
                    while a[i] < -math.pi: a[i] += 2 * math.pi
                    a[j] = angle + k2
                    while a[j] > math.pi: a[j] -= 2 * math.pi
                    while a[j] < -math.pi: a[j] += 2 * math.pi

pygame.quit()
print(c)
