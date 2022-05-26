
str=input("enter a string")
print(str)
index=len(str)
vowel_count= 0
print(index) 
for i in range(index):
  if str[i] in ('a','e','i','o','u','A','E','i','o','u'):
    vowel_count+=1
print("total number of vowel is :", vowel_count)

  


