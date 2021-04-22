file1 = open("C:\Python_Project\Input_file.txt", "r")
file2 = open("C:\Python_Project\Output_file.txt", "w")

prev_line_1, prev_line_2, prev_line_3, prev_line_4 = "", "", "", ""

for line in file1.readlines():
    print("Current Line :" + line)
    print("Previous Line :" + prev_line_1 + '|' + prev_line_2)
    items = line.split('|')
    print("--------- ------------- --------------------")
    if items[0] == prev_line_1 and items[1] == prev_line_2:
        items[3] = str(items[3]) + ',' + prev_line_4
    elif prev_line_1 == '':
        pass
    else:
        file2.write(prev_line_1 + '|' + prev_line_2 + '|' + prev_line_3 + '|' + prev_line_4)

    prev_line_1 = items[0]
    prev_line_2 = items[1]
    prev_line_3 = items[2]
    prev_line_4 = items[3]

file1.close()
file2.close()