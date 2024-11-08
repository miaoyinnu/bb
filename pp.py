import time
import threading
import pygame
import draw_love  # 假设 draw_love 是绘制爱心的模块
import sys
import os
import pygame

def suppress_pygame_output():
    """屏蔽 Pygame 的初始化输出"""
    sys.stdout = open(os.devnull, 'w')  # 重定向标准输出
    sys.stderr = open(os.devnull, 'w')  # 重定向标准错误

def restore_output():
    """恢复标准输出和错误输出"""
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

# 屏蔽 Pygame 输出
suppress_pygame_output()

# 初始化 Pygame
pygame.mixer.init()

# 恢复输出
restore_output()

# 示例播放音乐
def play_music():
    try:
        pygame.mixer.music.load("1.mp3")  # 替换为你的音乐文件路径
        pygame.mixer.music.play(-1)  # 无限循环播放
    except Exception as e:
        print(f"播放音乐时出错: {e}")
# 表白内容
message = """
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
親愛的周欣瑤：
如果有多一張船飛，你會唔會同我一齊走
1960年4月16号下午3点之前的一分钟你和我在一起，
因为你我会记住这一分钟。
从現在开始我們就是一分鈡的朋友，
这是事实，你改变不了，
因为已释过去了。我明天会再来。”
                    ——《阿K正傳》
你願意做我的唯一嗎？ ❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
"""

def dynamic_print(content, delay=1):
    """
    动态逐行打印内容
    :param content: 要打印的内容（字符串）
    :param delay: 每行打印的间隔时间（秒）
    """
    for line in content.split("\n"):
        print(line)
        time.sleep(delay)

def get_user_response():
    """
    获取用户输入并校验
    """
    valid_responses = ['願意', '更愛你']
    while True:
        print("\n请回答：願意❤️ or 願意❤️")
        ans = input("你的回答：").strip()
        if ans in valid_responses:
            return ans
        else:
            print("無效輸入，請回答：願意 或 更愛你")

def confess_love():
    """
    表白逻辑
    """
    print("加載中...\n")
    time.sleep(2)  # 加载表白
    dynamic_print(message)  # 打印表白内容

    # 获取用户回复
    response = get_user_response()
    if response == '愿意' or response == '願意':
        print("\n谢谢你的回答！为你画一个爱心❤️...")
        draw_love.draw()
    elif response == '更爱你':
        print("\n你比我更爱我，那我更要珍惜你！为你画一个超级大爱心❤️...")
        draw_love.draw()

if __name__ == "__main__":
    # 创建一个线程来播放音乐
    music_thread = threading.Thread(target=play_music, daemon=True)
    time.sleep(6)
    music_thread.start()  # 启动音乐线程

    # 启动表白逻辑
    confess_love()
