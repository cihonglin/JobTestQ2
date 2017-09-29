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

def doCale(formulaStr):
	num_list = re.findall(r"\-?\d+\.?\d*",formulaStr)
	cale_mark = re.findall(r"[^0-9]",formulaStr)

	mark = cale_mark[0]
	x = int(num_list[0])
	y = int(num_list[1])
	result = cale(x,y,cale_mark[0])

	return result

def renewFormula(formulaStr):
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

			cale_result = str(doCale(sub_formula_str))
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
			cale_result_list.append(doCale(mulit_cale))
			pare_start = inputStr.find(mulit_cale)

			cale_result = str(doCale(mulit_cale))
			inputStr = inputStr[:pare_start] + cale_result + inputStr[pare_start + len(mulit_cale):] 
		return inputStr
	else:
		return pare_count
"""
do add & minus cale
"""
def initAddMinus(inputStr):
	cale_list = re.findall('\+|\-',inputStr)
	pattern_str = re.compile(r"\-?\d*\+|\-\-?\d*")
	if(inputStr[0] == '-'):
		new_string = '0'+inputStr
	else:
		new_string = inputStr
	new_str = re.sub('\+|\-', ',', new_string)
	count_list = new_str.split(',')

	i = tmp_result = 0
	tmp_result = 0
	result_obj = [0]

	for element in cale_list :
		x = i
		y = i + 1
		i += 1
		tmp_result = cale(int(result_obj[x]),int(count_list[y]),element)
		result_obj.append(tmp_result)
	return tmp_result

"""
def get_file(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'input file is：', inputfile
   print 'output file is：', outputfile
"""


def main(formula,inputVariable):
	replace_formula = replaceVar(formula,inputVariable); #replace var 
	print "replace_formula => " + replace_formula + "\n"
	renew_formula_result = renewFormula(initPare(replace_formula))
	print "renew_para_result => " + renew_formula_result + "\n"
	mulit_result =  renewFormula(initCale(renew_formula_result,'*'))
	print "do_plus_result => " + mulit_result + "\n"
	add_result = initAddMinus(mulit_result)
	print "add_minus_result => " + str(add_result) + "\n"
	return add_result


print "----- Question 2 Start-----"


formula="-80+x+4-(y+24)*22+(x+58)*2"
input_variable = "x=43,y=-2,z=8"
print "formula => " + formula + "\n"
print "input_variable => " + input_variable + "\n"
print "result => " + str(main(formula,input_variable))



#get_file(sys.argv[1:])

print "----- Question 2 End-----"



