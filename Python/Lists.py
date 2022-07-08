if __name__ == '__main__':
    N = int(input())
    liste = []
    for i in range(0,N):
        inp = input()
        inpSplit = inp.split(" ")
        if(inpSplit[0] == "insert"):
            liste.insert(int(inpSplit[1]),int(inpSplit[2]))
        elif(inpSplit[0] == "remove"):
            liste.remove(int(inpSplit[1]))
        elif(inpSplit[0] == "sort"):
            liste.sort()
        elif(inpSplit[0] == "reverse"):
            liste.reverse()
        elif(inpSplit[0] == "pop"):
            liste.pop()
        elif(inpSplit[0] == "append"):
            liste.append(int(inpSplit[1]))
        elif(inpSplit[0] == "print"):
            print(liste)