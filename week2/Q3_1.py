# def maxProduct(nums):
#     n=[]
#     for i in nums:
#         if nums[0] < i:
#             n.append(i)
#             if nums[1] < i:

      
#     #print(nums[0])
#     print(n)

# # 請用你的程式補完這個函式的區塊
# maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
# maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
# maxProduct([10, -20, 0, -30])

def maxProduct(nums):
    #將nums由大到小排序
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j+1] > nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #將nums最前面的兩數相乘
    result= nums[0] * nums[1]
    print(result)


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


