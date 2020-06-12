import string 
import collections

mandatory_violation = False

##TODO: concatenate all the strings

def password_rules(password):
    # format for strengths and weaknesses. the default value is False.
    weaknesses = [['All letters:', 'False'], #0
                  ['All digits','False'], #1
                  ['Repeated characters:', 'False'], #2
                  ['Consecutive uppercase letters','False'], #3
                  ['Consecutive lowercase letters:', 'False'], #4
                  ['Consecutive digits','False'], #5
                  ['Sequential letters:', 'False'], #6
                  ['Sequential digits','False']] #7

    strengths = [['Length:', "False"], #0
                 ['Upper case letters',"False"], #1
                 ['Lower case letters:', "False"], #2
                 ['Digits', "False"], #3
                 ['Symbols:', "False"], #4
                 ['Digits & Symbols in the middle',"False"]] #5

    score = 0
    popup_msg="Password accepted"
    mandatory_violation = False

    # mandatory requirements check
    if (len(password)>=8):
        score += (len(password)*4)
        strengths[0][1] = 'True'
    else:
        popup_msg="Password is too short\nPlease check the analysis for correction"
        mandatory_violation = True

    if any(x.isupper()for x in password):
        num_of_upper = [x for x in password if x.isupper()]
        score += (len(num_of_upper)*2)
        strengths[1][1] = 'True'
    else:
        popup_msg="Password contains no upper class letters\nPlease check the analysis for correction"
        mandatory_violation = True

    if any(x.islower()for x in password):
        num_of_lower = [x for x in password if x.islower()]
        score += (len(num_of_lower)*2)
        strengths[2][1] = 'True'
    else:
        popup_msg="Password contains no lower class letters\nPlease check the analysis for correction"
        mandatory_violation = True

    if any(x.isdigit()for x in password):
        num_of_digits = [x for x in password if x.isdigit()]
        score += (len(num_of_digits)*4)
        strengths[3][1] = 'True'
    else:
        popup_msg="Password contains no digits\nPlease check the analysis for correction"
        mandatory_violation = True
###changed to check for special character
    if any(x in string.punctuation for x in password):
        num_of_signs = [x for x in password if x in string.punctuation]
        score += (len(num_of_signs)*6)
        strengths[4][1] = 'True'
    else:
        popup_msg="Password contains no special characters\nPlease check the analysis for correction"
        mandatory_violation = True

    if len(password)>2:
        s = password[1:-1]
        if any(x.isalnum()for x in s) or any(x.isdigit()for x in s):
            num_of_signs = [x for x in password if x.isalnum()]
            num_of_signs += [x for x in password if x.isdigit()]
            score += (len(num_of_signs)*2)
            strengths[5][1] = 'True'


###penalties added by me
## checking if string is all letters
    if (password.isalpha()):
        score -= (len(password)/4)
        popup_msg="string is all letters, penalty induced"
        mandatory_violation=True

## checking if string is all digits
    if(password.isdigit()):
        score -= (len(password)/4)
        popup_msg="string is all digits, penalty induced"
        mandatory_violation=True

### checking for repeated characters
    results=0
    results = collections.Counter(password)
    for i in results: 
        if results[i]>1:
            score -= results[i]*(results[i]-1)
            popup_msg="There are repeated characters, penalty induced"
            mandatory_violation=True

### checking if there are consecutive uppercase characters
    countUpper=0
    l=len(password)

    for i in range(1,l-1):
        if (password[i] == password[i+1] and password[i].isupper()):
            countUpper += 1
        else:
            countUpper=1

        if countUpper>1:
            score -= countUpper*2
            popup_msg="There are consecutive uppercase letters, penalty induced"
            mandatory_violation=True

### checking if there are consecutive lowercase characters
    
    countLower=0
    for i in range(1,l-1):
        if(password[i] == password[i-1] and password[i].islower()):
            countLower += 1
        else:
            counterLower=1
        if countLower>1:
            score -= countLower*2
            popup_msg="There are consecutive lowercase letters, penalty induced"
            mandatory_violation=True

##checking if there are sequential letters
#TODO:fix this, the function only seems to check if all letters and not if sequential
    '''
    sequentialLettersCount=0

    prev_letter = ''
    current_string=''

    for letter in password:
        if prev_letter <= letter and letter.isalpha():
            current_string+=letter
            sequentialLettersCount+=1

        if sequentialLettersCount>1:
            score -= sequentialLettersCount
            popup_msg="There are sequential letters, penalty induced"
            mandatory_violation=True

    '''
##checking if there are sequential digits
###TODO:fix this, the function only seems to check if all digits and not if sequential
    '''
    sequentialDigitCount=0

    prev_digit = ''
    current_string=''

    for digit in password:
        if prev_digit <= digit and digit.isdigit():
            current_string+=digit
            sequentialDigitCount+=1

        if sequentialDigitCount>1:
            score -= sequentialDigitCount
            popup_msg="There are sequential digits, penalty induced"
            mandatory_violation=True

    '''
###Added by me untill here

    # set the score
    if score < 20:
        score_txt = 'Very Weak'
    elif score < 40:
        score_txt = 'Weak'
    elif score < 60:
        score_txt = 'Good'
    elif score < 80:
        score_txt = 'Strong'
    elif score >= 80:
        score_txt = 'Very Strong'

    return  weaknesses, strengths, score_txt, popup_msg, mandatory_violation
