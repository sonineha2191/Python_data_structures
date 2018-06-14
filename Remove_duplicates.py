 # Define the remove_duplicates function

 ##  method_1:using for
def remove_duplicates(list):
    """
    I need to check and remove for duplicate elements in list and save the unique items to new_list
    """
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list

#list=[‘a’,‘b’,‘b’,‘c’,‘s’,‘k’,‘h’]
list = [1,1,3,3,5,8,4,5,6,8]
new_list=remove_duplicates(list)
print(new_list)

## method_2: using sets
list = [1,1,3,3,5,8,4,5,6,8]
print(set(list))

#solution

#C:\Users\Neha\Anaconda3\envs\myenv\python.exe "D:/Google Drive/Courses/Nanodegree_AI_foundation/Codes/Remove_duplicates.py"
#[1, 3, 5, 8, 4, 6]
#{1, 3, 4, 5, 6, 8}