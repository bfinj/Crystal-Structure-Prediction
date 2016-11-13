import re
import scipy.io
class Color:
	def __init__(self, colorr, colorg, colorb,colornum):
		self.r = colorr
		self.g = colorg
		self.b = colorb
		self.num = colornum
	def RDistanceSquare(self):
		self.RDS = (self.r - 1)*(self.r - 1) + self.g*self.g + self.b*self.b
		return self.RDS
	def BDistanceSquare(self):
		self.BDS = (self.b - 1)*(self.b - 1) + self.g*self.g + self.r*self.r
		return self.BDS
class Connection:
	def __init__(self, first, second, third, num):
		self.first = first
		self.second = second
		self.third = third
		self.num = num
#return the number of the reddist point of this triangle
	def SetR(self, RNum):
		self.RMax = RNum
	def SetB(self, BNum):
		self.BMax = BNum
class Coord:
	def __init__(self, first, second, third, num):
		self.first = first
		self.second = second
		self.third = third
		self.num = num
	def ReturnP(self, num):
		if num == 0:
			return self.first
		if num == 1:
			return self.second
		if num == 2:
			return self.third
class Point:
	def __init__(self, first, second, third, num):
		self.first = first
		self.second = second
		self.third = third
		self.num = num
	def RDis(self, RDisSqu):
		self.RDisSqu = RDisSqu
	def BDis(self, BDisSqu):
		self.BDisSqu = BDisSqu
class Normal:
	def __init__(self, first, second, third, num):
		self.first = first
		self.second = second
		self.third = third
		self.num = num
class NormalIndex:
	def __init__(self, first, second, third, num):
		self.first = first
		self.second = second
		self.third = third
		self.num = num
fil = open("ZZZTXI.VRML")
sStr2 = '] }'
ColorArr = []
while 1:
	line = fil.readline()
	if not line:
		break
	m = re.search('color Color', line)
	if bool(m):
		count = 0
		while 1:
			line = fil.readline()
			m = re.search(sStr2, line)
			if bool(m):
				break
			floats = [float(x) for x in line.split()]
			ColorArr.append(Color(floats[0],floats[1],floats[2], count))
			count = count + 1
		break
fil.close()
f = open("ZZZTXI.VRML")
sStr3 = 'colorIndex ['
sStr4 = ']'
ConnectionArr = []
while 1:
	line = f.readline()
	if not line:
		break
	m = re.search('colorIndex', line)
	if bool(m):
		count = 0
		while 1:
			line = f.readline()
			m = re.search(']', line)
			if bool(m):
				break
			colorindices = [int(x) for x in line.split()]
			ConnectionArr.append(Connection(colorindices[0],colorindices[1],colorindices[2], count))
			count = count + 1
		break
