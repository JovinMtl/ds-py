

class RegularExpressionMatching:
	def matche(self, s, p)->bool:
		i = 0
		i1 = 0
		status = True
		while i < len(s):
			if (s[i] == p[i]) or (p[i]=='.'):
				status = True
			elif ((p[i]=='\*')and (p[i-1]==s[i])):
				status = True
			else:
				status = False
				print("Don't match")
				break
			i += 1
		
		return status
