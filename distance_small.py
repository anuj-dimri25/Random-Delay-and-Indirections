from math import fabs
import matplotlib.pyplot as plt

cc1=[]
count1=0
for x in range(500,1502,5):
	for y in range(0,1001,5):
		if x%500==0 or y%500==0:
			if fabs(1033.25-x)+fabs(557.66-y)<=950:
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





points=[[1033.25,557.66],[1016.75,499,377],[1016.75,512.649],[1033.25,537.351],[1016.75,499.648],[783,523.35],[517.775,533.25],[516.75,288.5],
[523.35,757.17],[523.35,796.12],[544.25,1026.65],[738.421,1026.65],[877.107,1026.65],[1033.25,544.852],[1029.95,890],[1033.25,537.351],[1033.25,546.95]]
	
x=[]
y=[]		
i=0
#print cc1	
cc=[cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10,cc11,cc12,cc13,cc14,cc15,cc16,cc17]
for ccc1 in cc:
	for elem in ccc1:
		#print elem[0]
		x.append(elem[0])
		y.append(elem[1])		
	plt.scatter(x,y)
	plt.plot(points[i][0],points[i][1],'ro')
	plt.ylim(ymax=1100,ymin=-100)
	plt.xlim(xmax=1600,xmin=400)
	i=i+1	
	plt.show()		


