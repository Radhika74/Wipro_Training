'''Project 1: Happiness Calculator
Stream: Python | Tech Module: Command Line Arguments
Question: Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.
Third string contains the numbers given to you. Your initial happiness is 0. When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Sample Input 1: 3-1 5-7 1-5-3-8
Sample Output 1: 1
Explanation:

Numbers in string 1: 3, 1
Numbers in string 2: 5, 7
Numbers given to you: 1, 5, 3, 8
You gain 1 unit of happiness for numbers 1 and 3 which are in string 1. Your total happiness is 2 now.
You lose 1 unit of happiness for number 5 which is in string 2. Your total happiness is 1 now.
8 is not present in either of the strings, so your happiness does not change.
Final happiness is 1.

Sample Input 2: 60-77-34-5-2 44-11-99-3 77-15-13-2-34-3
Sample Output 2: 2
Explanation:

You gain 1 unit of happiness for numbers 77, 2 and 34 which are in string 1. Your total happiness is 3 now.
You lose 1 unit of happiness for number 3 which is in string 2. Your total happiness is 2 now.
15 and 13 are not present in either of the strings, so your happiness does not change.
Final happiness is 2.'''

import sys

def calculate_happiness(like_str, dislike_str, input_str):
    like = set(map(int, like_str.split('-')))
    dislike = set(map(int, dislike_str.split('-')))
    input_numbers = list(map(int, input_str.split('-')))

    happiness = 0
    for num in input_numbers:
        if num in like:
            happiness += 1
        elif num in dislike:
            happiness -= 1

    return happiness

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python happiness_calculator.py <like_string> <dislike_string> <input_string>")
        sys.exit(1)

    like_str = sys.argv[1]
    dislike_str = sys.argv[2]
    input_str = sys.argv[3]

    result = calculate_happiness(like_str, dislike_str, input_str)
    print(result)
