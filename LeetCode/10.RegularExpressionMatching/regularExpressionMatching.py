

class RegularExpressionMatching:
	def matche(self, s, p)->bool:
		i = 0
		i1 = 0
		spec = ''
		status = True
		while i < len(s):
			if (s[i] == p[i1]) or (p[i1]=='.'):
				status = True
			elif ((p[i]=='\*')):
				status = self._che1(s[1:], p[i])
			else:
				status = False
				print("Don't match")
				break
			i += 1
		
		return status
	
	def _che1(self, s, p):
		rep = False
		if p == s[0]:
			return True
		if p=='\*':
			rep = self._che1(s[1:], '\*')
		elif len(p)>1 and len(p) < len(s):
			rep = self._che1(s[1:], p[1])
		return rep
