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
	
	#print "x="+ str(x) 
	#print "y="+ str(y)

	if str(x).isdigit() and str(y).isdigit():
		op1 = int(x)
		op2 = int(y)
		result = cale(op1,op2,str(c))		
	else:
		result = str(x)+c+str(y)
	return result


def doCale(formulaStr):
	num_list = re.findall(r"\-?\d+\.?\d*",formulaStr)
	cale_mark = re.findall(r"[^0-9]",formulaStr)

	print cale_mark

	if(len(cale_mark) > 1 and cale_mark[0] == '-'):
		mark = cale_mark[1]
		x = int(num_list[0])
	else:
		mark = cale_mark[0]
		x = int(num_list[0])
	

	#mark = cale_mark[0]
	
	y = int(num_list[1])
	result = cale(x,y,mark)

	#print num_list[0] + mark + num_list[1] +"="+str(result)
	return result

def renewFormula(formulaStr):
	#print formulaStr
	return re.sub('\+\-','-',re.sub('\-\-', '+',formulaStr))

def initPare(inputStr):
	pare_left,pare_right = '(',')'
	pare_count = inputStr.count(pare_left) #counting '(' nums 
	new_string = inputStr
	if pare_count > 0:
		while pare_count > 0:
			pare_end = new_string.find(pare_right)
			pare_start = new_string.find(pare_left)
			sub_formula_str = new_string[pare_start + 1:pare_end]
			cale_result = str(doMath(sub_formula_str))
			new_string = new_string[:pare_start] + cale_result + new_string[pare_end + 1:] 

			pare_count -= 1
		return new_string

	else:
		return pare_count
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


	#print len(cale_list)
	while len(cale_list) != 0:
		#print i

		op1 = count_list.pop()
		op2 = count_list.pop()
		m = cale_list.pop()

		r = doCalculate(op1,op2,m)
		count_list.append(r)

		#print str(op1)+m+str(op2)+"="+str(r)

	return r



def doMath(renewFormulaResult):
	mulit_result =  renewFormula(initCale(renewFormulaResult,'*'))
	#print "do_plus_result => " + mulit_result + "\n"
	add_result = initAddMinus(mulit_result)
	#print "add_minus_result => " + str(add_result) + "\n"
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

string = raw_input("input (1-9)：");

if string.isdigit() and int(string) > 0 and int(string) < 10:
	filename = "input" + string + ".txt"
	print "input file name : "+filename
else:
	print "out of range"

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
	#print "replace_formula => " + replace_formula + "\n"
	renew_formula_result = renewFormula(initPare(replace_formula))
	#print renew_formula_result
	print doMath(renew_formula_result)
	#print "**********************************\n"

print "\n----- Question 2 End-----"



