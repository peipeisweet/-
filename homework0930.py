from vpython import *
from numpy import *
#基本參數的初始設定
g = 9.8
size = 0.25
height = 15
C_drag = 0.9
theta = pi/4
hittimes = 0
totaldistance = 0
maxheight = 0
#圖形的設定
oscillation = graph(width = 450, align ='right')
fun1 = gcurve(graph = oscillation, color=color.blue, width=4)
fun2 = gcurve(graph = oscillation, color=color.green, width=4)
fun3 = gcurve(graph = oscillation, color=color.orange, width=4)
#球的初始條件
scene = canvas(center = vec(0,5,0), width=600, background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width=4, color=color.blue)
ball = sphere(radius = size, color = color.red, make_trail = True)
ball.pos = vec(-15, size, 0)
ball.v = vec(20*cos(theta), 20*sin(theta), 0)
#標示切線方向的箭頭
a = arrow(color = color.white, shaftwidth = 0.1)
#隨著時間開始移動
t=0
dt = 0.001

while hittimes <= 2:
  rate(1000)
  t += dt
  ball.v += vec(0, -g, 0) * dt - C_drag*ball.v*dt #速度的每秒變化(考量空氣阻力)
  ball.pos += ball.v*dt #位移使用速度
  totaldistance += mag(ball.v)*dt #路徑長使用的是速率而非速度
  a.pos = ball.pos
  a.axis = ball.v*0.50
  fun1.plot( pos=(t,mag(ball.v)))  #速度/速率的圖形，藍色
  fun2.plot( pos=(t,totaldistance))  #路徑長的圖形，綠色
  fun3.plot( pos=(t,mag(ball.pos + vec(15, -size, 0))))  #位移的圖形，橘色
  if ball.pos.y <= size and ball.v.y < 0: #碰到地板會彈跳
   ball.v.y = - ball.v.y
   hittimes += 1  #彈跳次數加一，因為題目只要求三次
  if ball.pos.y >= maxheight:
      maxheight = ball.pos.y  #最大高度
#最後運動結束跳出訊息
msg = text(text = 'the maximum height is ' + str(maxheight) , pos = vec(-10,5,0))

 
