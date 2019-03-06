# Using python 3.6.6

# Soln 1
# Time Complexity: O(n^2)
# Space Complexity: O(1)
input_list = [10, 15, 3,7]
k = 17

def check_pair_sum(input_list, k):
	for i in range(len(input_list)):
		for j in range(i+1, len(input_list)):
			if (input_list[i] + input_list[j]) == k:
				return True
	return False

print(check_pair_sum(input_list, k))

k2 = 16
print(check_pair_sum(input_list, k2))

# Soln 2
# Time Complexity: O(n)
# Space Complexity: O(n)
def check_pair_sum(input_list, k):
	for i in range(len(input_list)):
		if k - input_list[i] in input_list:
			return True
	return False

# Soln 3
# One pass using set
def check_pair_sum(input_list, k):
	s = set()
	for i in input_list:
		if k - i in s:
			return True
		s.add(i)
	return False

# Ref. https://leetcode.com/articles/two-sum/