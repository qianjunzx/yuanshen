#get the situatiom of a day
import level
def day(pwr,exp,getmed,med,pingfeng,money,purple,blue,green):
	money += getmoney(pwr)
	med += getmed
	money -= 10 * getmed
	a = 0
	b = 0
	c = 0
	flag = true
	while flag:
		if money > 240 and purple > 0:
			purple -= 1
			a += 1
			money -= 240
		elif money > 160 and blue > 0:
			blue -= 1
			b += 1
			money -= 160
		elif money > 90 and green > 0:
			green -=1
			c += 1
			money -= 90
		else:
			flag = false

	d = a + b + c
	sit = getsit(level.lev(exp))
	num = 0
	while sit > num and (a > 0 or b > 0 or c > 0 or pingfeng > 0):
		if a > 0:
			list.append(90)
			a -= 1
			num += 1
		elif b > 0:
			list.append(60)
			b -= 1
			num += 1
		elif c > 0:
			list.append(30)
			c -= 1
			num += 1
		else: 
			list.append(90)
			pingfeng -= 1
			num += 1
	i = 0
	while (a > 0 or b > 0 or c > 0 or pingfeng > 0) and med > 0:
		
		if i <= d:
			if a > 0:
				add_exp += list[0]
				add_pwr += list[0]
				del list[0]
				list.append(90)
				a -= 1
				i += 1
			elif b > 0:
				add_exp += list[0]
				add_pwr += list[0]
				del list[0]			
				list.append(60)
				b -= 1
				i += 1
			elif c > 0:
				add_exp += list[0]
				add_pwr += list[0]
				del list[0]
				list.append(30)
				c -= 1
				i += 1
			else:
				add_exp += list[0]
				add_pwr += list[0]
				del list[0]
				list.append(90)
				pingfeng -= 1
				i += 1
		else:
			if a > 0:
				add_pwr += list[0]
				del list[0]
				list.append(90)
				a -= 1
				i += 1
			elif b > 0:
				add_pwr += list[0]
				del list[0]			
				list.append(60)
				b -= 1
				i += 1
			elif c > 0:
				add_pwr += list[0]
				del list[0]
				list.append(30)
				c -= 1
				i += 1
			else:
				add_pwr += list[0]
				del list[0]
				list.append(90)
				pingfeng -= 1
				i += 1
	k = 0		
	for k in range(0,num):
		if k + 1 <= d - i:
			nex_add_exp += list[k]
			nex_add_pwr += list[k]
		else:
			nex_add_pwr += list[k]
	return add_pwr,add_exp,nex_add_pwr,nex_add_exp






#get the sit per day from trust level   
def getsit(lev):
	if lev < 2:
		return 1
	elif lev < 4:
		return 2
	elif lev < 6:
		return 3
	elif lev < 9:
		return 4
	else:
		return 5


#get the money per day
def getmoney(pwr):
	if pwr < 2000:
		speed = 4
	elif pwr < 3000:
		speed = 8
	elif pwr < 4500:
		speed = 12
	elif pwr < 6000:
		speed = 16   
	elif pwr < 8000:
		speed = 20 
	elif pwr < 10000:
		speed = 22 
	elif pwr < 12000:
		speed = 24  
	elif pwr < 15000:
		speed = 26  
	elif pwr < 20000:
		speed = 28
	else :
		speed = 28
	money = speed * 24
	return money  