#/usr/bin/python
# encoding: utf-8
import re, sys, getopt

def replaceVar(inputStr,inputVariable):
	var_list = inputVariable.split(',')
	new_str = inputStr
	for var_x in var_list:
		var_num = var_x.split('=')
		v1,v2 = str(var_num[0]),str(var_num[1])
		new_str = re.sub(v1, v2, inputStr)
		inputStr = new_str
	return new_str

def cale(x,y,c):
	opration={'+':x+y,'-':x-y,'*':x*y}
	return opration.get(c,'error')

def doCalculate(x,y,c):
	
	if (str(x).lstrip('-').isdigit()) and (str(y).lstrip('-').isdigit()):
		op1 = int(x)
		op2 = int(y)
		result = cale(op1,op2,str(c))
	else:
		result = str(x)+c+str(y)

	#print result
	return result

def renewFormula(formulaStr):
	#print formulaStr
	return re.sub('\+\-','-',re.sub('\-\-', '+',formulaStr))

def initPare(inputStr):
	pare_left,pare_right = '(',')'
	pare_count = inputStr.count(pare_left) 
	new_string = pop_string = ''
	dump_list = []
	
	if pare_count > 0:
		for char in inputStr:
			if char != pare_right :
				dump_list.append(char)
				#print " << [ " + char + " ]  dump_list : " + "".join(dump_list)
			else:
				if char == pare_right :
					#pop_string = dump_list.pop()
					
					while len(dump_list) > 0 :
						#print "dump_list : " + "".join(dump_list)
						pop_string = dump_list.pop()
						#print " >> [ " + pop_string + " ]  dump_list : " + "".join(dump_list)
						if pop_string == pare_left:
							break;
						else:
							new_string = pop_string + new_string
							
				cale_result = str(doMath(new_string))
				dump_list.append(cale_result)
				#print " << [ " + char + " ]  dump_list : " + "".join(dump_list)
				#print "pop dump_list:" + new_string + " = " + cale_result
				new_string = ''

		return renewFormula("".join(dump_list))

	else:
		return inputStr
"""
do mulie cate
"""
def initCale(inputStr,pare):
	pare_count = inputStr.count(pare) #counting nums 
	if pare_count > 0:
		pattern_str = re.compile(r"\-?\d*"+ re.escape(pare) + "\-?\d*")
		cale_list = re.findall(pattern_str,inputStr)
		cale_result_list = [];
		for mulit_cale in cale_list:
			#print mulit_cale

			opration = mulit_cale.partition(pare)
			#print opration
			result = doCalculate(opration[0],opration[2],opration[1])
			#print result
			cale_result_list.append(result)
			pare_start = inputStr.find(mulit_cale)
			cale_result = str(result)
			inputStr = inputStr[:pare_start] + cale_result + inputStr[pare_start + len(mulit_cale):] 
	return inputStr

"""
do add & minus cale
"""
def initAddMinus(inputStr):
	cale_list = re.findall('\+|\-',inputStr)
	#pattern_str = re.compile(r"\-?\d*\+|\-\-?\d*")
	if(inputStr[0] == '-'):
		new_string = '0'+inputStr
	else:
		new_string = inputStr

	new_str = re.sub('\+|\-', ',', new_string)
	count_list = new_str.split(',')

	count_list.reverse()
	cale_list.reverse()

	#print cale_list
	#print count_list	

	result = inputStr

	#print len(cale_list)
	while len(cale_list) != 0:
		#print i

		op1 = count_list.pop()
		op2 = count_list.pop()
		m = cale_list.pop()

		result = doCalculate(op1,op2,m)
		count_list.append(result)

		#print str(op1)+m+str(op2)+"="+str(result)

	return result

def doMath(renewFormulaResult):
	mulit_result =  renewFormula(initCale(renewFormulaResult,'*'))
	#print "do_plus_result => " + mulit_result + "\n"
	add_result = initAddMinus(mulit_result)
	#print "add_minus_result => " + str(add_result) + "\n"
	#if(add_result[0] == '0'):
	#	add_result = add_result[1:]
	return add_result

def openFile(fileName):
	fo = open(fileName,"r+")
	if(fo):
		print " open file "+fileName+"..."
		fc = fo.read()
		fo.close()
		return fc
	else:
		print fileName+" not exists"

print "----- Question 2 Start-----"

option = raw_input("input (0-9)：");

if option.isdigit() and int(option) >= 0 and int(option) < 10:
	filename = "input" + option + ".txt"
	print "input file name : "+filename

	question_str = openFile("input/"+filename)

	split_list = question_str.split()

	split_list.reverse()

	formula = split_list.pop()

	split_list.reverse()

	#print formula_string

	print "\nformula => " + formula + "\n"

	for input_variable in split_list :
		print "**********************************"
		#print formula + "\n"
		print input_variable
		replace_formula = replaceVar(formula,input_variable); #replace var 
		print "replace_formula => " + replace_formula + "\n"
		init_pare = initPare(replace_formula)
		#if option == '3':
		#	print init_pare
	#		break
		renew_formula_result = renewFormula(init_pare)
		#print renew_formula_result
		print doMath(init_pare)
		print "**********************************\n"

	print "\n----- Question 2 End-----"

else:
	print "out of range"



