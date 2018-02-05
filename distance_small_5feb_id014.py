from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

creation_points=[[516.75,175.1579995],
[516.75,118.3685714],
[516.75,336.914002],
[516.75,505.148],
[726.1641236,1026.65],
[561.1007847,1026.65],
[1029.95,1008.609087],
[1029.95,816.6795777],
[1033.25,623.5167167],
[1012.649,533.25],
[1033.25,537.351],
[1033.25,537.351],
[1029.95,862.299],
[1033.25,537.351],
[1033.25,569.617],
[1033.25,541.5343312],
[1061.266163,533.25],
[1187.996,529.95],
[1312.84,529.95],
[1399.026182,533.25],
[1520.05,602.940033],
[1520.05,703.4164749],
[1516.75,590.0641771],
[1245.092055,1016.75],
[1335.466377,1020.05],
[1120.234234,1016.75],
[1520.05,675.6733569],
[1501.923142,1020.05],
[1100.021232,1016.75],
[1363.209806,1020.05],
[909.7611508,523.35],
[1029.95,894.4976467],
[533.25,279.380554],
[533.25,71.35500719],
[1026.65,537.351],
[794.6457851,520.05],
[906.5448154,33.25],
[533.25,299.532134],
[636.8062784,33.25],
[767.8518955,33.25],
[592.8069487,516.75],
[1427.392858,33.25],
[1516.75,389.2537992],
[1516.75,347.6484067]]

creation_distance=[550,1375,675,525,1100,2150,1150,850,675,650,1100,600,675,525,525,650,575,
525,625,725,675,750,1725,550,750,525,2000,1500,800,2375,725,2850,575,550,2825,2125,650,1850,1625,1475,3125,575,700,950]

cc=[]
counts=[]

for i in range(len(creation_distance)):
	cc.append([])
	count=0
	for x in range(500,1502,5):
		for y in range(0,1002,5):
			if x%500==0 or y%500==0:
				if fabs(creation_points[i][0]-x) + fabs(creation_points[i][1]-y)<=0.8*creation_distance[i] and fabs(creation_points[i][0]-x) + fabs(creation_points[i][1]-y)>=0.2*creation_distance[i]:
					cc[i].append([x,y])
					count+=1
	counts.append(count)
print counts
print len(cc)
#print cc[0]
#print cc[1]
'''

cc1=[]
count1=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(557.66-y)<=950 :
				count1+=1
				cc1.append([x,y])
print count1


cc2=[]
count2=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1016.75-x)+fabs(499.377-y)<=1000:
				count2+=1
				cc2.append([x,y])
print count2


cc3=[]
count3=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1016.75-x)+fabs(512.649-y)<=900:
				count3+=1
				cc3.append([x,y])
print count3


cc4=[]
count4=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(537.351-y)<=925:
				count4+=1
				cc4.append([x,y])
print count4

cc5=[]
count5=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1016.75-x)+fabs(499.648-y)<=900:
				count5+=1
				cc5.append([x,y])
print count5

cc6=[]
count6=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(783-x)+fabs(523.35-y)<=900:
				count6+=1
				cc6.append([x,y])
print count6

cc7=[]
count7=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(517.775-x)+fabs(533.25-y)<=950:
				count7+=1
				cc7.append([x,y])
print count7

cc8=[]
count8=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(516.75-x)+fabs(288.5-y)<=925:
				count8+=1
				cc8.append([x,y])
print count8

cc9=[]
count9=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(523.35-x)+fabs(757.17-y)<=900:
				count9+=1
				cc9.append([x,y])
print count9


cc10=[]
count10=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(523.35-x)+fabs(796.12-y)<=1050:
				count10+=1
				cc10.append([x,y])
print count1

cc11=[]
count11=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(544.25-x)+fabs(1026.65-y)<=1000:
				count11+=1
				cc11.append([x,y])
print count11

cc12=[]
count12=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(738.421-x)+fabs(1026.65-y)<=950:
				count12+=1
				cc12.append([x,y])
print count12

cc13=[]
count13=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(877.107-x)+fabs(1026.65-y)<=1175:
				count13+=1
				cc13.append([x,y])
print count13

cc14=[]
count14=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(544.852-y)<=950:
				count14+=1
				cc14.append([x,y])
print count14

cc15=[]
count15=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1029.95-x)+fabs(890-y)<=950:
				count15+=1
				cc15.append([x,y])
print count15

cc16=[]
count16=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(537.351-y)<=975:
				count16+=1
				cc16.append([x,y])
print count16

cc17=[]
count17=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(546.95-y)<=1000:
				count17+=1
				cc17.append([x,y])
print count17


'''


#points=[[1033.25,557.66],[1016.75,499,377],[1016.75,512.649],[1033.25,537.351],[1016.75,499.648],[783,523.35],[517.775,533.25],[516.75,288.5],
#[523.35,757.17],[523.35,796.12],[544.25,1026.65],[738.421,1026.65],[877.107,1026.65],[1033.25,544.852],[1029.95,890],[1033.25,537.351],[1033.25,546.95]]



