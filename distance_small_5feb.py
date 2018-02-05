from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

creation_points=[[516.75,175.1579995],
[516.75,93.1503],
[516.75,230.697],
[516.75,285.1446371],
[516.75,341.647],
[328.287,533.25],
[516.75,295.3170078],
[516.75,512.649],
[542.671,533.25],
[779.98,1026.65],
[523.35,843.3193385],
[883.6841849,1026.65],
[1037.351,516.75],
[1033.25,537.351],
[1014.1,533.25],
[1032.905,533.25],
[1033.25,559.02],
[1033.25,550.843],
[1113.13,529.95],
[1288.063242,533.25],
[1279.858,529.95],
[1349.188,533.25],
[1415.139,529.95],
[1490.72203,533.25],
[1515.667,533.836997],
[1026.65,874.3247044],
[1113.87,1016.75],
[1026.65,603.2532595],
[1026.65,572.5168277],
[1026.65,985.2893842],
[1026.65,544.852],
[963.6550038,523.35],
[980.9293794,523.35],
[856.358727,523.35],
[917.684,520.05],
[669.804,516.75],
[592.8069487,516.75],
[533.25,501.1379164],
[595.1758496,33.25],
[656.89,33.25],
[1059.1269,33.25],
[706.1476941,33.25],
[872.5871597,33.25],
[1419.747,33.25],
[1516.75,91.77623317],
[1516.75,389.2537992]]

creation_distance=[550,725,625,800,675,600,550,600,575,750,1600,1200,600,600,700,700,575,550,525,575,575,525,650,900,1725,650,1125,
700,725,1500,1050,675,825,625,900,600,600,550,600,600,600,1350,1550,700,700,575]

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
[516.75,509.5897336],
[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,708.2316905],
[1029.95,937.1795995],
[1029.95,913.4296684],
[1033.25,609.6472526],
[1033.25,539.9448612],
[1033.25,537.351],
[1033.25,537.351],
[1033.25,537.351],
[1164.399793,533.25],
[1232.589046,533.25],
[1440.626083,533.25],
[1516.75,540.4569034],
[1516.75,545.6869387],
[1516.75,565.1415871],
[1516.75,738.3337272],
[1516.75,863.1617907],
[1092.499397,1016.75],
[1026.65,538.0151455],
[1026.65,537.351],
[1024.877308,529.0590029],
[1002.37272,523.35],
[995.8071931,523.35],
[717.6588121,520.05],
[606.6805178,516.75],
[552.5646845,516.75],
[533.25,493.6852946],
[533.25,382.7460793],
[533.25,299.532134],
[533.25,244.043191],
[533.25,174.6869837],
[928.0653249,33.25],
[1011.272761,33.25],
[1413.521537,33.25],
[1455.137605,33.25],
[1516.75,244.3671276],
[1516.75,341.457188],
[1516.75,480.1548391],
[1302.477932,516.75]]

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

dist=[100,200,150,100,150,0,100,975,1825,50,550,175,725,175,150,750,125,375,300,25,
75,375,225,1050,1050,75,425,125,25,575,200,100,75,200,150,100,125,975,150,725,75,500,175,250,450]


ccnew=[]
count=[]
for i in range(len(calc_points)-1):
	count32=0
	cc32=[]
	r_subset2=[]
	print "distance", dist[44-i]
	for elem1 in calc_points[i]:
		for elem2 in calc_points[i+1]:
			if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=0.8*dist[44-i] and abs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])>=0.2*dist[44-i]:
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
	plt.plot(creation_points[45-i][0],creation_points[45-i][1],'go')
	plt.plot(uploader_points[45-i][0],uploader_points[45-i][1],'yo')
	plt.title(46-i)
	
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


