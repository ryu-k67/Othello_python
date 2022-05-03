def printBoard(board):
    for i in range(len(board)):
        print(*board[i],sep='')


def search(board,x,y,player):
    if board[x*2][y*2]!='　':
        return False
    flag=False
    if player==0:
        sign='●'
        correct='○'
    else:
        sign='○'
        correct='●'

    if x>1:
        if y>1:
            if board[(x-1)*2][(y-1)*2]==sign:
                flagLoop=False
                for i in range(2,min(x,y)):
                    if board[(x-i)*2][(y-i)*2]==sign:
                        continue
                    elif board[(x-i)*2][(y-i)*2]==correct:
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):
                        board[(x-i)*2][(y-i)*2]=correct

        if board[(x-1)*2][y*2]==sign:
            flagLoop=False
            for i in range(2,x):
                if board[(x-i)*2][y*2]==sign:
                    continue
                elif board[(x-i)*2][y*2]==correct:
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):
                    board[(x-i)*2][y*2]=correct

        if y<8:
            if board[(x-1)*2][(y+1)*2]==sign:
                flagLoop=False
                for i in range(2,min(x,8-y+1)):
                    if board[(x-i)*2][(y+i)*2]==sign:
                        continue
                    elif board[(x-i)*2][(y+i)*2]==correct:
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):
                        board[(x-i)*2][(y+i)*2]=correct


    if y>1:
        if board[x*2][(y-1)*2]==sign:
            flagLoop=False
            for i in range(2,y):
                if board[x*2][(y-i)*2]==sign:
                    continue
                elif board[x*2][(y-i)*2]==correct:
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):
                    board[x*2][(y-i)*2]=correct

    if y<8:
        if board[x*2][(y+1)*2]==sign:
            flagLoop=False
            for i in range(2,8-y+1):
                if board[x*2][(y+i)*2]==sign:
                    continue
                elif board[x*2][(y+i)*2]==correct:
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):
                    board[x*2][(y+i)*2]=correct


    if x<8:
        if y>1:
            if board[(x+1)*2][(y-1)*2]==sign:
                flagLoop=False
                for i in range(2,min(8-x+1,y)):
                    if board[(x+i)*2][(y-i)*2]==sign:
                        continue
                    elif board[(x+i)*2][(y-i)*2]==correct:
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):
                        board[(x+i)*2][(y-i)*2]=correct

        if board[(x+1)*2][y*2]==sign:
            flagLoop=False
            for i in range(2,8-x+1):
                if board[(x+i)*2][y*2]==sign:
                    continue
                elif board[(x+i)*2][y*2]==correct:
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):
                    board[(x+i)*2][y*2]=correct

        if y<8:
            if board[(x+1)*2][(y+1)*2]==sign:
                flagLoop=False
                for i in range(2,min(8-x+1,8-y+1)):
                    if board[(x+i)*2][(y+i)*2]==sign:
                        continue
                    elif board[(x+i)*2][(y+i)*2]==correct:
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):
                        board[(x+i)*2][(y+i)*2]=correct
    
    if flag==True:
        board[x*2][y*2]=correct

    return flag


def main():
    board=[['  1','  2','  3','  4','  5','  6','  7','  8'],[' +--','+--','+--','+--','+--','+--','+--','+--','+']]
    for i in range(8):
        vertical=[i+1,'|','　','|','　','|','　','|','　','|','　','|','　','|','　','|','　','|']
        horizontal=[' +--','+--','+--','+--','+--','+--','+--','+--','+']
        board.append(vertical)
        board.append(horizontal)
    board[4*2][4*2],board[5*2][5*2]='●','●'
    board[4*2][5*2],board[5*2][4*2]='○','○'

    printBoard(board)

    player=0
    color=['黒','白']
    loop=1
    while loop<=60:
        print('プレイヤー',player+1,'(',color[player],')：座標を入力してください')
        print('縦　横 :',end='')
        x,y=map(int,input().split())

        if 1<=x<=8 and 1<=y<=8:
            if search(board,x,y,player):
                printBoard(board)
                player=(player+1)%2
                loop+=1
            else:
                print('そこには置けません')
        else:
            print('指定された座標は範囲外です')

    print('--------ゲーム終了！--------')
    black=0
    white=0
    for i in range(1,9):
        for j in range(1,9):
            if board[i*2][j*2]=='○':
                black+=1
            elif board[i*2][j*2]=='●':
                white+=1
    print('プレイヤー1：',black,'枚\nプレイヤー2；',white,'枚')
    if black>white:
        print('プレイヤー1の勝利！')
    elif black<white:
        print('プレイヤー2の勝利！')
    else:
        print('引き分け！')


if __name__=="__main__":
    main()