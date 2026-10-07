class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		ROWS, COLUMNS = len(matrix), len(matrix[0])
		top, bot = 0, ROWS - 1
		while top <= bot:
			midRow = (top + bot) // 2
			if target > matrix[midRow][-1]:
				top = midRow + 1
			elif target < matrix[midRow][0]:
				bot = midRow - 1
			else:
				#found valid row
				break

		if not (top <= bot):
			return False

		l, r = 0, COLUMNS - 1
		row = matrix[midRow]
		while l <= r:
			mid = (l + r) // 2
			if target == row[mid]:
				return True
			elif target > row[mid]:
				l = mid + 1
			elif target < row[mid]:
				r = mid - 1
		return False