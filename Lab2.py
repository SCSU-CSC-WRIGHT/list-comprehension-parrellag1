nums = input("enter numbers seperated by spaces: ")
nums_list = nums.split(" ")
nums_list = [int(nums)]
for num in nums_list:
    if num % 2 == 0:
        print ("even")
    else:
        print ("odd")