for triangle in ConnectionArr:
	if ColorArr[triangle.first].RDistanceSquare()>ColorArr[triangle.second].RDistanceSquare() and ColorArr[triangle.first].RDistanceSquare()>ColorArr[triangle.third].RDistanceSquare():
		triangle.SetR(0)
	if ColorArr[triangle.second].RDistanceSquare()>ColorArr[triangle.first].RDistanceSquare() and ColorArr[triangle.second].RDistanceSquare()>ColorArr[triangle.third].RDistanceSquare():
		triangle.SetR(1)
	if ColorArr[triangle.third].RDistanceSquare()>ColorArr[triangle.second].RDistanceSquare() and ColorArr[triangle.third].RDistanceSquare()>ColorArr[triangle.first].RDistanceSquare():
		triangle.SetR(2)
	if ColorArr[triangle.first].RDistanceSquare()==ColorArr[triangle.second].RDistanceSquare() and ColorArr[triangle.first].RDistanceSquare()>ColorArr[triangle.third].RDistanceSquare():
		triangle.SetR(3)
	if ColorArr[triangle.first].RDistanceSquare()==ColorArr[triangle.third].RDistanceSquare() and ColorArr[triangle.first].RDistanceSquare()>ColorArr[triangle.second].RDistanceSquare():
		triangle.SetR(4)
	if ColorArr[triangle.third].RDistanceSquare()==ColorArr[triangle.second].RDistanceSquare() and ColorArr[triangle.first].RDistanceSquare()<ColorArr[triangle.third].RDistanceSquare():
		triangle.SetR(5)
	if ColorArr[triangle.first].RDistanceSquare()==ColorArr[triangle.second].RDistanceSquare() and ColorArr[triangle.first].RDistanceSquare()==ColorArr[triangle.third].RDistanceSquare():
		triangle.SetR(6)
	if ColorArr[triangle.first].BDistanceSquare()>ColorArr[triangle.second].BDistanceSquare() and ColorArr[triangle.first].BDistanceSquare()>ColorArr[triangle.third].BDistanceSquare():
		triangle.SetB(0)
	if ColorArr[triangle.second].BDistanceSquare()>ColorArr[triangle.first].BDistanceSquare() and ColorArr[triangle.second].BDistanceSquare()>ColorArr[triangle.third].BDistanceSquare():
		triangle.SetB(1)
	if ColorArr[triangle.third].BDistanceSquare()>ColorArr[triangle.second].BDistanceSquare() and ColorArr[triangle.third].BDistanceSquare()>ColorArr[triangle.first].BDistanceSquare():
		triangle.SetB(2)
	if ColorArr[triangle.first].BDistanceSquare()==ColorArr[triangle.second].BDistanceSquare() and ColorArr[triangle.first].BDistanceSquare()>ColorArr[triangle.third].BDistanceSquare():
		triangle.SetB(3)
	if ColorArr[triangle.first].BDistanceSquare()==ColorArr[triangle.third].BDistanceSquare() and ColorArr[triangle.first].BDistanceSquare()>ColorArr[triangle.second].BDistanceSquare():
		triangle.SetB(4)
	if ColorArr[triangle.third].BDistanceSquare()==ColorArr[triangle.second].BDistanceSquare() and ColorArr[triangle.first].BDistanceSquare()<ColorArr[triangle.third].BDistanceSquare():
		triangle.SetB(5)
	if ColorArr[triangle.first].BDistanceSquare()==ColorArr[triangle.second].BDistanceSquare() and ColorArr[triangle.first].BDistanceSquare()==ColorArr[triangle.third].BDistanceSquare():
		triangle.SetB(6)
f.close()
ff = open("ZZZTXI.VRML")
CoordArr = []
while 1:
	line = ff.readline()
	if not line:
		break
	m = re.search('coordIndex', line)
	if bool(m):
		count = 0
		while 1:
			line = ff.readline()
			m = re.search(']', line)
			if bool(m):
				break
			coords = [int(x) for x in line.split()]
			CoordArr.append(Coord(coords[0],coords[1],coords[2], count))
			count = count + 1
		break
ff.close()
fff = open("ZZZTXI.VRML")
PointArr = []
while 1:
	line = fff.readline()
	if not line:
		break
	m = re.search('point', line)
	n = re.search('View', line)
	o = re.search('grid', line)
	if bool(m and not n and not o):
		count = 0
		while 1:
			line = fff.readline()
			m = re.search(']', line)
			if bool(m):
				break
			points = [float(x) for x in line.split()]
			PointArr.append(Point(points[0], points[1], points[2], count))
			count = count + 1
		break
fff.close()
ffff = open("ZZZTXI.VRML")
NormalArr = []
while 1:
	line = ffff.readline()
	if not line:
		break
	m = re.search('vector', line)
	if bool(m):
		count = 0
		while 1:
			line = ffff.readline()
			m = re.search(']', line)
			if bool(m):
				break
			normals = [float(x) for x in line.split()]
			NormalArr.append(Normal(normals[0], normals[1], normals[2], count))
			count = count + 1
		break
ffff.close()
fffff = open("ZZZTXI.VRML")
NormalIndexArr = []
while 1:
	line = fffff.readline()
	if not line:
		break
	m = re.search('normalIndex', line)
	if bool(m):
		count = 0
		while 1:
			line = fffff.readline()
			m = re.search(']', line)
			if bool(m):
				break
			normalindices = [int(x) for x in line.split()]
			NormalIndexArr.append(NormalIndex(normalindices[0], normalindices[1], normalindices[2], count))
			count = count + 1
		break
