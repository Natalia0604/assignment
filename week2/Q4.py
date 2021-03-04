#要求四 ( 請閱讀英文 )：演算法 Given an array of integers, show indices(複數) of the two numbers such that they add up to a 
# specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice
def twoSum(nums, target):
# your code here
  #找出相加起來會等於target的數字，append to list b
  b=[]
  result=[]
  for i in nums:
    for j in nums:
      if i != j: #排除使用同個數字兩次
        if i + j == target:
          b.append(i) #i和j會重複計算，只要append其中1組就好
        else:
          continue
  #顯示兩數在nums 的 index
  for i in nums:
    if i in b:
      index=nums.index(i)
      result.append(index)
  return result
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9