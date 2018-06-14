## Solution_1
squares = set()
# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 1
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2


for index in range(2000):
    ans = nearest_square(index)
    squares.add(ans)

print(squares)

## Solution_2
squares1 = set()
n = 1
while n**2 < 2000:
    squares1.add(n**2)
    n += 1

print(squares1)

#solution
#C:\Users\Neha\Anaconda3\envs\myenv\python.exe "D:/Google Drive/Courses/Nanodegree_AI_foundation/Codes/sets_quiz.py"
#{256, 1, 1024, 4, 900, 1156, 9, 16, 144, 400, 529, 784, 1296, 1681, 1936, 25, 289, 36, 676, 1444, 169, 49, 441, 1849, 64, 576, 961, 1089, 196, 324, 1600, 841, 1225, 81, 729, 1369, 225, 100, 484, 1764, 361, 625, 1521, 121}
#{256, 1, 1024, 4, 900, 1156, 9, 16, 144, 400, 529, 784, 1296, 1681, 1936, 25, 289, 36, 676, 1444, 169, 49, 441, 1849, 64, 576, 961, 1089, 196, 324, 1600, 841, 1225, 81, 729, 1369, 225, 100, 484, 1764, 361, 625, 1521, 121}

