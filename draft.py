nums = [3,2,1]
done = False
for i in reversed(range(1, len(nums))):
    for j in reversed(range(0, i)):
        if nums[j] < nums[i] and not done:
            print(i)
            print(j)
            temp = nums[i]
            nums.pop(i)
            nums.insert(j, temp)
            print(nums)
            done = True
if not done:
    print(nums[::-1])