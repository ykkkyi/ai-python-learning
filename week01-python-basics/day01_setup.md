# Day 1 Setup: Windows 环境配置

初次配置时的历史检查记录：

- Git: 已安装
- Python: 当前终端无法识别 `python`
- Conda: 当前终端无法识别 `conda`

这些记录不代表当前环境状态。当前学习环境为 Anaconda 下的 `ai-python`；优先在 Anaconda Prompt 中执行 `conda activate ai-python`，并在 VS Code 中选择该环境的解释器。普通终端无法识别命令时，也可能只是 PATH 尚未配置。

## 推荐安装方式

建议安装 Miniconda，原因是它比 Anaconda 更轻，后续需要什么包再安装什么包，更适合学习和科研环境管理。

官方下载页：

- https://www.anaconda.com/download/success

在页面中选择：

```text
Miniconda
Windows
64-Bit Graphical Installer
```

安装时建议：

```text
Install for: Just Me
安装路径：默认即可
勾选：Register Miniconda as my default Python
不要强行勾选 Add to PATH，除非你知道自己在做什么
```

安装完成后，打开：

```text
Anaconda Prompt 或 Miniconda Prompt
```

检查：

```bash
python --version
conda --version
git --version
```

## 创建本仓库的学习环境

在 Anaconda Prompt / Miniconda Prompt 中进入仓库目录：

```bash
cd /d D:\ai-python-learning-1
```

创建环境：

```bash
conda create -n ai-python python=3.11
conda activate ai-python
```

运行第一个脚本：

```bash
python week01-python-basics/basic_syntax.py
python week01-python-basics/word_count.py
python week01-python-basics/student_score.py
```

## 今天要提交的内容

运行成功后执行：

```bash
git status
git add .
git commit -m "week01 initialize python basics"
```

如果你已经在 GitHub 创建了远程仓库，再执行：

```bash
git branch -M main
git remote add origin https://github.com/你的用户名/ai-python-learning.git
git push -u origin main
```
