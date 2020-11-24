#! python3
import re, pyperclip
#Create a regex for phone numbers

phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, x12345

(
 ((\d\d\d) | (\(\d\d\d\)))?      # area code (optional)
        
 (\s|-)                 # First seperator
 \d\d\d                 # First 3 digits
 -                      # Seperator
 \d\d\d\d               # Last 4 Digits
 (((ext(\.)?\s) |x)     # Extension (Optional)
 (\d{2,5}))?
)

''', re.VERBOSE)

#Create a regex for email addresses

emailRegex = re.compile(r'''
# some.+thing@something.com
            
[a-zA-Z0-9_.+]+            # name part
@                            # @ symbol
[a-zA-Z0-9_.+]+             # Domain name


''', re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' +'\n'.join(extractedEmail)
print(results)