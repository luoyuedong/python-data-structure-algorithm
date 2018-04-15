def isHuiWen(str):
    if(len(str)<2):
        return True
    if (str[0]!=str[-1]):
        return False
    return isHuiWen(str[1:-1])


if __name__ == '__main__':
    str = input("输入一个字符串:")
    if isHuiWen(str):
        print("该字符串是回文的")
    else:
        print("该字符串不是回文的")
