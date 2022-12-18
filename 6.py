from common.fileOp import readFile

def runner(input):
    start_marker = 0
    tail_marker=14
    while tail_marker <= len(input):
        if len(set(input[start_marker:tail_marker])) == 14:
            return tail_marker
        start_marker+=1
        tail_marker+=1
    print("Could not find the answer")
if __name__ == "__main__":
    input = readFile('6.txt')
    print(runner(input))