import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import Tk
from tkinter import SUNKEN, RAISED, END
from dataclasses import dataclass

#controls !@!!!!!!!!!!1One Hot Encoding Uniqueness quantification Hamming weight
class RHv2(tk.Frame):
	def __init__(mainWindow, parent):
		tk.Frame.__init__(mainWindow, parent)
		
		#prep input box for two-way
		text	= tk.StringVar()
		text.trace('w', lambda name, index, mode, text=text: RHv2.on_type(mainWindow,text))
		mainWindow.output	= tk.Entry(mainWindow, width=20, textvariable=text)
		RHv2.assess = text
		mainWindow.output.insert(0,'0')
		
		#buttons
		mainWindow.clippy	= tk.Button(mainWindow, text='Copy To Clipboard',command=mainWindow.clippy)
		mainWindow.A		= tk.Button(mainWindow, text='Aerate',	command=mainWindow.toggleA)
		mainWindow.B		= tk.Button(mainWindow, text='Brittle',	command=mainWindow.toggleB)
		mainWindow.C		= tk.Button(mainWindow, text='Cold',	command=mainWindow.toggleC)
		mainWindow.D		= tk.Button(mainWindow, text='Dense',	command=mainWindow.toggleD)
		mainWindow.E		= tk.Button(mainWindow, text='Elastic',	command=mainWindow.toggleE)
		mainWindow.F		= tk.Button(mainWindow, text='Fuel',	command=mainWindow.toggleF)
		mainWindow.G		= tk.Button(mainWindow, text='Gas',		command=mainWindow.toggleG)
		mainWindow.H		= tk.Button(mainWindow, text='Hot',		command=mainWindow.toggleH)
		mainWindow.I		= tk.Button(mainWindow, text='Inflow',	command=mainWindow.toggleI)
		mainWindow.J		= tk.Button(mainWindow, text='Jet',		command=mainWindow.toggleJ)
		mainWindow.K		= tk.Button(mainWindow, text='Rice',	command=mainWindow.toggleK)
		mainWindow.L		= tk.Button(mainWindow, text='Light',	command=mainWindow.toggleL)
		mainWindow.M		= tk.Button(mainWindow, text='Mochi',	command=mainWindow.toggleM)
		mainWindow.N		= tk.Button(mainWindow, text='Novel',	command=mainWindow.toggleN)
		mainWindow.O		= tk.Button(mainWindow, text='Outflow',	command=mainWindow.toggleO)
		mainWindow.P		= tk.Button(mainWindow, text='Powder',	command=mainWindow.toggleP)
		mainWindow.Q		= tk.Button(mainWindow, text='Water',	command=mainWindow.toggleQ)
		mainWindow.R		= tk.Button(mainWindow, text='Rigid',	command=mainWindow.toggleR)
		mainWindow.S		= tk.Button(mainWindow, text='String',	command=mainWindow.toggleS)
		mainWindow.T		= tk.Button(mainWindow, text='Tensile',	command=mainWindow.toggleT)
		mainWindow.U		= tk.Button(mainWindow, text='Users',	command=mainWindow.toggleU)
		mainWindow.V		= tk.Button(mainWindow, text='Viscous',	command=mainWindow.toggleV)
		mainWindow.W		= tk.Button(mainWindow, text='Wall',	command=mainWindow.toggleW)
		mainWindow.X		= tk.Button(mainWindow, text='Axis',	command=mainWindow.toggleX)
		mainWindow.Y		= tk.Button(mainWindow, text='Snow',	command=mainWindow.toggleY)
		mainWindow.Z		= tk.Button(mainWindow, text='Delete',	command=mainWindow.toggleZ)
		mainWindow.E1		= tk.Button(mainWindow, text='Alpha',	command=mainWindow.toggleE1)
		mainWindow.E2		= tk.Button(mainWindow, text='Beta',	command=mainWindow.toggleE2)
		mainWindow.E3		= tk.Button(mainWindow, text='Gamma',	command=mainWindow.toggleE3)
		mainWindow.E4		= tk.Button(mainWindow, text='Delta',	command=mainWindow.toggleE4)
		mainWindow.E5		= tk.Button(mainWindow, text='Epsilon',	command=mainWindow.toggleE5)
		mainWindow.E6		= tk.Button(mainWindow, text='Zeta',	command=mainWindow.toggleE6)
		RHv2.orig_color = mainWindow.A.cget("background")#catch system default button color
		
		#org
		mainWindow.output.grid(row=9,column=1,columnspan=2)
		mainWindow.clippy.grid(row=9,column=3,columnspan=2)
		mainWindow.A	 .grid(column=1,row=1,sticky='ew')
		mainWindow.B	 .grid(column=2,row=1,sticky='ew')
		mainWindow.C	 .grid(column=3,row=1,sticky='ew')
		mainWindow.D	 .grid(column=4,row=1,sticky='ew')
		mainWindow.E	 .grid(column=1,row=2,sticky='ew')
		mainWindow.F	 .grid(column=2,row=2,sticky='ew')
		mainWindow.G	 .grid(column=3,row=2,sticky='ew')
		mainWindow.H	 .grid(column=4,row=2,sticky='ew')
		mainWindow.I	 .grid(column=1,row=3,sticky='ew')
		mainWindow.J	 .grid(column=2,row=3,sticky='ew')
		mainWindow.K	 .grid(column=3,row=3,sticky='ew')
		mainWindow.L	 .grid(column=4,row=3,sticky='ew')
		mainWindow.M	 .grid(column=1,row=4,sticky='ew')
		mainWindow.N	 .grid(column=2,row=4,sticky='ew')
		mainWindow.O	 .grid(column=3,row=4,sticky='ew')
		mainWindow.P	 .grid(column=4,row=4,sticky='ew')
		mainWindow.Q	 .grid(column=1,row=5,sticky='ew')
		mainWindow.R	 .grid(column=2,row=5,sticky='ew')
		mainWindow.S	 .grid(column=3,row=5,sticky='ew')
		mainWindow.T	 .grid(column=4,row=5,sticky='ew')
		mainWindow.U	 .grid(column=1,row=6,sticky='ew')
		mainWindow.V	 .grid(column=2,row=6,sticky='ew')
		mainWindow.W	 .grid(column=3,row=6,sticky='ew')
		mainWindow.X	 .grid(column=4,row=6,sticky='ew')
		mainWindow.Y	 .grid(column=1,row=7,sticky='ew')
		mainWindow.Z	 .grid(column=2,row=7,sticky='ew')
		mainWindow.E1	 .grid(column=3,row=7,sticky='ew')
		mainWindow.E2	 .grid(column=4,row=7,sticky='ew')
		mainWindow.E3	 .grid(column=1,row=8,sticky='ew')
		mainWindow.E4	 .grid(column=2,row=8,sticky='ew')
		mainWindow.E5	 .grid(column=3,row=8,sticky='ew')
		mainWindow.E6	 .grid(column=4,row=8,sticky='ew')
		
	
	#conts
	yes: str = '1'
	no:  str = '0'
	orig_color = ''
	
	#vars
	a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=e1=e2=e3=e4=e5=e6 = no
	numOut	= '0'
	binIn	= [0]
	hexNum	= 0
	assess = ''
	
	#copy to board
	def clippy(mainWindow):
		clip = Tk()
		clip.withdraw()
		clip.clipboard_clear()
		clip.clipboard_append(RHv2.hexNum)
		clip.destroy()
	
	#calc hex from button input
	def output(mainWindow):
		#bind button inputs to char array
		RHv2.binIn = mainWindow.e6+mainWindow.e5+mainWindow.e4+mainWindow.e3+mainWindow.e2+mainWindow.e1+mainWindow.z+mainWindow.y+mainWindow.x+mainWindow.w+mainWindow.v+mainWindow.u+mainWindow.t+mainWindow.s+mainWindow.r+mainWindow.q+mainWindow.p+mainWindow.o+mainWindow.n+mainWindow.m+mainWindow.l+mainWindow.k+mainWindow.j+mainWindow.i+mainWindow.h+mainWindow.g+mainWindow.f+mainWindow.e+mainWindow.d+mainWindow.c+mainWindow.b+mainWindow.a
		RHv2.numOut = RHv2.binIn #bind char array to string
		RHv2.hexNum = format((int(RHv2.numOut, 2)),'x') #conv string to integer then represent as hex with no prefix
		
		#clear and update display
		mainWindow.output.delete(0,END)
		mainWindow.output.insert(0,RHv2.hexNum)
	
	#converts user input to binary switchboard
	def on_type(mainWindow,text_var):
		try:
			binRep = bin(int(RHv2.assess.get(), 16))[2:].zfill(32)
			RHv2.autoPress(mainWindow,binRep)#auto-presses buttons based on typed input
			RHv2.hexNum = RHv2.assess.get()#lets user immediately copy their own input
		except:#potential sanity check? doesn't seem to work
			RHv2.a=RHv2.b=RHv2.c=RHv2.d=RHv2.e=RHv2.f=RHv2.g=RHv2.h=RHv2.i=RHv2.j=RHv2.k=RHv2.l=RHv2.m=RHv2.n=RHv2.o=RHv2.p=RHv2.q=RHv2.r=RHv2.s=RHv2.t=RHv2.u=RHv2.v=RHv2.w=RHv2.x=RHv2.y=RHv2.z=RHv2.e1=RHv2.e2=RHv2.e3=RHv2.e4=RHv2.e5=RHv2.e6 = RHv2.no

	#dynamically depress buttons based on input
	def autoPress(mainWindow, materials):
		if materials[31] == RHv2.yes:
			mainWindow.a = mainWindow.yes
			mainWindow.A.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.a = mainWindow.no
			mainWindow.A.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[30] == RHv2.yes:
			mainWindow.b = mainWindow.yes
			mainWindow.B.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.b = mainWindow.no
			mainWindow.B.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[29] == RHv2.yes:
			mainWindow.c = mainWindow.yes
			mainWindow.C.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.c = mainWindow.no
			mainWindow.C.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[28] == RHv2.yes:
			mainWindow.d = mainWindow.yes
			mainWindow.D.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.d = mainWindow.no
			mainWindow.D.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[27] == RHv2.yes:
			mainWindow.e = mainWindow.yes
			mainWindow.E.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e = mainWindow.no
			mainWindow.E.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[26] == RHv2.yes:
			mainWindow.f = mainWindow.yes
			mainWindow.F.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.f = mainWindow.no
			mainWindow.F.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[25] == RHv2.yes:
			mainWindow.g = mainWindow.yes
			mainWindow.G.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.g = mainWindow.no
			mainWindow.G.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[24] == RHv2.yes:
			mainWindow.h = mainWindow.yes
			mainWindow.H.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.h = mainWindow.no
			mainWindow.H.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[23] == RHv2.yes:
			mainWindow.i = mainWindow.yes
			mainWindow.I.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.i = mainWindow.no
			mainWindow.I.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[22] == RHv2.yes:
			mainWindow.j = mainWindow.yes
			mainWindow.J.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.j = mainWindow.no
			mainWindow.J.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[21] == RHv2.yes:
			mainWindow.k = mainWindow.yes
			mainWindow.K.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.k = mainWindow.no
			mainWindow.K.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[20] == RHv2.yes:
			mainWindow.l = mainWindow.yes
			mainWindow.L.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.l = mainWindow.no
			mainWindow.L.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[19] == RHv2.yes:
			mainWindow.m = mainWindow.yes
			mainWindow.M.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.m = mainWindow.no
			mainWindow.M.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[18] == RHv2.yes:
			mainWindow.n = mainWindow.yes
			mainWindow.N.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.n = mainWindow.no
			mainWindow.N.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[17] == RHv2.yes:
			mainWindow.o = mainWindow.yes
			mainWindow.O.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.o = mainWindow.no
			mainWindow.O.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[16] == RHv2.yes:
			mainWindow.p = mainWindow.yes
			mainWindow.P.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.p = mainWindow.no
			mainWindow.P.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[15] == RHv2.yes:
			mainWindow.q = mainWindow.yes
			mainWindow.Q.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.q = mainWindow.no
			mainWindow.Q.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[14] == RHv2.yes:
			mainWindow.r = mainWindow.yes
			mainWindow.R.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.r = mainWindow.no
			mainWindow.R.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[13] == RHv2.yes:
			mainWindow.s = mainWindow.yes
			mainWindow.S.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.s = mainWindow.no
			mainWindow.S.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[12] == RHv2.yes:
			mainWindow.t = mainWindow.yes
			mainWindow.T.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.t = mainWindow.no
			mainWindow.T.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[11] == RHv2.yes:
			mainWindow.u = mainWindow.yes
			mainWindow.U.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.u = mainWindow.no
			mainWindow.U.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[10] == RHv2.yes:
			mainWindow.v = mainWindow.yes
			mainWindow.V.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.v = mainWindow.no
			mainWindow.V.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[9] == RHv2.yes:
			mainWindow.w = mainWindow.yes
			mainWindow.W.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.w = mainWindow.no
			mainWindow.W.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[8] == RHv2.yes:
			mainWindow.x = mainWindow.yes
			mainWindow.X.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.x = mainWindow.no
			mainWindow.X.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[7] == RHv2.yes:
			mainWindow.y = mainWindow.yes
			mainWindow.Y.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.y = mainWindow.no
			mainWindow.Y.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[6] == RHv2.yes:
			mainWindow.z = mainWindow.yes
			mainWindow.Z.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.z = mainWindow.no
			mainWindow.Z.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[5] == RHv2.yes:
			mainWindow.e1 = mainWindow.yes
			mainWindow.E1.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e1 = mainWindow.no
			mainWindow.E1.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[4] == RHv2.yes:
			mainWindow.e2 = mainWindow.yes
			mainWindow.E2.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e2 = mainWindow.no
			mainWindow.E2.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[3] == RHv2.yes:
			mainWindow.e3 = mainWindow.yes
			mainWindow.E3.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e3 = mainWindow.no
			mainWindow.E3.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[2] == RHv2.yes:
			mainWindow.e4 = mainWindow.yes
			mainWindow.E4.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e4 = mainWindow.no
			mainWindow.E4.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[1] == RHv2.yes:
			mainWindow.e5 = mainWindow.yes
			mainWindow.E5.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e5 = mainWindow.no
			mainWindow.E5.config(relief=RAISED,bg=RHv2.orig_color)
		if materials[0] == RHv2.yes:
			mainWindow.e6 = mainWindow.yes
			mainWindow.E6.config(relief=SUNKEN,bg='grey')
		else:
			mainWindow.e6 = mainWindow.no
			mainWindow.E6.config(relief=RAISED,bg=RHv2.orig_color)
			
	
	#material logic
	def toggleA(mainWindow):
		if mainWindow.a != mainWindow.yes:
			mainWindow.a = mainWindow.yes
			mainWindow.A.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.a = mainWindow.no
			mainWindow.A.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleB(mainWindow):
		if mainWindow.b != mainWindow.yes:
			mainWindow.b = mainWindow.yes
			mainWindow.B.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.b = mainWindow.no
			mainWindow.B.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleC(mainWindow):
		if mainWindow.c != mainWindow.yes:
			mainWindow.c = mainWindow.yes
			mainWindow.C.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.c = mainWindow.no
			mainWindow.C.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleD(mainWindow):
		if mainWindow.d != mainWindow.yes:
			mainWindow.d = mainWindow.yes
			mainWindow.D.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.d = mainWindow.no
			mainWindow.D.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE(mainWindow):
		if mainWindow.e != mainWindow.yes:
			mainWindow.e = mainWindow.yes
			mainWindow.E.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e = mainWindow.no
			mainWindow.E.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleF(mainWindow):
		if mainWindow.f != mainWindow.yes:
			mainWindow.f = mainWindow.yes
			mainWindow.F.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.f = mainWindow.no
			mainWindow.F.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleG(mainWindow):
		if mainWindow.g != mainWindow.yes:
			mainWindow.g = mainWindow.yes
			mainWindow.G.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.g = mainWindow.no
			mainWindow.G.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleH(mainWindow):
		if mainWindow.h != mainWindow.yes:
			mainWindow.h = mainWindow.yes
			mainWindow.H.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.h = mainWindow.no
			mainWindow.H.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleI(mainWindow):
		if mainWindow.i != mainWindow.yes:
			mainWindow.i = mainWindow.yes
			mainWindow.I.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.i = mainWindow.no
			mainWindow.I.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleJ(mainWindow):
		if mainWindow.j != mainWindow.yes:
			mainWindow.j = mainWindow.yes
			mainWindow.J.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.j = mainWindow.no
			mainWindow.J.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleK(mainWindow):
		if mainWindow.k != mainWindow.yes:
			mainWindow.k = mainWindow.yes
			mainWindow.K.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.k = mainWindow.no
			mainWindow.K.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleL(mainWindow):
		if mainWindow.l != mainWindow.yes:
			mainWindow.l = mainWindow.yes
			mainWindow.L.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.l = mainWindow.no
			mainWindow.L.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleM(mainWindow):
		if mainWindow.m != mainWindow.yes:
			mainWindow.m = mainWindow.yes
			mainWindow.M.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.m = mainWindow.no
			mainWindow.M.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleN(mainWindow):
		if mainWindow.n != mainWindow.yes:
			mainWindow.n = mainWindow.yes
			mainWindow.N.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.n = mainWindow.no
			mainWindow.N.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleO(mainWindow):
		if mainWindow.o != mainWindow.yes:
			mainWindow.o = mainWindow.yes
			mainWindow.O.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.o = mainWindow.no
			mainWindow.O.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleP(mainWindow):
		if mainWindow.p != mainWindow.yes:
			mainWindow.p = mainWindow.yes
			mainWindow.P.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.p = mainWindow.no
			mainWindow.P.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleQ(mainWindow):
		if mainWindow.q != mainWindow.yes:
			mainWindow.q = mainWindow.yes
			mainWindow.Q.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.q = mainWindow.no
			mainWindow.Q.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleR(mainWindow):
		if mainWindow.r != mainWindow.yes:
			mainWindow.r = mainWindow.yes
			mainWindow.R.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.r = mainWindow.no
			mainWindow.R.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleS(mainWindow):
		if mainWindow.s != mainWindow.yes:
			mainWindow.s = mainWindow.yes
			mainWindow.S.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.s = mainWindow.no
			mainWindow.S.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleT(mainWindow):
		if mainWindow.t != mainWindow.yes:
			mainWindow.t = mainWindow.yes
			mainWindow.T.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.t = mainWindow.no
			mainWindow.T.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleU(mainWindow):
		if mainWindow.u != mainWindow.yes:
			mainWindow.u = mainWindow.yes
			mainWindow.U.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.u = mainWindow.no
			mainWindow.U.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleV(mainWindow):
		if mainWindow.v != mainWindow.yes:
			mainWindow.v = mainWindow.yes
			mainWindow.V.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.v = mainWindow.no
			mainWindow.V.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleW(mainWindow):
		if mainWindow.w != mainWindow.yes:
			mainWindow.w = mainWindow.yes
			mainWindow.W.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.w = mainWindow.no
			mainWindow.W.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleX(mainWindow):
		if mainWindow.x != mainWindow.yes:
			mainWindow.x = mainWindow.yes
			mainWindow.X.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.x = mainWindow.no
			mainWindow.X.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleY(mainWindow):
		if mainWindow.y != mainWindow.yes:
			mainWindow.y = mainWindow.yes
			mainWindow.Y.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.y = mainWindow.no
			mainWindow.Y.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleZ(mainWindow):
		if mainWindow.z != mainWindow.yes:
			mainWindow.z = mainWindow.yes
			mainWindow.Z.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.z = mainWindow.no
			mainWindow.Z.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE1(mainWindow):
		if mainWindow.e1 != mainWindow.yes:
			mainWindow.e1 = mainWindow.yes
			mainWindow.E1.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e1 = mainWindow.no
			mainWindow.E1.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE2(mainWindow):
		if mainWindow.e2 != mainWindow.yes:
			mainWindow.e2 = mainWindow.yes
			mainWindow.E2.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e2 = mainWindow.no
			mainWindow.E2.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE3(mainWindow):
		if mainWindow.e3 != mainWindow.yes:
			mainWindow.e3 = mainWindow.yes
			mainWindow.E3.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e3 = mainWindow.no
			mainWindow.E3.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE4(mainWindow):
		if mainWindow.e4 != mainWindow.yes:
			mainWindow.e4 = mainWindow.yes
			mainWindow.E4.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e4 = mainWindow.no
			mainWindow.E4.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE5(mainWindow):
		if mainWindow.e5 != mainWindow.yes:
			mainWindow.e5 = mainWindow.yes
			mainWindow.E5.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e5 = mainWindow.no
			mainWindow.E5.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
	def toggleE6(mainWindow):
		if mainWindow.e6 != mainWindow.yes:
			mainWindow.e6 = mainWindow.yes
			mainWindow.E6.config(relief=SUNKEN,bg='grey')
			RHv2.output(mainWindow)
		else:
			mainWindow.e6 = mainWindow.no
			mainWindow.E6.config(relief=RAISED,bg=RHv2.orig_color)
			RHv2.output(mainWindow)
	
if	__name__ ==	"__main__":
	root = tk.Tk()
	RHv2(root).pack(fill="both", expand=True)
	root.title("Recipe Helper v2")
	#root.geometry("512x256")
	root.mainloop()

