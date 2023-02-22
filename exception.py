def handling_exception(nums):
    try:
        return int(nums[0]) // int(nums[1])
    except Exception as e:
        print("Error Code:", e)


test_time = int(input())
for i in range(test_time):
    nums = input().split()

    return_value = handling_exception(nums)

    if return_value is not None:
        print(return_value)
