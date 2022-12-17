from common.fileOp import readFileLine
def returnPriorityOfChar(a):
    priority = 0
    charOrd = ord(a)
    if charOrd < ord('a') : priority = charOrd - ord('A') + 27
    else : priority = charOrd - ord('a') + 1
    return priority

def returnPriority(firstHalf,secondHalf):
    common = list(set(firstHalf)&set(secondHalf))
    priority = returnPriorityOfChar(common[0])
    print(f"First Half :{firstHalf} Second Half :{secondHalf} and common Charachter: {common[0]} with Priority as: {priority}")
    return priority

def runner(input):
    prioritySum = 0
    for rucksack in input:
        prioritySum+=returnPriority(rucksack[:len(rucksack)//2],rucksack[len(rucksack)//2:])
    return prioritySum

def badgeFinder(input):
    group = []
    sumPriority=0
    for rucksack in input:
        group.append(rucksack)
        if len(group) == 3:
            common=list(set(group[0])&set(group[1])&set(group[2]))
            priority = returnPriorityOfChar(common[0])
            print(f"Group Rucksacks \n1:{group[0]}\n2:{group[1]}\n3:{group[2]}\nCommon Charachter: {common[0]} with Priority as: {priority}\n\n")
            sumPriority+=priority
            group=[]
    
    return sumPriority



if __name__ == "__main__":
    input = readFileLine('3.txt')
    print(f"\n\n\n\nFinall Priority Sum is .................   {runner(input)}")
    print(f"Finall Group Object Priority is .................   {badgeFinder(input)}")