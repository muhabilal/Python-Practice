def sum(a,b,c):
  return a+b+c
def printBoard(xState,zState):
    zero='X' if xState[0] else ('o' if zState[0] else '0')
    one='X' if xState[1] else ('o' if zState[1] else '1')
    two='X' if xState[2] else ('o' if zState[2] else '2')
    three='X' if xState[3] else ('o' if zState[3] else '3')
    four='X' if xState[4] else ('o' if zState[4] else '4')
    five='X' if xState[5] else ('o' if zState[5] else '5')
    six='X' if xState[6] else ('o' if zState[6] else '6')
    seven='X' if xState[7] else ('o' if zState[7] else '7')
    eight='X' if xState[8] else ('o' if zState[8] else '8')
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("o won the match")
            return 0
    return -1

      
if __name__=="__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("Welcome to Tic Tac Toe")
    while(True):
     printBoard(xState,zState)
     if(turn==1):
      print("X's chance")
      value=int(input("Please Enter a value :"))
      xState[value]=1
     else:
        print("o's chance")
        value=int(input("Please Enter a value :"))
        zState[value]=1
     cWin=checkWin(xState,zState)
     if(cWin!=-1):
       print("match over")
       break
     turn=1-turn
     
     