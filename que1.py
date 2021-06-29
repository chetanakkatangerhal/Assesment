import sys 

def main():
    # Read string of test to be run
    print('Enter string of test to run: ')
    inputString = sys.stdin.readline()

    # String stored into list
    strintList = list(inputString)

    filterStrintList = []
    # Removed "\n" from list
    for i in strintList:
        if i == '\n':
            del i
        else:
            filterStrintList.append(i)

 
    # Sort the filterStrintList
    filterStrintList.sort()

    # Removed dublicte string element form filterStrintList
    tempList1 = []
    for i in filterStrintList:
        if i not in tempList1:
            tempList1.append(i)

    # Count how many characters available in the input string
    tempList2 = []
    for i in tempList1:
        tempList2.append(filterStrintList.count(i))


    tempList3 = []
    for i in tempList2:
        if i >= 3 :
            tempList3.append('Dynamic')
        else:
            tempList3.append('Not')


    # Result list
    Result = []
    for i in tempList3:
        if i not in Result:
            Result.append(i)

    if 'Dynamic' in Result:
        print('Dynamic')
    else:
        print('Not')
  

if __name__ == '__main__':
    main()