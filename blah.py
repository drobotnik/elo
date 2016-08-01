with open('text_num.txt', 'r') as f:
    contents = f.read()
    num = int(contents)
    print(num)


with open('text_num.txt', 'w') as f:
    f.write(str(num - 1))

