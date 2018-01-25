from math import fabs
import matplotlib.pyplot as plt

cc1=[]
count1=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(196.89-x)+fabs(991.75-y)<=925:
				count1+=1
				cc1.append([x,y])
print count1
#print cc


cc2=[]
count2=0
for x in range(0,2001,5):
	for y in range(-505,1001,5):
		if x%500==0 or y%500==0:
			if fabs(119.94-x)+fabs(991.75-y)<=1400:
				count2+=1
				cc2.append([x,y])
print count2


cc3=[]
count3=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(418.804-x)+fabs(991.75-y)<=1000:
				count3+=1
				cc3.append([x,y])
print count3
#print cc


cc4=[]
count4=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(495.05-x)+fabs(869.03-y)<=925:
				count4+=1
				cc4.append([x,y])
print count4

cc5=[]
count5=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(498.35-x)+fabs(758.34-y)<=900:
				count5+=1
				cc5.append([x,y])
print count5
#print cc


cc6=[]
count6=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(498.35-x)+fabs(786.07-y)<=1250:
				count6+=1
				cc6.append([x,y])
print count6


cc7=[]
count7=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(498.35-x)+fabs(702.875-y)<=1025:
				count7+=1
				cc7.append([x,y])
print count7
#print cc


cc8=[]
count8=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(498.35-x)+fabs(591.906-y)<=925:
				count8+=1
				cc8.append([x,y])
print count8


cc9=[]
count9=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(498.35-x)+fabs(520.628-y)<=925:
				count9+=1
				cc9.append([x,y])
print count9


cc10=[]
count10=0
for x in range(0,2001,5):
	for y in range(-500,1001,5):
		if x%500==0 or y%500==0:
			if fabs(619.837-x)+fabs(498.35-y)<=925:
				count10+=1
				cc10.append([x,y])
print count10

#######################################


count12=0
cc12=[]
i=0

subset1=[]
subset2=[]

for elem1 in cc1:
	for elem2 in cc2:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=325:
			count12+=1
			cc12.append([elem1,elem2])
			if elem2 not in subset2:
				subset2.append(elem2)
			if elem1 not in subset1:
				subset1.append(elem1)

print "from 1 to 2",count12, len(subset1), len(subset2)

count23=0
cc23=[]
i=0

subset3=[]
subset20=[]

for elem1 in cc2:
	for elem2 in cc3:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=150:
			count23+=1
			cc23.append([elem1,elem2])
			if elem2 not in subset3:
				subset3.append(elem2)
			if elem1 not in subset20:
				subset20.append(elem1)

print "from 2 to 3",count23, len(subset20), len(subset3)



count34=0
cc34=[]
i=0

subset4=[]
subset30=[]

for elem1 in cc3:
	for elem2 in cc4:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=275:
			count34+=1
			cc34.append([elem1,elem2])
			if elem2 not in subset4:
				subset4.append(elem2)
			if elem1 not in subset30:
				subset30.append(elem1)

print "from 3 to 4",count34,len(subset30), len(subset4)



count45=0
cc45=[]
i=0

subset5=[]
subset40=[]

for elem1 in cc4:
	for elem2 in cc5:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=175:
			count45+=1
			cc45.append([elem1,elem2])
			if elem2 not in subset5:
				subset5.append(elem2)
			if elem1 not in subset40:
				subset40.append(elem1)

print "from 4 to 5",count45, len(subset40), len(subset5)








print "length", len(cc1), len(subset1), len(cc2), len(subset2)



count40=0
cc40=[]
subset3=[]
for elem1 in subset2:
	for elem2 in cc3:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=150:
			count40+=1
			cc40.append([elem1,elem2])
			if elem2 not in subset3:
				subset3.append(elem2)
			


print "from 2 to 3",count40	, len(subset3)


count31=0
cc31=[]
subset31=[]
for elem1 in subset1:
	for elem2 in subset3:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=475:
			count31+=1
			cc31.append([elem1,elem2])
			if elem1 not in subset31:
				subset31.append(elem1)
print "from 1 to 3 via 2", count31,len(subset31)

count32=0
cc32=[]
for elem1 in cc1:
	for elem2 in cc3:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=475:
			count32+=1
			cc32.append([elem1,elem2])

print count32
	
x=[]
y=[]		
#print cc1	
for elem in cc1:
	#print elem[0]
	x.append(elem[0])
	y.append(elem[1])		
plt.scatter(x,y)
plt.ylim(ymax=1100,ymin=-100)
plt.xlim(xmax=2100,xmin=-100)	
plt.show()		

###############################


# from 3 to 2

print "rev"
count32=0
cc32=[]
r_subset2=[]
r_subset3=[]
for elem1 in cc3:
	for elem2 in cc2:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=150:
			count32+=1
			cc32.append([elem1,elem2])
			if elem2 not in r_subset2:
				r_subset2.append([elem2[0],elem2[1]])
			if elem1 not in r_subset3:
				r_subset3.append(elem1)

print "from 3 to 2",count32,len(r_subset3), len(r_subset2)


# from 2 to 1

print r_subset2[0],cc2[0]
count21=0
r_subset1=[]
cc21=[]
i=0
#r_subset3=[]
for elem1 in r_subset2:
	#print i
	i=i+1
	for elem2 in cc1:
		if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=325:
			count21+=1
			cc21.append([elem1,elem2])
			if elem2 not in r_subset1:
				r_subset1.append(elem2)
			#if elem1 not in r_subset3:
			#	r_subset3.append(elem1)

print "from 3 to 2 to 1",count21,len(r_subset1)



cc=[cc9,cc8,cc7,cc6,cc5,cc4,cc3,cc2,cc1]
dist=[]
ccnew=[]
count=[]
for i in range(len(cc)-1):
	count32=0
	cc32=[]
	r_subset2=[]
	for elem1 in cc[i]:
		for elem2 in cc[i+1]:
			if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=150:
				count32+=1
				cc32.append([elem1,elem2])
				if elem2 not in r_subset2:
					r_subset2.append([elem2[0],elem2[1]])
	print len(cc[i+1]), len(r_subset2)
	count.append(count32)
	ccnew.append(cc32)
	cc[i+1]=r_subset2

print count





