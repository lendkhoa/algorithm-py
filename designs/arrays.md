# Move positive elements to the front
⭐️ The order of the even and odd numbers are not guaranteed <br>

```py
def even_odd(nums: List[int]) -> None:
	l = 0
	r = len(nums) - 1
	# Anything on the left side of left is even
	while l < r:
		if nums[l] % 2 == 0:
			l += 1
		else:
			nums[l], nums[r] = nums[r], nums[l]
			r -= 1
	print(nums)
```
Similar variant, move negatives to front <br>
```py
def negative_front(nums: List[int]) -> None:
	l = 0
	r = len(nums) - 1
	# Anything on the left side of left is even
	while l < r:
		if nums[l] < 0:
			l += 1
		else:
			nums[l], nums[r] = nums[r], nums[l]
			r -= 1
	print(nums)
```