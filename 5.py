from common.fileOp import readFileLine

dock = [[],[],[],[],[],[],[],[],[]]
moves = []

def buildDock(input):
    for line in range(8):
        currLine = [element[1] for element in list(input[line].replace('    ' , ' [0]').split(' '))]
        for i in range(len(currLine)):
            if currLine[i] != '0': dock[i].append(currLine[i])
    
    for line in range(10,len(input)):
        currLine = list(input[line].split(' '))
        curList=[]
        quantity , from_stack , to_stack = int(currLine[1]), int(currLine[3])-1 , int(currLine[5])-1
        curList.append(quantity)
        curList.append(from_stack)
        curList.append(to_stack)
        moves.append(curList)

def crane(): # Part 1
    for move in moves:
        quantity , from_index , to_index = move[0],move[1],move[2]
        # print("\n-----------------------------------------------------------------------")
        # print(f"Moving {dock[from_index][:quantity]} from Stack:{dock[from_index]}, Input {quantity}")
        dock[to_index] = dock[from_index][:quantity][::-1] + dock[to_index]
        dock[from_index]=dock[from_index][quantity:]
        # print(f"Result after moves \nFrom Stack:{dock[from_index]}\nTo Stack:{dock[to_index]}")
        # print("-----------------------------------------------------------------------\n")

def newCrane(): # Part 2
    for move in moves:
        quantity , from_index , to_index = move[0],move[1],move[2]
        # print("\n-----------------------------------------------------------------------")
        # print(f"Moving {dock[from_index][:quantity]} from Stack:{dock[from_index]}, Input {quantity}")
        dock[to_index] = dock[from_index][:quantity] + dock[to_index]
        dock[from_index]=dock[from_index][quantity:]
        # print(f"Result after moves \nFrom Stack:{dock[from_index]}\nTo Stack:{dock[to_index]}")
        # print("-----------------------------------------------------------------------\n")

def runner(input):
    buildDock(input)
    print("Dock Initialized")
    # for stack in dock: print(stack)
    print("Moves initialized")
    # for move in moves: print(f"Move {move[0]} boxes from stack {move[1]} to stack {move[2]}")
    # crane() # Part 1 Uncomment for Part 1
    newCrane() # Part 2 uncomment for part 2 
    print("Moves Completed")
    for stack in dock: print(stack)

    # for line in input:
        # print(line.replace('    ' , ' [0]'))
        # splittedLine = list(line.strip())
        # print(splittedLine,len(splittedLine))
    
if __name__ == "__main__":
    input = readFileLine('5.txt')
    runner(input)
    ans = "".join([stack[0] for stack in dock])
    print(f"\n\nPrinting Output {ans}")