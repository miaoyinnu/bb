import turtle
from time import sleep


def draw():
    # 画心形圆弧
    def hart_arc():
        """绘制爱心的圆弧部分"""
        for _ in range(200):  # 循环200次以绘制弧线
            turtle.right(1)  # 每次右转1度
            turtle.forward(2)  # 每次前进2像素

    def move_pen_position(x, y):
        """移动画笔到指定位置"""
        turtle.penup()  # 提起画笔
        turtle.goto(x, y)  # 移动到指定坐标
        turtle.pendown()  # 放下画笔

    # 表白文字与署名
    love = 'Will you marry me?'
    signature = 'pp'

    # 界面初始化
    turtle.setup(width=800, height=600)  # 设置画布大小
    turtle.bgcolor('#FFD1DC')  # 设置背景为柔和的粉色
    turtle.speed(10)  # 设置绘制速度
    turtle.pensize(5)  # 设置画笔粗细
    turtle.color('red', 'pink')  # 设置画笔和填充颜色

    # 隐藏画笔箭头
    turtle.hideturtle()

    # 获取窗口对象以修改标题
    window = turtle.getcanvas().winfo_toplevel()
    window.title("zhouzhou")  # 修改窗口标题

    # 开始绘制爱心
    move_pen_position(0, -180)  # 设置起始位置
    turtle.left(140)  # 旋转画笔角度
    turtle.begin_fill()  # 开始填充
    turtle.forward(224)  # 绘制左下直线
    hart_arc()  # 绘制左侧圆弧
    turtle.left(120)  # 调整画笔方向
    hart_arc()  # 绘制右侧圆弧
    turtle.forward(224)  # 绘制右下直线
    turtle.end_fill()  # 填充结束

    sleep(2)
    # 在心形中写表白文字
    move_pen_position(0, 20)  # 表白文字稍微靠上居中
    turtle.color('#8B0000')  # 设置文字颜色为深红
    turtle.write(love, font=('Arial', 32, 'bold'), align="center")  # 设置文字大而醒目
    sleep(2)

    # 签署名
    if signature.strip():  # 检查署名是否为空
        turtle.color('#8B0000')  # 设置署名颜色为深红
        move_pen_position(180, -220)  # 定位到爱心右下方
        turtle.write(f"- {signature}", font=('Arial', 24, 'italic'), align="center")  # 署名更具设计感
    sleep(1)

    # 点击关闭窗口
    turtle.done()  # 等待用户点击关闭窗口

# 调用绘制函数
