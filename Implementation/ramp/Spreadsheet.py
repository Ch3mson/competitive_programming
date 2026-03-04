"""
Implement a spreadsheet with two methods: setCell and getCell. setCell should support setting a cell's value to a number or a formula. getCell should return the value of a cell.

Example:

setCell('A1' 1)
setCell('B1', 2)
setCell('C1', '=2*B1)
setCell('D1', '=C1+B1')
setCell('E1', '=D1+C1')
getCell('E1')

Only consider operations: "+, -, *, /" and the number of operands are 2. The type in a cell might be a numeral, character or a formula starting with =.

Followup: How to optimize the complexity so each cell is only computed once? How to ensure the expression is valid?
"""

# [VAL] [op] [VAL]
# can there be a mix of cells & numbers? (yes)
# [Number] op [Cell]
# [Number] op [Number]
# [Cell] op [Cell]

# references exist? (i.e. A1 -> B1)
#   yes

# with there be cycles? no 
# is it possible that cells can have more than a length of 2? (i.e. A22, for example? )
#    yes 

# will formulas always start with =? 
#    yes

# do i have to deal with 0 dvision edge case (8 / 0) -> assume no


# cases
# formulas: 
# [Number] op [Cell]
# [Number] op [Number]
# [Cell] op [Cell]

# integers 
# references 
# dependencies between different formulas 
# ensure that we can handle cells of different lengths 

# approach 
# 1. data members
#  hash map representing the spreadsheet 
#  key: cell 
#  value: formula, integer or reference 

# 2. set function:
#  update the hash map with the given key-value pair 

# 3. get function:
# check the data type - if it is an integer, return the value right away (no reference or formula)
# otherwise, check if the first value is an equal sign
#   if its not, we know its a reference to another cell -> call the get function on this cell 

# otherwise, process the formula (ignore the first digit)
# split the formula into two portions (on opposite sides of the operator)
# then if it is an integer/digit, then we will cast the value to an integer 
# otherwise, we will call get to fetch the value associated with this integer 

from collections import defaultdict

import unittest

_FORMULA = "="

class Spreadsheet:
	def __init__(self) -> None:
		self.spreadsheet = {}
		self.cache = {}
		self.dependencies = defaultdict(list)
		self.operators = {"+", "-", "*", "/"}
	
	def set(self, key: str, value: int | str):
		self.clear_cache(key)
		self.spreadsheet[key] = value 
	
	def get(self, key: str):
		if key not in self.spreadsheet:
			return None 

		if key in self.cache:
			print(f"Using the cache for {key}")
			return self.cache[key]

		value = self.spreadsheet[key]

		if isinstance(value, int):
			return value 
		
		if value[0] != _FORMULA:
			self.dependencies[value].append(key)

		final_result = self.get(value) if value[0] != _FORMULA else self.process_formula(key, value[1:]) 
		self.cache[key] = final_result
		return final_result
	
	def process_formula(self, key: str, formula: str):
		left, right = "", "" 

		for i, c in enumerate(formula):
			if c in self.operators:
				right = formula[i+1:]
				self.update_formula_dependencies(key, left, right)
				return self.calculate_formula(left, right, c)
			
			else:
				left += c
		
		return None
	
	def calculate_formula(self, val1: str, val2: str, operator: str):
		val1 = int(val1) if val1.isdigit() else self.get(val1) # either a number or a cell
		val2 = int(val2) if val2.isdigit() else self.get(val2)

		match operator:
			case "+":
				return val1 + val2

			case "-":
				return val1 - val2

			case "*":
				return val1 * val2

			case "/":
				return val1 / val2

			case _:
				return 0
	
	def update_formula_dependencies(self, key: str, val1: str, val2: str):
		if not val1.isdigit(): 
			self.dependencies[val1].append(key)
		
		if not val2.isdigit(): 
			self.dependencies[val2].append(key)
	
	def clear_cache(self, key: str):
		if key not in self.cache:
			return 
		
		for dependency in self.dependencies[key]:
			self.clear_cache(dependency)
	
		self.cache.pop(key)

class TestSpreadsheet(unittest.TestCase):
	def setup(self):
		self.app = Spreadsheet()
		self.app.set("A1", 2)
		self.app.set("B1", 3)
		self.app.set("C1", "A1")
		self.app.set("D1", "B1")
		self.app.set("C2", "=2+3")
		self.app.set("D2", "=2*3")
		self.app.set("E2", "=2-3")
		self.app.set("F2", "=3/2")
		self.app.set("C10", "=2+A1")
		self.app.set("D10", "=2*A1")
		self.app.set("E10", "=2-A1")
		self.app.set("F10", "=2/A1")
		self.app.set("C15", "=B1+A1")
		self.app.set("D15", "=C1*A1")
		self.app.set("E15", "=C15-A1")
		self.app.set("F15", "=D15/A1")
	
	def test_integers(self):
		self.setup()
		assert self.app.get("A1") == 2
		assert self.app.get("B1") == 3
	
	def test_associations(self):
		self.setup()
		assert self.app.get("C1") == 2
		assert self.app.get("D1") == 3
	
	def test_int_formulas(self):
		self.setup()
		assert self.app.get("C2") == 5
		assert self.app.get("D2") == 6
		assert self.app.get("E2") == -1
		assert self.app.get("F2") == 1.5
		assert self.app.get("F2") == 1.5

	def test_combination_formulas(self):
		self.setup()
		assert self.app.get("C10") == 4
		assert self.app.get("D10") == 4 
		assert self.app.get("E10") == 0
		assert self.app.get("F10") == 1
	
	def test_cell_formulas(self):
		self.setup()
		assert self.app.get("C15") == 5
		assert self.app.get("D15") == 4 
		assert self.app.get("E15") == 3
		assert self.app.get("F15") == 2
	
	def test_unexistent_cells(self):
		self.setup()
		assert self.app.get("A200") == None
	
	def test_cache_update(self):
		self.setup()
		assert self.app.get("F2") == 1.5
		assert self.app.get("F2") == 1.5
		
		self.app.set("F2", "A1")
		assert self.app.get("F2") == 2
		assert self.app.get("F2") == 2


if __name__ == "__main__":
	unittest.main()



