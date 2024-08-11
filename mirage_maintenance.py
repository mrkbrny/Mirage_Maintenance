def is_all_zero(list):
    for num in list:
        if num != 0:
            return False
    return True

#history = [[0, 3, 6, 9, 12, 15]]
#history = [[1, 3, 6, 10, 15, 21]]
#history = [[10, 13, 16, 21, 30, 45]]
#history = [[-3, 8, 35, 82, 152, 255, 432, 803, 1648, 3531, 7478, 15221, 29521, 54584, 96585, 164316, 269975, 430114, 666765, 1008764, 1493294]]
#history = [[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

sum = 0
with open('input.txt') as f:
    while line := f.readline():
        input = line.split(" ")
        
        if "\n" in line:
            #remove last character of the last value, it should be \n for new line
            input[-1] = input[-1][:-1]
        else:
            print("asd")
        
        history = [[]]
        for val in input:
            history[0].append(int(val))
        #print(history)

        i = 0
        depth = 0
        #print(is_all_zero(history[-1]))
        while not is_all_zero(history[-1]):
            history.append([])
            while i < len(history[depth]) - 1:
                history[depth+1].append(history[depth][i + 1] - history[depth][i])
                i += 1
            #print(history[-1])
            i = 0
            depth += 1

        for line in history:
            line.append(0)

        depth = len(history) - 2
        while depth >= 0:
            history[depth][-1] = history[depth][-2] + history[depth+1][-1] 
            #print(history[depth])
            depth -= 1
        print(history[0][-1])
        sum += history[0][-1]

print(sum)