'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def divmultiinrange(d,m,start,end):
    nums = []
    numss = ''
    for i in range(start,end):
        if (i%d) == 0 and (i%m) != 0:
            nums.append(str(i))
    # for n in nums:
    #     numss += f'{n}.'
    print(",".join(nums))                       # żeby użyć musiałem zamienić i na string

print(divmultiinrange(7,5,2000,3200))
