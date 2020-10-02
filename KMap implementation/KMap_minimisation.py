# CSE 101 - IP HW2
# K-Map Minimization 
# Name: garvit gupta
# Roll Number:2018141
# Section:A
# Group:5
# Date:17/10/2018
def expression(epil):

	s='wxyz'
	expression=''#in this we will keep on adding the pis expression
	for k1 in epil:
		indexp=''#first we are forming expression for each individual pi in list epil
		for k2 in range(len(k1)):
			if k1[k2]=='1':
				indexp+=s[k2]
			elif k1[k2]=='0':
				indexp+=s[k2]+'`'
		expression+='+'+indexp
	expression=expression[1:]
	return expression
def dectobin(n):#decimal to binary
	if n==0:
		a='0000'
	elif n==1:
		a='0001'
	elif n==2:
		a='0010'
	elif n==3:
		a='0011'
	elif n==4:
		a='0100'
	elif n==5:
		a='0101'
	elif n==6:
		a='0110'
	elif n==7:
		a='0111'
	elif n==8:
		a='1000'
	elif n==9:
		a='1001'
	elif n==10:
		a='1010'
	elif n==11:
		a='1011'
	elif n==12:
		a='1100'
	elif n==13:
		a='1101'
	elif n==14:
		a='1110'
	elif n==15:
		a='1111'
	return a
	
def dectobintwo(n):
	if n==0:
		a='00'
	elif n==1:
		a='01'
	elif n==2:
		a='10'
	elif n==3:
		a='11'
	return a
	
def dectobinthree(n):
	if n==0:
		a='000'
	elif n==1:
		a='001'
	elif n==2:
		a='010'
	elif n==3:
		a='011'
	elif n==4:
		a='100'
	elif n==5:
		a='101'
	elif n==6:
		a='110'
	elif n==7:
		a='111'
	return a
	
def same(a,b):#checking if b satisfies to be under a (pi)
	check=True
	for k in range(len(a)):			
		if a[k]=='_':
			continue
		elif a[k]!=b[k]:
			check=False
	return check

	
