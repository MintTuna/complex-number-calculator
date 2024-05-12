import turtle as t
import math 

#좌표를 그려주는 함수
def coordinateDraw(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.goto(0, 0) 
    t.up()

#복소평면 위의 그려진 선의 각도를 반환하는 함수
def returnAngle(x, y):
    angle = math.degrees(math.atan(y / x))
    #1사분면
    if (x>0 and y>0):
        print(angle)
    #2사분면
    if (x<0 and y>0):
        print(angle+90)
    #3사분면
    if (x<0 and y<0):
        print(angle+180)
    #4사분면
    if (x>0 and y<0):
        print(angle+270)


#복소수 입력받기
a = float(input("복소수의 실수부를 입력하세요 : "))
b = float(input("복소수의 허수부를 입력하세요 : "))

#복소수의 제곱근 계산
p = math.sqrt((a+math.sqrt(a*a + b*b))/2)
q = math.sqrt((-a+math.sqrt(a*a + b*b))/2)

if (b<0):
    p = -p #b의 부호에 따라 제곱근의 부호가 달라짐

#출력
print("%f + %fi 의 제곱근은 %f + %fi 그리고 %f + %fi 입니다" %(a, b, p, q, -p, -q))

#가로축, 세로축 그리기
t.goto(0, 0)
t.forward(500)
t.backward(1000)
t.goto(0, 0)
t.left(90)
t.forward(500)
t.backward(1000)
t.goto(0,0)

#a+bi 그리기
coordinateDraw(a, b) 
returnAngle(a, b)

#p+qi 그리기
t.color("red")
coordinateDraw(p, q)
returnAngle(p, q)

#-p-qi 그리기
t.color("red")
coordinateDraw(-p, -q)
returnAngle(-p, -q)

t.mainloop()