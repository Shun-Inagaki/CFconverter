import ui

value1 = '0'
value2 = '0'
flgvalue = 0

def calc(sender):
	input1 = sender.superview['textfield1'].text
	input2 = sender.superview['textfield2'].text
	result1 = sender.superview['textfield1']
	result2 = sender.superview['textfield2']
	global value1
	global value2
	global flgvalue
	
	if input1 != value1 or flgvalue == 3:
		result2.text = str(round((float(input1) * 1.8 + 32.0),1))
		value1 = input1
		value2 = float(input1) * 1.8 + 32.0
		flgvalue = 1
	elif input2 != value2 or flgvalue == 4:
		result1.text = str(round(((float(input2) - 32.0) / 1.8),1))
		value1 = (float(input2) - 32.0) / 1.8
		value2 = input2
		flgvalue = 2

def exchange(sender):
	global value1
	global value2
	global flgvalue
	
	if flgvalue == 1:
		exvalue1 = sender.superview['textfield1'].text
		exvalue2 = str(round(((float(exvalue1) - 32.0) / 1.8),1))
		sender.superview['textfield1'].text = exvalue2
		sender.superview['textfield2'].text = exvalue1
		value1 = exvalue2
		flgvalue = 4
	elif flgvalue == 2:
		exvalue2 = sender.superview['textfield2'].text
		exvalue1 = str(round((float(exvalue2) * 1.8 + 32.0),1))
		sender.superview['textfield1'].text = exvalue2
		sender.superview['textfield2'].text = exvalue1
		value2 = exvalue1
		flgvalue = 3
	calc(sender)

v = ui.load_view()
if min(ui.get_screen_size()) >= 768:
	# iPad
	v.frame = (0, 0, 360, 400)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])
