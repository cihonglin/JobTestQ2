#/usr/bin/python
# encoding: utf-8
import re, sys, getopt

def replace_var(input_str,input_variable):
	var_list = input_variable.split(',')
	new_str = input_str
	for var_x in var_list:
		var_num = var_x.split('=')
		v1,v2 = str(var_num[0]),str(var_num[1])
		new_str = re.sub(v1, v2, input_str)
		input_str = new_str
	return new_str

def cale(x,y,c):
	opration={'+':x+y,'-':x-y,'*':x*y}
	return opration.get(c,'error')

def do_cale(formula_str):
	num_list = re.findall(r"\-?\d+\.?\d*",formula_str)
	cale_mark = re.findall(r"[^0-9]",formula_str)

	mark = cale_mark[0]
	x = int(num_list[0])
	y = int(num_list[1])
	result = cale(x,y,cale_mark[0])

	return result

def renew_formula(formula_str):
	return re.sub('\+\-','-',re.sub('\-\-', '+',formula_str))

def init_pare(input_str):
	pare_left,pare_right = '(',')'
	pare_count = input_str.count(pare_left) #counting '(' nums 
	new_string = input_str
	if pare_count > 0:
		while pare_count > 0:
			pare_end = new_string.find(pare_right)
			pare_start = new_string.find(pare_left)
			sub_formula_str = new_string[pare_start + 1:pare_end]

			cale_result = str(do_cale(sub_formula_str))
			new_string = new_string[:pare_start] + cale_result + new_string[pare_end + 1:] 

			pare_count -= 1
		return new_string

	else:
		return pare_count
"""
do mulie cate
"""
def init_cale(input_str,pare):
	pare_count = input_str.count(pare) #counting nums 
	if pare_count > 0:
		pattern_str = re.compile(r"\-?\d*"+ re.escape(pare) + "\-?\d*")
		cale_list = re.findall(pattern_str,input_str)
		cale_result_list = [];
		for mulit_cale in cale_list:
			cale_result_list.append(do_cale(mulit_cale))
			pare_start = input_str.find(mulit_cale)

			cale_result = str(do_cale(mulit_cale))
			input_str = input_str[:pare_start] + cale_result + input_str[pare_start + len(mulit_cale):] 
		return input_str
	else:
		return pare_count
"""
do add & minus cale
"""
def init_add_minus(input_str):
	cale_list = re.findall('\+|\-',input_str)
	pattern_str = re.compile(r"\-?\d*\+|\-\-?\d*")
	if(input_str[0] == '-'):
		new_string = '0'+input_str
	else:
		new_string = input_str
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


def main(formula,input_variable):
	replace_formula = replace_var(formula,input_variable); #replace var 
	print "replace_formula => " + replace_formula + "\n"
	renew_formula_result = renew_formula(init_pare(replace_formula))
	print "renew_para_result => " + renew_formula_result + "\n"
	mulit_result =  renew_formula(init_cale(renew_formula_result,'*'))
	print "do_plus_result => " + mulit_result + "\n"
	add_result = init_add_minus(mulit_result)
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



