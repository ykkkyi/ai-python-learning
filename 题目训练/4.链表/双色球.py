import random
red_balls=list(range(1,34))
selected_ball=[]
for _ in range(6):
    index=random.randrange(len(red_balls))
    selected_ball.append(red_balls.pop(index))
selected_ball.sort()
for ball in selected_ball:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
blue_ball=random.randrange(1,17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
利用random模块提供的sample和choice函数来简化上面的代码
"""

red_balls=[i for i in range(1,34)]
blue_balls=[i for i in range(1,17)]
selected_ball=random.sample(red_balls,6)
selected_ball.sort()
for ball in selected_ball:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
blue_ball=random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')


"""
实现随机生成N注号码
"""

n=int(input('生成几注号码：'))
red_balls=[i for i in range(1,34)]
blue_balls=[i for i in range(1,17)]

for _ in range(n):
    selected_ball=random.sample(red_balls,6)
    selected_ball.sort()
    for ball in selected_ball:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    blue_ball=random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')



"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""


from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)