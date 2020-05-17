'''
_________________________________________________|MERGE_SORT|_________________________________________-
NOTE:
'''
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left_list=merge_sort(nums[:mid])
    right_list=merge_sort(nums[mid:])
    return merge(left_list,right_list)
def merge(left_list,right_list):
    loop=True
    new_list=[]
    a=len(right_list)+len(left_list)
    while loop:
        if len(left_list)>0 and len(right_list)>0:
            if left_list[0]<=right_list[0]:
                new_list.append(left_list[0])
                left_list=left_list[1:]
            elif left_list[0]>=right_list[0]:
                new_list.append(right_list[0])
                right_list=right_list[1:]
        if len(left_list)==0:
            new_list.append(right_list[0])
            right_list=right_list[1:]
        elif len(right_list)==0:
            new_list.append(left_list[0])
            left_list=left_list[1:]

            # else:
            #     new_list.append(right_list[0])
            #     new_list.append(right_list[0])
            #     left_list=left_list[:-1]
            #     right_list=right_list[:-1]
        if len(new_list)==a:
            loop=False
            return new_list
print(merge_sort([2,3,4,6,3,2,4,53,4,2]))
'''
______________________________________________|QUICK_SORT|__________________________________________________________-
NOTE:
'''
def quick_sort(array,start,end):
    if start>=end:
        return
    p=partition(array,start,end)
    quick_sort(array,start,p-1)
    quick_sort(array,p+1,end)
def partition(array, start, end):
    pivot=array[0]
    loop=True
    index=1
    smal_array=[]
    big_array=[]
    new_array=[]
    while loop:
        if pivot<array[index]:
            big_array.append(array[index])
        elif pivot>array[index]:
            smal_array.append(array[index])
        index+=1
        if index==len(array):
            loop=False
    new_array.append(small_array)
    new_array.append(pivot)
    return small_array+big_array,len(smal_array),len(array)
    

