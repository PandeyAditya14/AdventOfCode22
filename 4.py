from common.fileOp import readFileLine

def runner(input):
    count = 0
    for pair in input:
        range1 , range2 = pair.split(',')
        left_range1 , right_range1 = map( int , range1.split('-'))
        left_range2 , right_range2 = map( int , range2.split('-'))
        rg1 = range(left_range1,right_range1+1)
        rg2 = range(left_range2,right_range2+1)
        common = set(rg1)&set(rg2)
        if len(common) == min(len(rg1),len(rg2)): 
            count+=1
            print(f"Found complete Intersection: {pair} and common elements: {len(common)}")
    
    return count

def anyOverlap(input):
    count = 0
    for pair in input:
        range1 , range2 = pair.split(',')
        left_range1 , right_range1 = map( int , range1.split('-'))
        left_range2 , right_range2 = map( int , range2.split('-'))
        rg1 = range(left_range1,right_range1+1)
        rg2 = range(left_range2,right_range2+1)
        common = set(rg1)&set(rg2)
        if len(common) > 0: 
            count+=1
            print(f"Found Intersection: {pair} and common elements: {len(common)}")
    
    return count

if __name__ == "__main__":
    input = readFileLine('4.txt')
    print(f"\n\nFinal Number of complete Intersections: {runner(input)}")
    print(f"\n\nFinal Number of Intersections: {anyOverlap(input)}")