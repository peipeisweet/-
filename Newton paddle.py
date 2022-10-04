#homework2 Newton cradle
from vpython import *
#基本參數的設定
print('Please type how many balls you want to be lifted at the beginning:', end='')
N = int(input())
g = 9.8
size, m = 0.2, 1
L, k = 2, 150000
Ek_total = 0
Ek_average = 0
Eg_total = 0
Eg_average = 0
#背景與天花板的設定
scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), background=vec(0.5, 0.5, 0))
ceiling = box(length=3, height=0.005, width=0.05, color=color.blue)
#曲線圖也先設定好
graph1 = graph(width = 450)
graph2 = graph(width = 450)
Total_Kinetic_Energy = gcurve(graph = graph1, color=color.blue, width=4)
Total_Gravitation_Energy = gcurve(graph = graph1, color=color.red, width=4)
Average_Kinetic_Energy = gcurve(graph = graph2, color=color.blue, width=4)
Average_Gravitation_Energy = gcurve(graph = graph2, color=color.red, width=4)
#五顆球以及繩子
balls = []
springs = []
for i in range(5):
    balls.append(sphere(radius = size, color=color.red))
    balls[i].v = vec(0, 0, 0)
    balls[i].m = m
    #初始位置
    balls[i].pos = vec((2*size)*(i-2), -L-m*g/k, 0)
    #單擺的輕繩
    springs.append(cylinder(radius=0.005))
    springs[i].pos = vec((2*size)*(i-2), 0, 0)
    springs[i].force = vec(0, 0, 0)
#拉起N顆球
for i in range(N):
    balls[i].pos = vec((i-2)*(2*size)-sqrt(2**2-1.95**2), -1.95-m*g/k, 0)
#先定義好碰撞前後的速度變化
def af_col_v(m1, m2, v1, v2, x1, x2):
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)
#開始隨著時間移動
dt = 0.0001
t = 0
#只跑兩秒避免程式停不下來
while t<2:
    rate(5000)
    t += dt
    for i in range(5):
        #畫出動能隨時間關係圖
        for ball in balls:
            Ek_total += 0.5 * m * ball.v.x ** 2
        Total_Kinetic_Energy.plot(pos=(t, Ek_total))
        #平均動能隨時間關係圖
        Ek_average = Eg_total/t
        Average_Kinetic_Energy.plot(pos=(t, Ek_average))
        #動能變數歸零
        Ek_total = 0
        Ek_average = 0
        #接著劃出位能隨時間的關係圖
        for ball in balls:
            Eg_total += m*g*(ball.pos.y+L+m*g/k)
        Total_Gravitation_Energy.plot(pos=(t, Eg_total))
        #還有平均位能隨時間關係圖
        Eg_average = Eg_total/t
        Average_Gravitation_Energy.plot(pos=(t, Eg_average))
        Eg_total = 0

        springs[i].axis = balls[i].pos-springs[i].pos
        springs[i].force = -k*(mag(springs[i].axis)-L)*springs[i].axis.norm()
        balls[i].a = vec(0, -g, 0)+springs[i].force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        #任兩顆球碰撞在一起
        for j in range(i):
            if mag(balls[i].pos-balls[j].pos)<2*size and balls[i].v.x < balls[j].v.x:
                balls[i].v, balls[j].v = af_col_v(m, m, balls[i].v, balls[j].v, balls[i].pos, balls[j].pos)
