#盤面を表示する
def printBoard(board):
    for i in range(len(board)):
        print(*board[i],sep='')


#指定場所に置けるか置けないかを探索
def search(board,x,y,player):
    if board[x*2][y*2]!='　':  #すでに駒があったら探索終了
        return False
    flag=False

    if player==0:
        sign='●'   #プレイヤー側ではない駒
        correct='○'#プレイヤー側の駒
    else:
        sign='○'   #プレイヤー側ではない駒
        correct='●'#プレイヤー側の駒

    if x>1:
        if y>1:
            if board[(x-1)*2][(y-1)*2]==sign:#指定の左上を探索
                flagLoop=False
                for i in range(2,min(x,y)):
                    if board[(x-i)*2][(y-i)*2]==sign:
                        continue
                    elif board[(x-i)*2][(y-i)*2]==correct:#探索列に自駒があればループ終了
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):  #あいだの駒を自駒の色にする
                        board[(x-i)*2][(y-i)*2]=correct

        if board[(x-1)*2][y*2]==sign:#指定の上を探索
            flagLoop=False
            for i in range(2,x):
                if board[(x-i)*2][y*2]==sign:
                    continue
                elif board[(x-i)*2][y*2]==correct:#探索列に自駒があればループ終了
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):  #あいだの駒を自駒の色にする
                    board[(x-i)*2][y*2]=correct

        if y<8:
            if board[(x-1)*2][(y+1)*2]==sign:#指定の右上を探索
                flagLoop=False
                for i in range(2,min(x,8-y+1)):
                    if board[(x-i)*2][(y+i)*2]==sign:
                        continue
                    elif board[(x-i)*2][(y+i)*2]==correct:#探索列に自駒があればループ終了
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):  #あいだの駒を自駒の色にする
                        board[(x-i)*2][(y+i)*2]=correct


    if y>1:
        if board[x*2][(y-1)*2]==sign:#指定の左を探索
            flagLoop=False
            for i in range(2,y):
                if board[x*2][(y-i)*2]==sign:
                    continue
                elif board[x*2][(y-i)*2]==correct:#探索列に自駒があればループ終了
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):  #あいだの駒を自駒の色にする
                    board[x*2][(y-i)*2]=correct

    if y<8:
        if board[x*2][(y+1)*2]==sign:#指定の右を探索
            flagLoop=False
            for i in range(2,8-y+1):
                if board[x*2][(y+i)*2]==sign:
                    continue
                elif board[x*2][(y+i)*2]==correct:#探索列に自駒があればループ終了
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):  #あいだの駒を自駒の色にする
                    board[x*2][(y+i)*2]=correct


    if x<8:
        if y>1:
            if board[(x+1)*2][(y-1)*2]==sign:#指定の左下を探索
                flagLoop=False
                for i in range(2,min(8-x+1,y)):
                    if board[(x+i)*2][(y-i)*2]==sign:
                        continue
                    elif board[(x+i)*2][(y-i)*2]==correct:#探索列に自駒があればループ終了
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):  #あいだの駒を自駒の色にする
                        board[(x+i)*2][(y-i)*2]=correct

        if board[(x+1)*2][y*2]==sign:#指定の下を探索
            flagLoop=False
            for i in range(2,8-x+1):
                if board[(x+i)*2][y*2]==sign:
                    continue
                elif board[(x+i)*2][y*2]==correct:#探索列に自駒があればループ終了
                    flagLoop=True
                    index=i
                    break
                else:
                    break
            if flagLoop==True:
                flag=True
                for i in range(1,index):  #あいだの駒を自駒の色にする
                    board[(x+i)*2][y*2]=correct

        if y<8:
            if board[(x+1)*2][(y+1)*2]==sign:#指定の右下を探索
                flagLoop=False
                for i in range(2,min(8-x+1,8-y+1)):
                    if board[(x+i)*2][(y+i)*2]==sign:
                        continue
                    elif board[(x+i)*2][(y+i)*2]==correct:#探索列に自駒があればループ終了
                        flagLoop=True
                        index=i
                        break
                    else:
                        break
                if flagLoop==True:
                    flag=True
                    for i in range(1,index):  #あいだの駒を自駒の色にする
                        board[(x+i)*2][(y+i)*2]=correct
    
    if flag==True:#探索の結果、置ける場合置く
        board[x*2][y*2]=correct

    return flag



def main():
    #初期オセロ盤面の作成
    board=[['  1','  2','  3','  4','  5','  6','  7','  8'],[' +--','+--','+--','+--','+--','+--','+--','+--','+']]
    for i in range(8):
        vertical=[i+1,'|','　','|','　','|','　','|','　','|','　','|','　','|','　','|','　','|']
        horizontal=[' +--','+--','+--','+--','+--','+--','+--','+--','+']
        board.append(vertical)
        board.append(horizontal)
    board[4*2][4*2],board[5*2][5*2]='●','●'
    board[4*2][5*2],board[5*2][4*2]='○','○'

    printBoard(board)

    player=0    #先行プレイヤーの設定
    color=['黒','白']#先行：黒　後攻：白
    loop=1
    while loop<=60:  #盤面がすべて埋まったらループ終了
        print('プレイヤー',player+1,'(',color[player],')：座標を入力してください')
        print('縦　横 :',end='')
        x,y=map(int,input().split())

        if 1<=x<=8 and 1<=y<=8:         #指定場所が盤面内の場合
            if search(board,x,y,player):#置けるかどうかを探索して True の場合
                printBoard(board)
                player=(player+1)%2     #プレイヤーを交代
                loop+=1                 #盤面に置いたコマの数をプラス
            else:                       #置けない場所の場合
                print('そこには置けません')
        else:                           #指定場所が盤面外の場合
            print('指定された座標は範囲外です')

    print('--------ゲーム終了！--------')
    black=0  #黒駒の数
    white=0  #白駒の数
    for i in range(1,9):
        for j in range(1,9):
            if board[i*2][j*2]=='○':  #黒駒の場合
                black+=1
            elif board[i*2][j*2]=='●':#白駒の場合
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