fffff.close()
for APoint in PointArr:
	for ACoord in CoordArr:
		if APoint.num == ACoord.first:
			APoint.RDis(ColorArr[ConnectionArr[ACoord.num].first].RDistanceSquare())
			break
		if APoint.num == ACoord.second:
			APoint.RDis(ColorArr[ConnectionArr[ACoord.num].second].RDistanceSquare())
			break
		if APoint.num == ACoord.third:
			APoint.RDis(ColorArr[ConnectionArr[ACoord.num].third].RDistanceSquare())
			break
for APoint in PointArr:
	for ACoord in CoordArr:
		if APoint.num == ACoord.first:
			APoint.BDis(ColorArr[ConnectionArr[ACoord.num].first].BDistanceSquare())
			break
		if APoint.num == ACoord.second:
			APoint.BDis(ColorArr[ConnectionArr[ACoord.num].second].BDistanceSquare())
			break
		if APoint.num == ACoord.third:
			APoint.BDis(ColorArr[ConnectionArr[ACoord.num].third].BDistanceSquare())
			break
RR = []
BB = []
TempRDisSqu = 0.3
TempBDisSqu = 0.2
StrRNum=-1
StrBNum=-1
for RPoint in PointArr:
	if RPoint.RDisSqu < 0.3:
		RR.append(RPoint)
		if RPoint.RDisSqu<TempRDisSqu:
			TempRDisSqu=RPoint.RDisSqu
			StrRNum=RPoint.num
#N = 0
#for P in RR:
#	print('draw pt'+str(N)+' {'+str(P.first)+','+str(P.second)+','+str(P.third)+'}')
#	N = N + 1
for BPoint in PointArr:
	if BPoint.BDisSqu < 0.2:
		BB.append(BPoint)
		if BPoint.BDisSqu<TempBDisSqu:
			TempBDisSqu=RPoint.BDisSqu
			StrBNum=BPoint.num
import sys
import numpy as np
from sklearn.cluster import KMeans
RMatrix = np.zeros((len(RR),3))
BMatrix = np.zeros((len(BB),3))
Temp = 0
for EachPoint in RR:
	RMatrix[Temp, 0] = EachPoint.first
	RMatrix[Temp, 1] = EachPoint.second
	RMatrix[Temp, 2] = EachPoint.third
	Temp = Temp + 1
Temp = 0
for EachPoint in BB:
	BMatrix[Temp, 0] = EachPoint.first
	BMatrix[Temp, 1] = EachPoint.second
	BMatrix[Temp, 2] = EachPoint.third
	Temp = Temp + 1
#clustering analysis
import itertools
clf1 = KMeans(n_clusters = 12)
s1 = clf1.fit(RMatrix)
clf2 = KMeans(n_clusters = 2)
s2 = clf2.fit(BMatrix)
#find the nearest point of the cluster center
Nearest = 0
BNMatrix = np.zeros((2, 3))
RNMatrix = np.zeros((12, 3))
hang = 0
for row in clf1.cluster_centers_:
	D = 1
	for P in PointArr:
		if (P.first-row[0])**2+(P.second-row[1])**2+(P.third-row[2])**2<D:
			D = (P.first-row[0])**2+(P.second-row[1])**2+(P.third-row[2])**2
			Nearest = P.num
	RNMatrix[hang][0]=PointArr[Nearest].first
	RNMatrix[hang][1]=PointArr[Nearest].second
	RNMatrix[hang][2]=PointArr[Nearest].third
	hang = hang + 1
hang = 0
for row in clf2.cluster_centers_:
	D = 1
	for P in PointArr:
		if (P.first-row[0])**2+(P.second-row[1])**2+(P.third-row[2])**2<D:
			D = (P.first-row[0])**2+(P.second-row[1])**2+(P.third-row[2])**2
			Nearest = P.num
	BNMatrix[hang][0]=PointArr[Nearest].first
	BNMatrix[hang][1]=PointArr[Nearest].second
	BNMatrix[hang][2]=PointArr[Nearest].third
	hang = hang + 1
