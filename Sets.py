# sets are used for storing unique elements without any particular ordering.

list = [1,1,3,3,5,8,4,5,6,8]
list_set = (set(list))
print(list_set)

## in opeartor

print(1 in list)

## add elements in sets

list_set.add(10)
print(list_set)

## sets have "pop" method, unlike lists a random element is removed as sets are unordered
list_set.pop()
print(list_set) ## randomly any element an be removed

##Solution

#C:\Users\Neha\Anaconda3\envs\myenv\python.exe "D:/Google Drive/Courses/Nanodegree_AI_foundation/Codes/Sets.py"
#{1, 3, 4, 5, 6, 8}
#True
#{1, 3, 4, 5, 6, 8, 10}
#{3, 4, 5, 6, 8, 10}