from math import fabs
import matplotlib.pyplot as plt

creation_points=[[516.75,39.95],
[516.75,101.438],
[516.75,309.182],
[516.75,475.436],
[516.75,235.698],
[533.25,578.612],
[523.35,519.833],
[588.838,1026.65],
[516.75,833.0544443],
[516.75,755.836],
[1020.05,993.971],
[1029.81431,1014.406938],
[1037.351,516.75],
[1028.279,533.25],
[1033.25,537.351],
[1113.136,529.95],
[1516.75,590.0641771],
[1516.75,544.77],
[1516.75,987.9717487],
[1516.75,807.6799513],
[1520.05,980.793],
[1026.65,825.1503107],
[1026.65,860.456],
[1026.65,818.857],
[1026.65,791.13],
[1161.855723,1016.75],
[1029.95,852.8902191],
[1026.65,694.075],
[1026.65,562.4662886],
[1026.65,541.4055379],
[1017.099,525.75],
[1026.65,546.67],
[1026.65,544.852],
[1026.65,666.335],
[962.556,520.05],
[1026.65,537.351],
[891.67,520.05],
[933.1220299,523.35],
[533.25,362.588],
[929.785,520.05],
[533.25,99.086],
[650.6748319,33.25],
[533.974,33.45],
[886.4570002,33.25],
[906.544,33.25],
[1017.517,33.25],
[1025.146548,33.25],
[1233.204204,33.25],
[1267.17,33.25],
[1441.168267,516.75]]

creation_distance=[1175,875,600,575,625,650,550,975,1575,1700,550,675,550,525,575,775,625,1250,550,975,850,650,700,700,725,1400,950,750,600,
575,575,1225,950,1725,725,1625,800,1600,625,1800,825,625,950,600,675,750,1575,1250,1800,625]

cc=[]
counts=[]

for i in range(len(creation_distance)):
	cc.append([])
	count=0
	for x in range(500,1502,5):
		for y in range(0,1002,5):
			if x%500==0 or y%500==0:
				if fabs(creation_points[i][0]-x) + fabs(creation_points[i][1]-y)<=creation_distance[i]:
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



uploader_points=[[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,512.649],
[516.75,585.5499884],
[516.75,722.0961892],
[516.75,763.7050762],
[1029.95,985.8833616],
[1029.95,948.0887894],
[1029.95,937.1795995],
[1029.95,734.4741519],
[1033.25,692.8639313],
[1033.25,538.3855048],
[1033.25,537.351],
[1033.308818,535.9289861],
[1514.05856,533.3070783],
[1516.75,918.6233145],
[1328.31637,1016.75],
[1245.092055,1016.75],
[1189.599448,1016.75],
[1064.759755,1016.75],
[1026.65,537.351],
[1026.65,537.351],
[1026.65,537.351],
[1026.65,537.351],
[1026.65,537.351],
[1026.65,537.351],
[1026.58251,535.8759052],
[1026.015571,531.8933289],
[1022.60276,526.1208705],
[745.3954603,520.05],
[703.7830013,520.05],
[689.9128324,516.75],
[592.8069487,516.75],
[552.5646845,516.75],
[533.25,452.0787647],
[533.25,410.4782884],
[533.25,35.98194259],
[567.4421145,33.25],
[664.5371086,33.25],
[941.930245,33.25],
[997.399337,33.25],
[1080.64027,33.25],
[1219.338471,33.25],
[1302.558309,33.25],
[1455.137605,33.25],
[1516.75,410.8036252],
[1516.75,438.5449759],
[1233.132715,516.75],
[1094.424488,516.75]]

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


ccc1=[]
for i in range(len(cc)-1,-1,-1):
	ccc1.append(cc[i])


#calc_points=[cc17,cc16,cc15,cc14,cc13,cc12,cc11,cc10,cc9,cc8,cc7,cc6,cc5,cc4,cc3,cc2,cc1]

print "number of points before"
for elem in calc_points:
	print len(elem),

print "wvrg"	

dist=[75,500,275,475,275,75,1600,100,25,375,75,350,825,475,1225,850,525,150,100,225,1050,25,75,
75,0,75,125,50,50,650,75,25,175,75,150,75,675,75,175,500,100,150,250,150,275,800,50,650,250]
ccnew=[]
count=[]
for i in range(len(calc_points)-1):
	count32=0
	cc32=[]
	r_subset2=[]
	print "distance", dist[48-i]
	for elem1 in calc_points[i]:
		for elem2 in calc_points[i+1]:
			if fabs(elem1[0]-elem2[0]) + fabs(elem1[1]-elem2[1])<=dist[48-i]:
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
	plt.plot(creation_points[49-i][0],creation_points[49-i][1],'go')
	plt.plot(uploader_points[49-i][0],uploader_points[49-i][1],'yo')
	plt.title(50-i)
	
	plt.ylim(ymax=1100,ymin=-100)
	plt.xlim(xmax=1600,xmin=400)
	i=i+1
	x=[]
	y=[]
	x2=[]
	y2=[]	
	plt.show()		



