#You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
#'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely 
#and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each 
#move consists of turning one wheel one slot. The lock initially starts at 
#'0000', a string representing the state of the 4 wheels. You are given a list 
#of deadends dead ends, meaning if the lock displays any of these codes, the 
#wheels of the lock will stop turning and you will be unable to open it.
#Given a target representing the value of the wheels that will unlock 
#the lock, return the minimum total number of turns required to open the 
#lock, or -1 if it is impossible.

#approach: breadth-first search (BFS): suitable for finding the shrotest path in unweighted graphs, which fits this problem
#well. traverse the possible combinations of the lock one by one, keeping track of the number of moves required to reach
#each combination. continue in a level-by-level manner until reached the target combination or all possibilities are exhausted.
from queue import deque

def openLock(deadends, target):
    queue = deque()
    
    deadends = set(deadends)
    if "0000" not in deadends:
        deadends.add("0000")
        queue.append(("0000",0))
    
    while queue:
        curr_combination, moves = queue.popleft()
        if curr_combination == target:
            return moves

        for i in range(4):
            #move wheel at index forward#
            new_combination = curr_combination[:i] + str((int(curr_combination[i])+1)%10) + curr_combination[i+1:]
            if new_combination not in deadends:
                deadends.add(new_combination)
                queue.append((new_combination, moves+1))

            #move wheel at index backward#
            new_combination = curr_combination[:i] + str((int(curr_combination[i])-1)%10) + curr_combination[i+1:]
            if new_combination not in deadends:
                deadends.add(new_combination)
                queue.append((new_combination, moves+1))
    return -1


#inputs#
deadends = ['0201','0101','0102','1212','2002']
target = '0202'
print(openLock(deadends, target))