'''
-in the first tell the interviewer about the naive solution then tell him:
but in this case we will enhance the space complexity over the time complexity, so what should i do umm....
- then ask him : are u care about time complexity or the space complexity or balance between them , will say balance
- then start thinking and write the keyword and sudo code of the will u do then start
'''

# In case of (balancing) or enhancing the time complexity over the space complexity
#
array1 = ['y', 'b', 'c', 'd', 'x', 'z']
array2 = ['x', 'y', 'a', 'z']
empty_array = []


def comon_func(arr1, arr2):
    for i in arr2:
        if i in arr1:
            empty_array.append(i)
        else:
            continue
    return print(empty_array)


# in case of enhanceing the space complexity over the the time complexity
# here the BigO will be quadrtic(n^2)
'''
      for i in arr1:
        for j in arr2:
            if i==j :
                empty_array.append(i)
            else:
                continue
    return print(empty_array)
'''
comon_func(array1, array2)
