#要求二：Python 字典與列表、JavaScript 物件與陣列 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
# 請用你的程式補完這個函式的區塊
  sum=0
  average=0
  e_dict=[]
  for i in data["employees"]:
    e_dict=i
    sum+=e_dict["salary"]
    average=sum / data["count"]
  print(data["count"], "人的平均薪資為: ", "{:.2f}".format(average), "元") #取到小數點後2位
  
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式