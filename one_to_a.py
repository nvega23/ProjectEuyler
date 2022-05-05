def titleToNumber(columnTitle: str) -> int:
    multiplier = 1
    column = 0
    for i in range(len(columnTitle)-1,-1,-1):
        column += (ord(columnTitle[i]) - 64) * multiplier
        multiplier *= 26

    return column


if __name__ == "__main__":
    comulmn = titleToNumber