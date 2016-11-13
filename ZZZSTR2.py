import numpy as np
import re
import scipy.io as sio
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
#Start rotation!
M1 = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
M2 = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
M3 = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
PointTable = [[0 for i in range(len(PointArr))] for j in range(3)]
for Points in PointArr:
	PointTable[0][Points.num] = Points.first
	PointTable[1][Points.num] = Points.second
	PointTable[2][Points.num] = Points.third
NormalTable = [[0 for i in range(len(NormalArr))] for j in range(3)]
for Normals in NormalArr:
	NormalTable[0][Normals.num] = Normals.first
	NormalTable[1][Normals.num] = Normals.second
	NormalTable[2][Normals.num] = Normals.third
data2 = sio.loadmat('saveddata.mat')
#RT = data2['RPT']
RT = np.transpose(data2['RPT'])
RedTable=[[0,0],[0,0],[0,0]]
BlueTable=[[0,0],[0,0],[0,0]]
#BT = data2['BPT']
BT = np.transpose(data2['BPT'])
T = [0, 0, 0]
OutFile = open('outputSTR', 'w')
for i in range(12):
	for j in range(2):
		matfn = 'esp'+str(i+1)+str(j+1)+'.mat'
		data = sio.loadmat(matfn)
		Rint = data['Results']
		for m in range(12):
			for k in range(2):
				for n in range(3):
					RedTable[n][0]=RT[n][i]
					BlueTable[n][0]=BT[n][j]
					RedTable[n][1]=RT[n][m]
					BlueTable[n][1]=BT[n][k]
				NewRT1 = np.dot(Rint, RedTable)
				NewRT2 = np.dot(M1, NewRT1)
				NewRT3 = np.dot(M2, NewRT1)
				NewRT4 = np.dot(M3, NewRT1)
				NewBT1 = np.dot(Rint, BlueTable)
				NewBT2 = np.dot(M1, NewBT1)
				NewBT3 = np.dot(M2, NewBT1)
				NewBT4 = np.dot(M3, NewBT1)
#print NewRT1
#print NewBT2
#print NewBT1
#print NewRT4
				a=2*(NewRT1[0][0]-NewBT2[0][0])
				T[2]=0.5*(NewBT2[2][0]-NewRT1[2][0])
				#T[1]=0.5*(NewBT4[1][1]-NewRT1[1][1])
				#T[0]=0.5*(0.5*a+NewBT4[0][1]-NewRT1[0][1])
				#b=2*(2*T[1]+NewRT1[1][0]-NewBT2[1][0])
				b=2*(NewRT4[1][1]-NewBT2[1][1])
				T[0]=0.5*(NewRT4[0][1]-NewBT2[0][1])
				T[1]=0.5*(0.5*b+NewBT2[1][0]-NewRT1[1][0])
				c=2*(-2*T[2]+NewBT2[2][1]-NewRT4[2][1])
				#c=2*(NewRT1[2][1]-NewBT4[2][1])
				if max(abs(a),abs(b),abs(c))<15.5 and max(abs(a),abs(b),abs(c))>12.5 and min(abs(a),abs(b),abs(c))>3.4 and min(abs(a),abs(b),abs(c))<6.4 and abs(a)+abs(b)+abs(c)-max(abs(a),abs(b),abs(c))-min(abs(a),abs(b),abs(c))>12.1 and abs(a)+abs(b)+abs(c)-max(abs(a),abs(b),abs(c))-min(abs(a),abs(b),abs(c))<15.1:
					OutFile.write(matfn)
					OutFile.write('\nT=['+str(T[0])+','+str(T[1])+','+str(T[2])+']\n')
					OutFile.write('T2=['+str(0.5*a)+','+str(0.5*b)+','+str(0)+']\n')
					OutFile.write('T3=['+str(0)+','+str(0.5*b)+','+str(0.5*c)+']\n')
					OutFile.write('T4=['+str(0.5*a)+',0,'+str(0.5*c)+']\n')
				#T[0]=0.5*(NewBT3[0][1]-NewRT1[0][1])
				#b=2*(NewRT1[1][1]-NewBT3[1][1])
				#T[1]=0.5*(0.5*b+NewBT2[1][0]-NewRT1[1][0])
				#c=2*(2*T[2]+NewRT1[2][1]-NewBT3[2][1])
				T[0]=0.5*(NewRT3[0][1]-NewBT2[0][1]-0.5*a)
				T[1]=0.5*(NewBT2[1][1]-NewRT3[1][1])
				b=2*(2*T[1]+NewRT1[1][0]-NewBT2[1][0])
				c=2*(NewBT2[2][1]-NewRT3[2][1])
				if max(abs(a),abs(b),abs(c))<15.5 and max(abs(a),abs(b),abs(c))>12.5 and min(abs(a),abs(b),abs(c))>3.4 and min(abs(a),abs(b),abs(c))<6.4 and abs(a)+abs(b)+abs(c)-max(abs(a),abs(b),abs(c))-min(abs(a),abs(b),abs(c))>12.1 and abs(a)+abs(b)+abs(c)-max(abs(a),abs(b),abs(c))-min(abs(a),abs(b),abs(c))<15.1:
					OutFile.write(matfn)
					OutFile.write('\nT=['+str(T[0])+','+str(T[1])+','+str(T[2])+']\n')
					OutFile.write('T2=['+str(0.5*a)+','+str(0.5*b)+','+str(0)+']\n')
					OutFile.write('T3=['+str(0)+','+str(0.5*b)+','+str(0.5*c)+']\n')
					OutFile.write('T4=['+str(0.5*a)+',0,'+str(0.5*c)+']\n')
OutFile.close()
