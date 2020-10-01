def solution(board, moves):
    st=[0,-1]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if(board[j][i-1]==-1):
                continue
            elif (board[j][i-1]==0):
                continue
            else:
                st.append(board[j][i-1])
                board[j][i-1]=-1
                break
        if(st[-1]==st[-2]):
            st.pop()
            st.pop()
            answer=answer+2
    
    return answer
