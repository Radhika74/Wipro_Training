# Q10. Write a program to find if the given number is palindrom or not.

num = int(input())
reverse = int(str(num)[::-1])

if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")