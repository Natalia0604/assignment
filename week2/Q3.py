#要求三：演算法 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
#由大到小排序，找出最大值跟第二大值的數，再讓它們相乘。
def maxProduct(nums):
 re_nums = sorted(nums, reverse = True)
 result = re_nums[0] * re_nums[1]
 print("兩兩相乘的最大值為: ", result)
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值