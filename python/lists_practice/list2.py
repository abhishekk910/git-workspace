list1 = [1,2,3,2,1]
list2 = [1,3,2,2,1]

if len(list1) == len(list2):
    nums1 = {}
    nums2 = {}
    for i in list1:
        if i not in nums1:
            nums1[i] = list1.count(i)
        if i not in nums2:
            nums2[i] = list2.count(i)
    print(nums1)
    print(nums2)
    if nums1 == nums2:
        print("Both Lists are Equal")
    else:
        print("Both Lists are not equal")







        


