def lev(exp):
	a1_2 = 300
	a2_3 = a1_2 + 600
	a3_4 = a2_3 + 900
	a4_5 = a3_4 + 1200
	a5_6 = a4_5 + 1500
	a6_7 = a5_6 + 1500
	a7_8 = a6_7 + 1500
	a8_9 = a7_8 + 1500
	a9_10 = a8_9 + 1500

	if exp < 300:
		return 1
	elif exp < a2_3:
		return 2
	elif exp < a3_4:
		return 3
	elif exp < a4_5:
		return 4
	elif exp < a5_6:
		return 5
	elif exp < a6_7:
		return 6
	elif exp < a7_8:
		return 7
	elif exp < a8_9:
		return 8
	elif exp < a9_10:
		return 9
	else:
		return 10

