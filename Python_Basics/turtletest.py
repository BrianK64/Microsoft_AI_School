from turtle import *

color('green')
begin_fill()
while True:
    forward(100)
    left(120)

    if abs(pos()) < 1:
        break
end_fill()

color('brown')
begin_fill()

penup()
goto(30, -60)
pendown()
for _ in range(2):
    forward(40)
    left(90)
    forward(60)
    left(90)

end_fill()


done()