#end of nearest
RVMatrix = np.zeros((12, 3))
BVMatrix = np.zeros((2, 3))
count = 0
#StrRTemp=10000
#StrBTemp=10000
#StrR=-1
#StrB=-1
#for row in clf1.cluster_centers_:
for row in RNMatrix:
	#Distance1 = 1
	cls1 = []
	xsum=0
	ysum=0
	zsum=0
	for APoint in PointArr:
		Distance = (row[0]-APoint.first)**2+(row[1]-APoint.second)**2+(row[2]-APoint.third)**2
		if Distance < 1:
			cls1.append(APoint.num)
			#Distance1 = Distance
			for Triangles in CoordArr:
				if APoint.num == Triangles.first:
					xsum = NormalArr[NormalIndexArr[Triangles.num].first].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].first].second+ysum
					zsum = NormalArr[NormalIndexArr[Triangles.num].first].third+zsum
					break
				if APoint.num == Triangles.second:
					xsum = NormalArr[NormalIndexArr[Triangles.num].second].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].second].second+ysum
					zsum = NormalArr[NormalIndexArr[Triangles.num].second].third+zsum
					break
				if APoint.num == Triangles.third:
					xsum = NormalArr[NormalIndexArr[Triangles.num].third].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].third].second+ysum
					zsum = NormalArr[NormalIndexArr[Triangles.num].third].third+zsum
					break
	RVMatrix[count,0]=xsum/len(cls1)
	RVMatrix[count,1]=ysum/len(cls1)
	RVMatrix[count,2]=zsum/len(cls1)
		#StrR=count
	count = count + 1
#Nearest2 = 0
count = 0
#for row in clf2.cluster_centers_:
for row in BNMatrix:
	#Distance2 = 1
	cls2=[]
	xsum=0
	ysum=0
	zsum=0
	for APoint in PointArr:
		Distance = (row[0]-APoint.first)**2+(row[1]-APoint.second)**2+(row[2]-APoint.third)**2
		if Distance < 1:
			cls2.append(APoint.num)
			#Distance2 = Distance
			for Triangles in CoordArr:
				if APoint.num == Triangles.first:
					xsum = NormalArr[NormalIndexArr[Triangles.num].first].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].first].second+ysum
					zsum = NormalArr[NormalIndexArr[Triangles.num].first].third+zsum
					break
				if APoint.num == Triangles.second:
					xsum = NormalArr[NormalIndexArr[Triangles.num].second].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].second].second+ysum
					zsum = NormalArr[NormalIndexArr[Triangles.num].second].third+zsum
					break
				if APoint.num == Triangles.third:
					xsum = NormalArr[NormalIndexArr[Triangles.num].third].first+xsum
					ysum = NormalArr[NormalIndexArr[Triangles.num].third].second+ysum
					zsum= NormalArr[NormalIndexArr[Triangles.num].third].third+zsum
					break
	BVMatrix[count,0]=xsum/len(cls2)
	BVMatrix[count,1]=ysum/len(cls2)
	BVMatrix[count,2]=zsum/len(cls2)
	count = count + 1
#for row in clf1.cluster_centers_:
#	print('draw ptr'+str(row[0])+' {'+str(row[0])+','+str(row[1])+','+str(row[2])+'}')
for i in range(12):
	print('draw ptr'+str(i)+' {'+str(RNMatrix[i][0])+','+str(RNMatrix[i][1])+','+str(RNMatrix[i][2])+'}')
scipy.io.savemat('saveddata.mat', {'RPT':RNMatrix, 'BPT':BNMatrix, 'RVT':RVMatrix, 'BVT':BVMatrix})
#scipy.io.savemat('zzzstr.mat',{'RPT':clf1.cluster_centers_[StrR,:],'BPT':clf2.cluster_centers_[StrB,:],'RVT':RVMatrix[StrR,:],'BVT':BVMatrix[StrB,:],'RT':clf1.cluster_centers_,'BT':clf2.cluster_centers_})
