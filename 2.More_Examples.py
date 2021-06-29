""" More Examples: """
""" #1."""
x = 15
y = 10
print(x % y)

"""Answer = 5, Solution: whereas according to formuala (x-ny) 10-15 = 5, and if we continue to 
minus 5, 5-10 = -5, negative integers are not entertained in modulo method. thus answer is 5."""

""" #2."""

x = 85
y = 4
print(x % y)

""" Answer is 1 """ 

""" Solution: 85 - 4 = 81, 81 - 4 = 77 ... till depreciates towards 0
    I will explain the process more simpler with simple while statement"""

x = 85
y = 4
# (x-ny)
xy = 85 -1
ans = 81 # now this 81 has to depreciate, lets do that with simple while state with if condition.

while ans <= 81:
    print(ans)
    ans -= 4

    if ans == -3: # I have mentioned -3 because the last depreciated value is 1 and not 0.
        break     # -3 is the next depreciated value from 1.

""" Answer: 81
            77
            73
            69
            65
            61
            57
            53
            49
            45
            41
            37
            33
            29
            25
            21
            17
            13
            9
            5
            1 """    

