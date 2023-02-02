'''
Input: 
st = '449kghtf349khkfen99jkkidq67'
Output:
349 99
'''

st = input()
num_list = ['0','1','2','3','4','5','6','7','8','9']
n = ''
alpha = []
nums = []

for i in range(len(st)):
    if st[i] in num_list:
        n += st[i]
    else:
        alpha.append(st[i])
        if n != '':
            nums.append(int(n))
            n = ''
if n != '':
    nums.append(int(n))

l = len(nums)
if l%2 == 0:
    print(nums[l//2 - 1], nums[l//2])
else:
    print(nums[l//2])