def minFunc(numvar,stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	"""

	if numvar==4:	
		a=stringIn.find('d')
		minterms_ones=stringIn[1:a-1]	
		ones=list(minterms_ones.split(','))
		y=[]#will contain the binary rep. of dont cares
		if stringIn[-1]==')':
			dontcares=stringIn[a+2:-1]		
			dc=list(dontcares.split(','))
			for k in dc:
				y.append(dectobin(int(k)))
				y.sort()
		x=[]		
		if ones!=['']:	#will contain the binary rep. of minterms
			for k in ones:
				x.append(dectobin(int(k)))
		b=x+y
		b.sort()
		if b==['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111'] and y!=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']:
			z=1
		elif y==['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']:
			z=0
		else:
			l='01_'
			d={}
			for a1 in l:
				for a2 in l:
					for a3 in l:
						for a4 in l:
							k=a1+a2+a3+a4
							d[k]=0
			for k in d.keys():
				for i in b:
					if same(k,i):
						d[k]+=1
			
			d1={}
			for k in d.keys():
				count_=k.count('_')
				if d[k]==2**count_:
					d1[k]=2**count_
			
			l=[]
			for y in d1.keys():                    
				for k in x:                                    #x is a list of minterms
					if same(y,k) and y not in l:               #here we checked that whether a particular key possess dont care terms or not
						l.append(y)
				
			cus=0
			for k in l:
				b=k.count('_')
				if b>cus:
					cus=b
			l1=[]
			l2=[]
			for k in l:
				if k.count('_')==cus:
					l1.append(k)
				else:
					l2.append(k)
			l3=[]
			l4=[]
			for k1 in l1:
				for k2 in l2:
					if same (k1,k2)and(k2 not in l3):
						l3.append(k2)
					elif not same(k1,k2)and(k2 not in l4):
						l4.append(k2)
			for k in l3:
				l2.remove(k)
			
			cus1=0
			for k in l2:
				c=k.count('_')
				if c>cus1:
					cus1=c
			l5=[]
			for k in l2:
				if k.count('_')==cus1:
					l5.append(k)
			l=l1+l5
			

			#now finding essential prime implicants
			''' now we will take out each minterm from x and
			then will see that that particular minterm is coming in how many pis.
			if it is coming only in one of the pis then that pi is essential prime implicant.'''
			
			d2={}
			for k in x:
				d2[k]=[]
			
			for k1 in d2.keys():
				for k2 in l:
						if same(k2,k1):
							d2[k1].append(k2)
			l6=[]
			for k in d2.keys():
				f=d2[k]
				if len(f)==1 and (d2[k] not in l6):
					l6.append(d2[k])
			 
			
			li1=[]
			for k in l6:
				li1.extend(k)
				
			w=list(x)
			li2=[]
			for k1 in x:
				for k2 in li1:
					if  same(k2,k1) and ( k1 not in li2):
						li2.append(k1)
			for k in li2:
				w.remove(k) #minterms which are not included in essential prime implicants 
			d3={}#making another dictionary for finding the epis for minterms(as keys and values as those pis which are satisfying those respective minterms)
			for k in w:
				d3[k]=[]     
			nl=list(l)
			for k in li1:
				nl.remove(k)#having only those pi which are not epi
			for k1 in d3.keys():
				if len(nl)!=0:
					for k2 in nl:
						if same(k2,k1):
							d3[k1].append(k2)     #till this it is 100% correct
				else:
					break
			l7=[]#it is a list in list and we only we have to make a list which is li3
			for k in d3.keys():
				g=d3[k]
				if d3[k] not in l7:
					l7.append(d3[k])
					
			li3=[]
			for k in l7:
				li3.extend(k)
			li4=[]
			for k in d3.keys():
				a=d3[k]
				if a[0] not in li4:
					li4.append(a[0])
			epil=li4+li1#list of all those pis which will form the expression
			
			'''now we will form the expression'''
			
			z=expression(epil)
			g=list(z.split('+'))
			h=[]
			for k in g:
				h.append(k+'+')
			h.sort()
			m=''
			n=m.join(h)
			z=n[:-1]


	
	elif numvar==3:
		a=stringIn.find('d')
		minterms_ones=stringIn[1:a-1]	
		ones=list(minterms_ones.split(','))
		y=[]#will contain the binary rep. of dont cares
		if stringIn[-1]==')':
			dontcares=stringIn[a+2:-1]		
			dc=list(dontcares.split(','))
			for k in dc:
				y.append(dectobinthree(int(k)))
				y.sort()
		x=[]	#will contain the binary rep. of minterms
		if ones!=['']:
			for k in ones:
				x.append(dectobinthree(int(k)))
		b=x+y
		b.sort()
		if b==['000','001','010','011','100','101','110','111'] and y!=['000','001','010','011','100','101','110','111']:
			z=1
		elif y==['000','001','010','011','100','101','110','111']:
			z=0
		else:
			l='01_'
			d={}
			for a1 in l:
				for a2 in l:
					for a3 in l:
						k=a1+a2+a3
						d[k]=0
			
			for k in d.keys():
				for i in b:
					if same(k,i):
						d[k]+=1
			
			d1={}
			for k in d.keys():
				count_=k.count('_')
				if d[k]==2**count_:
					d1[k]=2**count_
			
			l=[]
			for y in d1.keys():                    
				for k in x:                                    #x is a list of minterms
					if same(y,k) and y not in l:               #here we checked that whether a particular key possess dont care terms or not
						l.append(y)
				
			cus=0
			for k in l:
				b=k.count('_')
				if b>cus:
					cus=b
			l1=[]
			l2=[]
			for k in l:
				if k.count('_')==cus:
					l1.append(k)
				else:
					l2.append(k)
			l3=[]
			l4=[]
			for k1 in l1:
				for k2 in l2:
					if same (k1,k2)and(k2 not in l3):
						l3.append(k2)
					elif not same(k1,k2)and(k2 not in l4):
						l4.append(k2)
			for k in l3:
				l2.remove(k)
			
			cus1=0
			for k in l2:
				c=k.count('_')
				if c>cus1:
					cus1=c
			l5=[]
			for k in l2:
				if k.count('_')==cus1:
					l5.append(k)
			l=l1+l5
			
			#now finding essential prime implicants
			'''now we will take out each minterm from x and
			then will see that that particular minterm is coming in how many pis.
			if it is coming only in one of the pis then that pi is essential prime implicant.'''
			
			d2={}
			for k in x:
				d2[k]=[]
			
			for k1 in d2.keys():
				for k2 in l:
						if same(k2,k1):
							d2[k1].append(k2)
			l6=[]
			for k in d2.keys():
				f=d2[k]
				if len(f)==1 and (d2[k] not in l6):
					l6.append(d2[k])
			 
			
			li1=[]
			for k in l6:
				li1.extend(k)
				
			w=list(x)
			li2=[]
			for k1 in x:
				for k2 in li1:
					if  same(k2,k1) and ( k1 not in li2):
						li2.append(k1)
			for k in li2:
				w.remove(k) #minterms which are not included in essential prime implicants 
			d3={}#making another dictionary for finding the epis for minterms(as keys and values as those pis which are satisfying those respective minterms)
			for k in w:
				d3[k]=[]     
			nl=list(l)
			for k in li1:
				nl.remove(k)#having only those pi which are not epi
			for k1 in d3.keys():
				if len(nl)!=0:
					for k2 in nl:
						if same(k2,k1):
							d3[k1].append(k2)     #till this it is 100% correct
				else:
					break
			l7=[]#it is a list in list and we only we have to make a list which is li3
			for k in d3.keys():
				g=d3[k]
				if d3[k] not in l7:
					l7.append(d3[k])
					
			li3=[]
			for k in l7:
				li3.extend(k)
			li4=[]
			for k in d3.keys():
				a=d3[k]
				if a[0] not in li4:
					li4.append(a[0])
			epil=li4+li1#list of all those pis which will form the expression
			
			#now we will form the expression
			
			z=expression(epil)
			g=list(z.split('+'))
			h=[]
			for k in g:
				h.append(k+'+')
			h.sort()
			m=''
			n=m.join(h)
			z=n[:-1]

	elif numvar==2:
		a=stringIn.find('d')
		minterms_ones=stringIn[1:a-1]	
		ones=list(minterms_ones.split(','))
		y=[]#will contain the binary rep. of dont cares
		if stringIn[-1]==')':
			dontcares=stringIn[a+2:-1]		
			dc=list(dontcares.split(','))
			for k in dc:
				y.append(dectobintwo(int(k)))
				y.sort()
				
		x=[]	#will contain the binary rep. of minterms
		if ones!=['']:
			for k in ones:
				x.append(dectobintwo(int(k)))
		b=x+y
		b.sort()
		if b==['00','01','10','11'] and y!=['00','01','10','11']:
			z=1
		elif y==['00','01','10','11']:
			z=0
		else:
			l='01_'
			d={}
			for a1 in l:
				for a2 in l:
					k=a1+a2
					d[k]=0
			
			for k in d.keys():
				for i in b:
					if same(k,i):
						d[k]+=1
			
			d1={}
			for k in d.keys():
				count_=k.count('_')
				if d[k]==2**count_:
					d1[k]=2**count_
			
			l=[]
			for y in d1.keys():                    
				for k in x:                                    #x is a list of minterms
					if same(y,k) and y not in l:               #here we checked that whether a particular key possess dont care terms or not
						l.append(y)
				
			cus=0
			for k in l:
				b=k.count('_')
				if b>cus:
					cus=b
			l1=[]
			l2=[]
			for k in l:
				if k.count('_')==cus:
					l1.append(k)
				else:
					l2.append(k)
			l3=[]
			l4=[]
			for k1 in l1:
				for k2 in l2:
					if same (k1,k2)and(k2 not in l3):
						l3.append(k2)
					elif not same(k1,k2)and(k2 not in l4):
						l4.append(k2)
			for k in l3:
				l2.remove(k)
			
			cus1=0
			for k in l2:
				c=k.count('_')
				if c>cus1:
					cus1=c
			l5=[]
			for k in l2:
				if k.count('_')==cus1:
					l5.append(k)
			l=l1+l5
			#now finding essential prime implicants
			'''now we will take out each minterm from x and
			then will see that that particular minterm is coming in how many pis.
			if it is coming only in one of the pis then that pi is essential prime implicant.'''
			
			d2={}
			for k in x:
				d2[k]=[]
			
			for k1 in d2.keys():
				for k2 in l:
						if same(k2,k1):
							d2[k1].append(k2)
			l6=[]
			for k in d2.keys():
				f=d2[k]
				if len(f)==1 and (d2[k] not in l6):
					l6.append(d2[k])
			 
			
			li1=[]
			for k in l6:
				li1.extend(k)
				
			w=list(x)
			li2=[]
			for k1 in x:
				for k2 in li1:
					if  same(k2,k1) and ( k1 not in li2):
						li2.append(k1)
			for k in li2:
				w.remove(k) #minterms which are not included in essential prime implicants 
			d3={}#making another dictionary for finding the epis for minterms(as keys and values as those pis which are satisfying those respective minterms)
			for k in w:
				d3[k]=[]     
			nl=list(l)
			for k in li1:
				nl.remove(k)#having only those pi which are not epi
			for k1 in d3.keys():
				if len(nl)!=0:
					for k2 in nl:
						if same(k2,k1):
							d3[k1].append(k2)     #till this it is 100% correct
				else:
					break
			l7=[]#it is a list in list and we only we have to make a list which is li3
			for k in d3.keys():
				g=d3[k]
				if d3[k] not in l7:
					l7.append(d3[k])
					
			li3=[]
			for k in l7:
				li3.extend(k)
			li4=[]
			for k in d3.keys():
				a=d3[k]
				if a[0] not in li4:
					li4.append(a[0])
			epil=li4+li1#list of all those pis which will form the expression
			
			#now we will form the expression
			
			z=expression(epil)
			g=list(z.split('+'))
			h=[]
			for k in g:
				h.append(k+'+')
			h.sort()
			m=''
			n=m.join(h)
			z=n[:-1]
			
	return z
print(minFunc(4,'()d(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)'))
print(minFunc(4,'(7)d(0,1,2,3,4,5,6,8,9,10,11,12,13)'))
print(minFunc(3,'(0,2)d(1,3,4,5,6,7)'))
print(minFunc(3,'(7)d(0,1,2,3,4,5,6)'))
print(minFunc(2,'(0,1,2,3)d-'))
print(minFunc(2,'(1,3)d(0,2)'))	

