import random



def print_fibonacci_pyramid(rows):
    """
    打印斐波那契数列金字塔。
    每行数字个数递增，整体居中对齐。
    :param rows: 金字塔的行数
    """
    # 计算需要的斐波那契数列长度
    total_numbers = rows * (rows + 1) // 2
    fibs = [1, 1]
    while len(fibs) < total_numbers:
        fibs.append(fibs[-1] + fibs[-2])

    idx = 0
    max_num_len = len(str(fibs[-1]))
    pyramid_width = rows * (max_num_len + 1) - 1
    for r in range(1, rows + 1):
        line_nums = fibs[idx:idx + r]
        line = ' '.join(f"{num:>{max_num_len}}" for num in line_nums)
        print(line.center(pyramid_width))
        idx += r

# 示例：打印10行斐波那契金字塔
if __name__ == "__main__":
    print_fibonacci_pyramid(10)