uploader_points=[[516.75,479.3172385],
[516.75,512.649],
[516.75,512.649],
[516.75,521.185247],
[1029.95,803.8267675],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,536.9469252],
[1033.308818,535.9289861],
[1055.479096,533.25],
[1190.986873,533.25],
[1288.063242,533.25],
[1329.67659,533.25],
[1501.834549,533.25],
[1516.75,590.0641771],
[1516.75,669.1780481],
[1516.75,987.9717487],
[1397.651303,1016.75],
[1029.95,991.588688],
[1029.95,922.2319605],
[1029.95,880.6260175],
[1026.65,811.2852206],
[1026.65,714.2143736],
[1026.65,630.9932359],
[1026.65,617.1235959],
[909.7611508,523.35],
[533.25,493.6852946],
[533.25,202.434643],
[622.9363074,33.25],
[817.1126008,33.25],
[872.5871597,33.25],
[983.5294216,33.25],
[1288.685112,33.25],
[1288.685112,33.25],
[1516.75,50.16005378],
[1516.75,119.5175401],
[1516.75,230.497762],
[1516.75,258.2391635],
[1233.132715,516.75],
[1136.041912,516.75]]

############ plot########
'''
x=[]
y=[]		
i=0
for ccc1 in cc:
	for elem in ccc1:
		#print elem[0]
		x.append(elem[0])
		y.append(elem[1])		
	plt.scatter(x,y)
	plt.plot(creation_points[i][0],creation_points[i][1],'ro')
	plt.plot(uploader_points[i][0],uploader_points[i][1],'yo')
	plt.ylim(ymax=1100,ymin=-100)
	plt.xlim(xmax=1600,xmin=400)
	plt.title(i+1)

	i=i+1	
	x=[]
	y=[]
	plt.show()		

'''

calc_points=[]
for i in range(len(cc)-1,-1,-1):
	calc_points.append(cc[i])


calc_points2=[]
for i in range(len(cc)-1,-1,-1):
	calc_points2.append(cc[i])


ccc1=[]
for i in range(len(cc)-1,-1,-1):
	ccc1.append(cc[i])


#calc_points=[cc17,cc16,cc15,cc14,cc13,cc12,cc11,cc10,cc9,cc8,cc7,cc6,cc5,cc4,cc3,cc2,cc1]

print "number of points before"
for elem in calc_points:
	print len(elem),



print "wvrg"	

#dist=[100,200,150,100,150,0,100,975,1875,-50,600,175,725,175,150,750,125,375,325,-25,
#100,375,225,1050,1050,75,425,125,25,575,200,100,75,200,150,100,125,975,150,725,75,500,175,250,450]

dist=[700,200,375,2575,750,25,125,100,300,475,50,25,175,350,175,75,350,325,
175,575,275,700,125,75,125,175,150,25,1100,725,525,475,350,100,200,550,0,450,125,200,50,975,175]


ccnew=[]
count=[]
for i in range(len(calc_points)-1):
	count32=0
	cc32=[]
	r_subset2=[]
	print "distance", dist[42-i]
	for elem1 in calc_points[i]:
		for elem2 in calc_points[i+1]:
			if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=0.8*dist[42-i] and abs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])>=0.2*dist[42-i]:
				count32+=1
				cc32.append([elem1,elem2])
				if elem2 not in r_subset2:
					r_subset2.append([elem2[0],elem2[1]])
	print len(calc_points[i+1]), len(r_subset2)
	count.append(count32)
	ccnew.append(cc32)
	calc_points[i+1]=r_subset2

print "number of points after"
for elem in calc_points:
	print len(elem),

print "count"
print count


############ cumulative distance
'''
dist_cum=dist
dist_cum.reverse()

for i in range(1,len(dist_cum)):
	dist_cum[i]=dist_cum[i]+dist_cum[i-1]


dist_cum.reverse()


countrev=[]
ccnewrev=[]
for i in range(len(calc_points)-1):
	count32=0
	cc32=[]
	r_subset2=[]
	print "distance", dist_cum[48-i]
	for elem1 in calc_points[0]:
		for elem2 in calc_points[i+1]:
			if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=dist_cum[48-i]:
				count32+=1
				cc32.append([elem1,elem2])
				if elem2 not in r_subset2:
					r_subset2.append([elem2[0],elem2[1]])
	print len(calc_points[i+1]), len(r_subset2)
	countrev.append(count32)
	ccnewrev.append(cc32)
	calc_points[i+1]=r_subset2


print "number of points after"
for elem in calc_points:
	print len(elem),
'''

###### plots ######
x=[]
y=[]
x2=[]
y2=[]
for i in range(len(ccc1)):
	for elem in ccc1[i]:
		#print elem[0]
		x.append(elem[0])
		y.append(elem[1])
	for elem2 in calc_points[i]:
		x2.append(elem2[0])
		y2.append(elem2[1])

	plt.scatter(x,y)
	plt.plot(x2,y2,'ro')
	plt.plot(creation_points[43-i][0],creation_points[43-i][1],'go')
	plt.plot(uploader_points[43-i][0],uploader_points[43-i][1],'yo')
	plt.title(44-i)
	
	plt.ylim(ymax=1100,ymin=-100)
	plt.xlim(xmax=1600,xmin=400)
	i=i+1
	x=[]
	y=[]
	x2=[]
	y2=[]	
	plt.show()		


xx=[]

for i in range(len(calc_points2)):
	print len(calc_points[i])/float(len(calc_points2[i]))
	xx.append(len(calc_points[i])/float(len(calc_points2[i])))

print min(xx), max(xx), np.mean(xx), np.median(xx), stats.mode(xx)
xx.reverse()
plt.plot(xx)
plt.ylim(ymax=1.2,ymin=0)
plt.xlabel('Number of uploads')
plt.ylabel('Ratio of points remaining')
plt.show()


