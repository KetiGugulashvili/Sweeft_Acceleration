Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
●       It must be greater than the original word
●       It must be the smallest word that meets the first condition
Example w = abcd
The next largest word is abdc.
Create the function bigger_Is_greater and return the new string meeting the criteria. If it is not possible, return no answer.
Function Description
Function has the following parameter(s):
    	●	string w: a word
Returns
    	- 	string: the smallest lexicographically higher string possible or no answer
Input Format
The first line of input contains T, the number of test cases. Each of the next T lines contains w.
Constraints
●   	1 ≤ T ≤ 105
●   	1 ≤ length of w ≤ 100
●   	w will contain only letters in the range ascii[a...z]
