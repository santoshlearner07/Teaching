if __name__ == '__main__':
    N = int(input())
    newList=[]
    for i in range(N):
        array = map(str,input().split())
        array = list(array)
        if len(array) > 1 :
            for i in range(1,len(array)):
                if array[i].isdigit():
                    array[i] = int(array[i])
        if array[0].lower() == 'insert':
            newList.insert(array[1],array[2])
