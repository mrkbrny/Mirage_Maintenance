def is_all_zero(list):
    #check if all values in list equals to 0, return False as soon as a non-0 value is found
    for num in list:
        if num != 0:
            return False
    return True

def process_history(readings):
    sequences = [readings]
    #first, build array layers until all the values of the last row equals to 0 
    reading_counter = 0
    depth = 0 #counter for sequence layer
    while not is_all_zero(sequences[-1]):
        sequences.append([])
        while reading_counter < len(sequences[depth]) - 1:
            sequences[depth+1].append(sequences[depth][reading_counter + 1] - sequences[depth][reading_counter])
            reading_counter += 1
        reading_counter = 0
        depth += 1

    #second, add a 0 at the end for placeholder for all layers
    for layer in sequences:
        layer.append(0)

    #lastly, calculate correct values placeholder values from bottom to top, until we reach the first layer
    depth = len(sequences) - 2
    while depth >= 0:
        sequences[depth][-1] = sequences[depth][-2] + sequences[depth+1][-1] 
        depth -= 1
    
    return sequences[0][-1]

def process_input(line):
    #sanitize and format input to expected format   
    input = line      
    if "\n" in input:
        #remove last character of input, it could be \n for new line
        input = input[:-1]
    input = input.split(" ")

    history = []
    try:
        for val in input:
            history.append(int(val))
    except:
        print("failed to process line: ", line)
    return history

#process each line in input.txt
input_file = 'input.txt'
sum = 0
try:
    with open(input_file) as f:
        while line := f.readline():
            sum += process_history(process_input(line))
    print(sum)
except:
    print("error with file input")