from vpython import *
g = 10
size = 0.25
height = 15.0

scene = canvas(width=800, height=800, center =vec(0,height/2,0),
               background=vec(0.5,0.5,0))
# canvas開一個新視窗，右x上y出z
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball

msg =text(text = 'Free Fall', pos = vec(-10, 10, 0))
ball.pos = vec( 0, height, 0) # ball center initial position
ball.v = vec(0, 0 , 0) # ball initial velocity

dt = 0.001 # time step
while ball.pos.y >= size:
 rate(1000) # run 1000 times per real second
 ball.pos = ball.pos + ball.v*dt
 ball.v.y = ball.v.y - g*dt


msg.visible = False
msg =text(text = str(ball.v.y), pos = vec(-10, 10, 0))
print(ball.v.y)
