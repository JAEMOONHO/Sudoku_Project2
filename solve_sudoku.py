def solve_sudoku(board):
    # 빈 위치 찾기
    empty_loc = find_empty_location(board)

    if not empty_loc: # 빈 위치가 없으면, not None = True
        return True # 다 풀었다, 끝!

    # 빈 위치가 있으면,
    row, col = empty_loc
    
    # 빈값에 1~9를 다 넣어보면서, 유효한 값을 찾는다.
    for num in range(1, 10):
        # 3가지 규칙이 맞을 때,
        if is_valid(board, row, col, num):
            board[row][col] = num   # 유효하면, 대입!

            ########## 재귀 (recursive) 함수 ##########
            # 위 규칙에 의거, 값을 채워 넣었는데, 결국 스도쿠를 해결하지 못했다면,
            if solve_sudoku(board):
                return True
            
            # 무르기 (풀 수 없는 수도쿠가 입력으로 들어 올 수 있기 때문!)
            board[row][col] = 0
            ###########################################
        
    return False # 이 경로로는 해결 불가