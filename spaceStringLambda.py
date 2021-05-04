#! python3

userStr = input('Please enter a string to be spaced:\n')
print('\nYour spaced string is:\n'+
      (lambda userStr: ''.join([char + ' ' 
                                for char in userStr 
                                if char != ' ']).strip())(userStr))
