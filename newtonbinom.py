def newtonbinom(n):
	binomcalc = 1
	expr = []
	for k in range(0, n+1):
		templist = []
		nminusk = n-k
		if k != 0:
			binomcalc = binomcalc * (nminusk+1)//k
		if binomcalc > 1:
			templist.append(f"{binomcalc}")
		if nminusk != 0:
			templist.append(f"a{'' if nminusk == 1 else f'^{nminusk}'}")
		if k != 0:
			templist.append(f"b{'' if k == 1 else f'^{k}'}")
		expr.append("*".join(templist))
	return " + ".join(expr)
