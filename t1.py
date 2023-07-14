from turtle import *
speed('slowest')
pencolor('red')
pensize(3)
# range(stop)
# range(start,stop)
# range(start,stop,step)
for i in range(6,30,3):
    fd(120)
    lt(60)
    dot(10,"green")
    write(i,font=('calibri',20,'bold '))

# reverse
goto(500,500)
for i in range(10,0,-1):
    fd(60)
    lt(36)
    dot(20,'green')
    write(i,font=('calibri',20,'bold '))
mainloop()