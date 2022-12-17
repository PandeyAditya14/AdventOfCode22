from common.fileOp import readFileLine

input = readFileLine('1.txt')

curMax = 0 
curSum = 0
elfs = 0
sumList = []

for calorie in input:
    if calorie == '':
        elfs+=1
        curMax = max(curMax,curSum)
        print(f"Elf {elfs} has {curSum} calories and current maximum is {curMax}")
        sumList.append(curSum)
        curSum = 0
    else:
        curSum+= int(calorie)

print (f"Maximum Calories carried by Single Elf is {curMax}")

topThree = sorted(sumList)[-3:]
print (f"Top three calorie sum are {topThree[0]}, {topThree[1]} and {topThree[2]} .... Total sum is {sum(topThree)}")