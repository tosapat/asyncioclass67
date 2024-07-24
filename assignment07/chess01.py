import time


my_compute_time = 0.1  
opponent_compute_time = 0.5   
move_pairs = 30
opponents = 24

def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1}:{i+1} 1 move.")
        time.sleep(opponent_compute_time)
        print(f"BOARD-{x+1}:{i+1} 2 move.")
    
    print(f"BOARD{x+1}- >>>>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter()- board_start_time)}sec\n")
    return round(time.perf_counter()-board_start_time)

if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
        print(f"Total time elapsed up to board {board + 1}: {board_time} sec\n")
    
    
    print(f"Chess finished in {board_time} sec.")
    print(f"finished in {round(time.perf_counter()- start_time)} sec.")
