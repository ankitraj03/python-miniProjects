import re

message=input()

#
phoneRegex = re.compile(r'''(
             (\d{3})?
            (\s|-|\.)?
            \d{3}
             (\s|-|\.)
              \d{4}            
    )''',re.VERBOSE)

emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      
   @                     
  [a-zA-Z0-9.-]+         
    (\.[a-zA-Z]{2,4})       
    )''', re.VERBOSE)


phonenum=phoneRegex.search(message)
emailadd=emailRegex.search(message)

print(phonenum)
print(emailadd)
