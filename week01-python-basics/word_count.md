# 从文件统计词频

[对应练习代码](<word_count.py>)

### 思路与知识点

使用 `pathlib` 定位同目录的文本文件，统一大小写、分词并去掉单词两端的常见标点，最后按次数降序输出。

### 运行说明与易错点

文件路径基于 `__file__`，不依赖终端当前目录。这里只做空白分词，不适用于中文分词，也不会去掉单词内部的标点。

### 练习代码

```python
from pathlib import Path


def count_words(text):
    words = text.lower().split()
    result = {}
    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if not word:
            continue
        result[word] = result.get(word, 0) + 1
    return result


def main():
    file_path = Path(__file__).with_name("sample_text.txt")
    text = file_path.read_text(encoding="utf-8")
    counts = count_words(text)

    for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```

### 检查结果

运行时读取 [sample_text.txt](sample_text.txt)。用 `count_words('Python, python!')` 检查函数，应得到 `{'python': 2}`。
