#/usr/bin/python
# encoding: utf-8
import re

def find_pare(input_str):
	pare_left,pare_right = '(',')'
	pare_info = {}
	pare_count = input_str.count(pare_left) #counting '(' nums 
	new_string = input_str
	if pare_count > 0:
		sub_formula = [] 
		while pare_count > 0:
			pare_end = new_string.find(pare_right)
			sub_formula.append (new_string[new_string.find(pare_left)+1:pare_end])
			new_string = new_string[pare_end+1:]
			pare_count -= 1
		return sub_formula

	else:
		return pare_count

def replace_var(input_str,var_list):
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

def do_cal(var_list):
	result = []
	for cal_list in var_list:
		num_list = re.findall(r"\d+\.?\d*",cal_list)
		cale_mark = re.findall(r"[^0-9]",cal_list)
		result.append(cale(int(num_list[0]),int(num_list[1]),cale_mark[0]))

	return result


print "----- test Q2 start-----"

formula="x+4-(y-43)*2+(x+58)-2"
input_variable = "x=43,y=26"

var_list = input_variable.split(',')

print("formula = "+formula)

replace_formula = replace_var(formula,var_list);

print "replace_formula = " +replace_formula

pare_cale = find_pare(replace_formula)

print pare_cale


#print 
#pare_cale_result = do_cal(pare_cale)
"""
pare_cale_result = map(str, do_cal(pare_cale))

print pare_cale_result

pare_dict = dict(zip(pare_cale, pare_cale_result))

print pare_dict

print replace_formula
#new_str = replace_formula

print "replace start --- "
for dict_index,dict_value in pare_dict.items():
	x = "\("+dict_index+"\)"

	print x + " => " + dict_value
	replace_formula = re.sub(x,dict_value,replace_formula)
	print replace_formula
	print " "
"""
#print replace_formula

#pattern = re.compile(r'\b(' + '|'.join(pare_dict.keys()) + r')\b')

#print pattern
#result = pattern.sub(lambda x: pare_dict[x.group()], replace_formula)

#result = reduce(lambda x, y: x.replace(y, pare_dict[y]), pare_dict, replace_formula)
#print result





print "-----test Q2 End-----"



