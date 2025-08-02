'''import re
text='hi students !!'
se=r'how'
output=re.match(se,text)
if output:
    print('mathc found for:',output.group())

else:
    print('no match...')''' 

import re
text='my number is 229'
match=re.search(r'\d+',text)
print(match.group())
