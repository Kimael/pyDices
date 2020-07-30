import random


def generateOneGroup (pMinValue, pMaxValue, pGroupBy):
    diceNum=1
    diceGroup=0
    while (diceNum <= pGroupBy):
        dice=random.randint(pMinValue, pMaxValue)
        diceGroup=diceGroup+dice
        diceNum=diceNum+1
    return str(diceGroup)


def prependNChars (pOriginalStr, pChar, pNbCharsToAdd):
	charNum=1
	chars=''
	while (charNum <= pNbCharsToAdd):
	       chars=chars + pChar
	       charNum=charNum+1
	       
	return chars + pOriginalStr


def fixedSizeString (pOriginalStr, pTargetSize, pChar):
    nbWhiteSpacesToAdd=pTargetSize - len(pOriginalStr)
    result=prependNChars(pOriginalStr, pChar, nbWhiteSpacesToAdd)
    
    return result


def generateGroups (pNbGroups, pTargetSize):
	result=''
	groupNum=1
	while (groupNum <= pNbGroups):
	       diceGroupStr=generateOneGroup(min_value, max_value, group_by)
	       diceGroupStrFix=fixedSizeString(diceGroupStr, pTargetSize, ' ')
	       result=result + diceGroupStrFix
	       groupNum=groupNum+1
	       
	return result



try:
    min_value = int(input('Enter the minimum value of the die: '))
    max_value = int(input('Enter the maximum value of the die: '))
    group_by = int(input('Enter the number of dices to group: '))
    nb_groups = int(input('Number of groups per line: '))
    nb_lines = int(input('Number of lines: '))
except:
    print('Input invalid program will revert to defaults.')
    min_value=1
    max_value=6
    group_by=2
    nb_groups=2
    nb_lines=3

max_group_value=max_value*group_by
max_group_value_size=len(str(max_group_value))

nb_lines_size=len(str(nb_lines))

again = True

while again:
    lineNum=1
    while (lineNum <= nb_lines):
        lineNumStr=str(lineNum)
        lineNumFixedStr=fixedSizeString(lineNumStr, nb_lines_size, ' ')
        lineStr='#'+ lineNumFixedStr
        
        groups=generateGroups(nb_groups, max_group_value_size+1)
        lineStr=lineStr + groups
        
        print(lineStr)
        lineNum=lineNum+1
    
    stop_roll = input('Want to stop rolling the dices? ')
    noStopRoll=(len(stop_roll) < 1)
    if (noStopRoll):
    	continue
    else:
    	stopRoll=stop_roll
    	doStop=(stopRoll[0].lower() == 'y')
    	if (doStop):
    		again = False
    		#break
    	#else:
    		#continue
