# Week 01: Python 基础语法

本周目标：从 C++ 思维切换到 Python 思维，能写简单脚本，能运行代码，能把练习和笔记提交到 GitHub。

现有代码的配套笔记见 [练习索引](练习索引.md)，更完整的主题笔记见 [Python 基础](../python_basic/README.md)。

## VS Code 学习方式

每天先打开 Anaconda Prompt：

```bash
cd /d D:\ai-python-learning-1
conda activate ai-python
code .
```

在 VS Code 中选择“终端 → 新建终端”，运行当天代码。

## 学习资料

- 廖雪峰 Python 教程：基础语法、函数、错误调试、IO 编程
- 莫烦 Python：Python 基础部分

## 每天任务

| 天数 | 学习主题 | 练习文件 | 运行命令 |
| --- | --- | --- | --- |
| Day 1 | print / input / 变量 / 基本类型 | `code1/day1_basic.py`、`code1/print_input.py` | `python week01-python-basics/code1/day1_basic.py` |
| Day 2 | 字符串 | `code1/string.py` | `python week01-python-basics/code1/string.py` |
| Day 3 | list / tuple | `code1/list.py`、`code1/tuple.py` | `python week01-python-basics/code1/list.py` |
| Day 4 | dict / set | `code1/dict_set.py` | `python week01-python-basics/code1/dict_set.py` |
| Day 5 | if / for / while | `code1/if_loop.py` | `python week01-python-basics/code1/if_loop.py` |
| Day 6 | 函数 | `code1/function.py` | `python week01-python-basics/code1/function.py` |
| Day 7 | 综合练习和整理 | `code1/student_summary.py`、`notes.md` | `python week01-python-basics/code1/student_summary.py` |

## 每天固定流程

```text
看教程 30-60 分钟
写当天练习文件
运行代码并修改 2-3 次
把收获和报错写进 notes.md
git add / commit / push
```

提交示例：

```bash
git status
git add .
git commit -m "week01 update day1 practice"
git push
```

## 本周产出

```text
week01-python-basics/
  README.md
  notes.md
  code1/
    day1_basic.py
    print_input.py
    string.py
    list.py
    tuple.py
    dict_set.py
    if_loop.py
    function.py
    student_summary.py
```
