def maxProduct(nums):
    #將nums由大到小排序
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j+1] > nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #將nums最前面的兩數相乘
   
    if (nums[0] * nums[1]) > nums[-1] * nums[-2]:
        result= nums[0] * nums[1]
    else:
         result= nums[-1] * nums[-2]
    print(result)


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([-10,-20,1,2]) # 得到 200 因為 -10 和 -20 相乘得到最大值