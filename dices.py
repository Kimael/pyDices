import random


def generateOneGroup (pMinValue, pMaxValue, pGroupBy):
    if (pGroupBy < 1):
        return ''
    else:
        diceNum = 1
        diceGroup = 0
        while (diceNum <= pGroupBy):
            dice = random.randint(pMinValue, pMaxValue)
            diceGroup += dice
            diceNum += 1
        
        return str(diceGroup)


def prependNChars (pOriginalStr, pChar, pNbCharsToAdd):
    if (pNbCharsToAdd < 1):
        return pOriginalStr
    else:
        charNum = 1
        chars = ''
        while (charNum <= pNbCharsToAdd):
            chars += pChar
            charNum += 1
        
        result = chars + pOriginalStr
        return result


def fixedSizeString (pOriginalStr, pTargetSize, pChar):
    nbWhiteSpacesToAdd = pTargetSize - len(pOriginalStr)
    result = prependNChars(pOriginalStr, pChar, nbWhiteSpacesToAdd)
    
    return result


def generateGroups (pNbGroups, pTargetSize):
    if (pNbGroups < 1):
        return ''
    else:
        result = ''
        groupNum = 1
        while (groupNum <= pNbGroups):
            diceGroupStr = generateOneGroup(min_value, max_value, group_by)
            diceGroupStrFix = fixedSizeString(diceGroupStr, pTargetSize, ' ')
            result += diceGroupStrFix
            groupNum += 1
        
        return result



try:
    min_value = int(input('Enter the minimum value of the dice: '))
    max_value = int(input('Enter the maximum value of the dice: '))
    group_by  = int(input('Enter the number of dices to group: '))
    nb_groups = int(input('Number of groups per line: '))
    nb_lines  = int(input('Number of lines: '))
except:
    print('Invalid input; program defaults to "Can\'t Stop" game settings.')
    min_value = 1
    max_value = 6
    group_by  = 2
    nb_groups = 2
    nb_lines  = 3

if (group_by < 1):
    print('\nInvalid number of dices to group: '+ str(group_by))
    quit()
if (nb_groups < 1):
    print('\nInvalid number of groups per line: '+ str(nb_groups))
    quit()
if (nb_lines < 1):
    print('\nInvalid number of lines: '+ str(nb_lines))
    quit()

max_group_value = max_value * group_by
max_group_value_size = len(str(max_group_value))
max_group_value_size_plus_one = max_group_value_size + 1

nb_lines_size = len(str(nb_lines))

throwNb = 1
again = True
while again:
    print('\nThrow number: '+ str(throwNb))
    lineNum = 1
    while (lineNum <= nb_lines):
        lineNumStr = str(lineNum)
        lineNumFixedStr = fixedSizeString(lineNumStr, nb_lines_size, ' ')
        lineStr = '#'+ lineNumFixedStr
        
        groups=generateGroups(nb_groups, max_group_value_size_plus_one)
        lineStr += groups
        
        print(lineStr)
        lineNum += 1
    
    stop_roll = input('Want to Stop rolling the dices or Restart? ')
    noStopRoll = (len(stop_roll) < 1)
    if (noStopRoll):
        throwNb += 1
    else:
        stopRoll = stop_roll
        doStop = (stopRoll[0].lower() == 's')
        if (doStop):
            again = False
            print('\nThank you! Bye bye ...\n')
        else:
            doRestart = (stopRoll[0].lower() == 'r')
            if (doRestart):
                throwsWord = 'throw'
                if(throwNb > 1):
                    throwsWord += 's'
                print('\nRestarting after '+ str(throwNb) +' '+ throwsWord +'.\n\n')
                throwNb = 1
            else:
                throwNb += 1
