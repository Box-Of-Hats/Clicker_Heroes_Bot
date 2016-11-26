import pyautogui, time
from tkinter import *
import subprocess
import threading
import win32api as wapi

class Fish(): #Non Functional
	def __init__(self,meme="dank"):
		self.meme = meme

	def find(self):
		fishPresent = pyautogui.locateOnScreen("fish.png",region=(0,0,767,600))
		print("region 1",fishPresent)
		if not fishPresent:
			fishPresent = pyautogui.locateOnScreen("fish.png",region=(767,0,767,600))
			print("region2",fishPresent)
		return fishPresent

	def click(self):
		pyautogui.click(self.find())

class Attack():
	def __init__(self,times,delay,loops=1,loc=(1000,500)):
		self.times = times
		self.delay = delay
		self.loc = loc
		self.loops = loops


	def execute(self):
		pyautogui.click(self.loc,clicks=self.times)
		time.sleep(self.delay)

	def loopexecute(self):
		print("Attacking!")
		loopsleft = self.loops
		while loopsleft != 0:
			self.execute()
			loopsleft = loopsleft - 1

class Powerup():
	def __init__(self,ID,icon,region=(0,0,800,800)):
		self.id = ID
		self.icon = icon
		self.region = region

	def isReady(self):
		ready = pyautogui.locateOnScreen(self.icon,region=self.region)
		if ready:
			print("Powerup {}:".format(self.id),"Ready!")
			return True
		else:
			print("Powerup {}:".format(self.id),"Charging")
			return False
	def execute(self):
		if self.isReady():
			pyautogui.typewrite(str(self.id))

class Combo():
	def __init__(self,powerups):
		self.powerups = powerups

	def execute(self):
		if self.check():
			print("Executing Combo",self.powerups)
			for powerup in self.powerups:
				powerup.execute()

	def check(self):
		checkList = []
		for powerup in self.powerups:
			checkList.append(powerup.isReady())
		if False in checkList:
			return False
		else: 
			return True


#Class for the Level Up panel:
class LevelUp():
	def __init__(self,clicks=1):
		self.clicks = clicks

	def goToTop(self): #Scrolls the upgrade bar to the top.
		cidLoc = pyautogui.locateOnScreen("heroes\\cid.png",region=(279,220,250,28))
		if cidLoc != (279,220,250,28):
			pyautogui.click(660,252)
			cidLoc = pyautogui.locateOnScreen("heroes\\cid.png",region=(279,220,250,28))
		pyautogui.moveTo(165,280)

	def goToBottom(self):
		bottom = pyautogui.locateOnScreen("buyavailable.png",region=(273,606,216,53))
		if bottom != (273,606,216,53):
			pyautogui.click(660,690)

	def buyAvailable(self):
		self.goToBottom()
		#self.goToTop()
		time.sleep(0.2)
		#thisBut = pyautogui.locateOnScreen("buyAvailable.png")
		pyautogui.click(460,640)

	def buyBottom(self,bottom=True):
		self.goToBottom()
		time.sleep(0.1)
		counter = self.clicks
		while  counter > 0:
			if bottom == True:
				pyautogui.click(166,420)
			else:
				pyautogui.click(146,296)
			counter = counter - 1 





def checkAutoMove():
	stoppedProgressing = pyautogui.locateOnScreen("automove.png",region=(1275,288,18,20))
	if stoppedProgressing:
		print("Automove: Off")
		return False
	else:
		print("Automove: On")
		return True

def toggleAutoMove():
	pyautogui.click(1275,288)

def checkWindowOpen(change=True):

	def changeToWindow():
		icon = pyautogui.locateOnScreen("pinnedbutton.png")
		pyautogui.click(icon)
		

	windowOpen = pyautogui.locateOnScreen("gameicon.png",region=(2,3,15,15))
	if windowOpen:
		return True
	else:
		if change == True:
			changeToWindow()
			return True
		else:
			return False

class Hero():
	def __init__(self,name):
		self.name = name
		self.filename = "heroes\\" + str(name.lower()) + ".png"
	def find(self):
		location = pyautogui.locateOnScreen(self.filename)
		#pyautogui.click(659,232)
		print("{}: {}".format(self.name,location))
 


def sweepingUpgrade(stepSize=40):
	posY = 220
	pyautogui.click(220,posY)
	pyautogui.keyDown('ctrl')
	while (posY+stepSize) <= 605:
		pyautogui.moveRel(0,stepSize)
		pyautogui.click()
		posY += stepSize
	pyautogui.keyUp('ctrl')

def scrollDown(times=1,clickTimes=19):
	while times > 0:
		clickCount = clickTimes
		while clickCount > 0:
			pyautogui.click(660,710)
			clickCount -= 1
		times -=1


def upgradeEverything():
	callAnus = LevelUp(1)

	sweepingUpgrade()
	callAnus.buyAvailable()
	callAnus.goToTop()
	scrollDown()
	sweepingUpgrade()
	callAnus.buyAvailable()


def postAscend():
	time.sleep(1)
	if not checkAutoMove():
			toggleAutoMove()
	pyautogui.click(1000,500)
	countTo = 15
	counter = 0
	clickCount = 0
	call = LevelUp(1)
	positions = [(165,270),(165,385),(165,500),(165,650)]
	for position in positions:
		counter = 0
		while counter != countTo:
			clickCount = 0
			while clickCount < clickCountTo:
				pyautogui.click(1000,500)
				clickCount +=1
			
			if counter % 5 == 0:
				pyautogui.keyDown('ctrl')
				pyautogui.click(position)
				call.buyAvailable()
				call.goToTop()
				pyautogui.keyUp('ctrl')
			counter +=1
			clickCount = 0
		time.sleep(1)
		if not checkAutoMove():
			toggleAutoMove()

	
	call.buyAvailable()
	time.sleep(1)
	if not checkAutoMove():
			toggleAutoMove()



# Initialising Objects

#Powerups
Clickstorm  	= Powerup(1,"clickstorm.png",(712,191,27,39))
Powersurge 		= Powerup(2,"powersurge.png",(706,249,40,39))
Luckystrikes 	= Powerup(3,"luckystrikes.png",(704,302,44,46))
Metaldetector	= Powerup(4,"metaldetector.png",(703,360,45,45))
Goldenclicks 	= Powerup(5,"goldenclicks.png",(704, 419, 44, 42)) 
Darkritual 		= Powerup(6,"deathritual.png",(705,476,43,41))
Superclicks 	= Powerup(7,"superclicks.png",(704,533,44,43))
Energise 		= Powerup(8,"energise.png",(704,589,44,44))
Reload 			= Powerup(9,"reload.png",(704,647,43,42))

allPowerups 	= [Clickstorm,Powersurge,Luckystrikes,Metaldetector,Goldenclicks,
					Darkritual,Superclicks,Energise,Reload]

#Combos
All 		= Combo(allPowerups)
Boss 		= Combo([Clickstorm,Powersurge,Luckystrikes,Superclicks])
Ritual 		= Combo([Energise,Darkritual,Reload])
Money 		= Combo([Metaldetector,Goldenclicks])
BaseGrind  	= Combo([Clickstorm,Powersurge])
MediumGrind = Combo([Clickstorm,Powersurge,Luckystrikes])

#Attacks
Grind 			= Attack(3,0.05,loops=10)
InfiniteGrind 	= Attack(3,0.05,loops=-1)



#Fish (Not working)
Fisch = Fish()

#LevelUp
Lvl = LevelUp(2)


#Heroes
Amenhotep = Hero("Amenhotep")
Cid 	  = Hero("Cid")
Amenhotep2= Hero("Amenhotep2")
Amenhotep3= Hero("Amenhotep3")

allHeroes = [Amenhotep,Cid,Amenhotep2,Amenhotep3]

def justMomentum():
	pyautogui.click(1000,460)
	counter = 0
	while True:
		x,y = pyautogui.position()
		if x == 0 and y ==0:
			break
		if x >= 765:
			if x <=  1260:
				if y >= 200:
					if y <= 600:
						pyautogui.click(clicks=2)
						time.sleep(0.05)
		
		if counter % 100 == 0 :
			time.sleep(1)
		counter += 1


def wiggleMouse(times=40,click=True):
	if click:
		while times > 0 :
			pyautogui.click(900,500)
			pyautogui.click(920,500)
			pyautogui.click(940,500)
			pyautogui.click(960,500)
			pyautogui.click(1000,500)
			pyautogui.click(1040,500)
			pyautogui.click(1080,500)
			pyautogui.click(1120,500)
			times -=1
	else:
		while times > 0 :
			pyautogui.moveTo(900,500)
			pyautogui.moveTo(920,500)
			pyautogui.moveTo(940,500)
			pyautogui.moveTo(960,500)
			pyautogui.moveTo(1000,500)
			pyautogui.moveTo(1040,500)
			pyautogui.moveTo(1080,500)
			pyautogui.moveTo(1120,500)
			times -=1

def regularGrind(upgrades=True,scrolldownClicks=8):

	levelObj = LevelUp(1)
	loopNo = 0
	levelupNo = -1
	wiggleMouse(times=5)
	while True:
		if wapi.GetAsyncKeyState(ord('C')):
			pyautogui.moveTo(0,0)
		if loopNo % 30 == 0:
			clickFishLocations()

		#Money/Ritual Check
		if loopNo % 100 == 0:
			Ritual.execute()
			if Money.check():
				Money.execute()
				wiggleMouse()
		Grind.execute()


		#Attack Type Check
		if loopNo % 5 ==0:
			if Boss.check():
				#time.sleep(2)
				if not checkAutoMove():
					pyautogui.typewrite('a')
				Boss.execute()
				if upgrades: sweepingUpgrade()
				if not Darkritual.isReady():
					Energise.execute()
					Reload.execute()

				wiggleMouse(click=False)
				if upgrades: sweepingUpgrade()
				wiggleMouse(click=False)
			elif MediumGrind.check():
				if not checkAutoMove():
					pyautogui.typewrite('a')
				MediumGrind.execute()
				if upgrades: sweepingUpgrade()
				wiggleMouse(click=False)
				if upgrades: sweepingUpgrade()
				wiggleMouse(click=False)
				
			else:
				if BaseGrind.check():
					BaseGrind.execute()
					if upgrades: sweepingUpgrade()
					wiggleMouse(click=False)
					if upgrades: sweepingUpgrade()
					wiggleMouse(click=False)
					

			Grind.execute()
		if loopNo % 10 == 0:
			if not upgrades:
					#BUYS FROSTLEAF:
					pyautogui.keyDown('ctrl')
					#Top Pos
					#pyautogui.click(170,280)
					#Bottom Pos
					pyautogui.click(165,655)
					pyautogui.keyUp('ctrl')
				

		#levelUps
		if upgrades:
			if loopNo % 30 == 0:
				levelupNo += 1
				
				if (levelupNo % 9 ==0):
					sweepingUpgrade()
					levelObj.buyAvailable()
					levelObj.goToTop()
				else:
					sweepingUpgrade()
					bottom = False
					bottom = pyautogui.locateOnScreen("buyavailable.png",region=(273,606,216,53))
	
					if not bottom:
						scrollDown(clickTimes=scrolldownClicks)
					else:
						pyautogui.keyDown('ctrl')
						pyautogui.click(160,420)
						pyautogui.keyUp('ctrl')
						levelObj.buyAvailable()
						levelObj.goToTop()
		Grind.execute()
		loopNo+=1

def openGame():
	filePath = "C:\Program Files (x86)\Steam\SteamApps\common\Clicker Heroes\Clicker Heroes.exe"
	this = threading.Thread(target=subprocess.call,args=([filePath]) )
	this.start()
	time.sleep(3)
	pyautogui.click(650,260)
	time.sleep(1)
	pyautogui.keyDown('winleft')
	pyautogui.keyDown('up')
	pyautogui.keyUp('winleft')
	pyautogui.keyUp('up')
	time.sleep(1)
	pyautogui.click(680,320)
	#time.sleep(1.5)
	#pyautogui.click()

def raid(counterIn=500):
	counter = counterIn
	pyautogui.click(1000,500)
	while  counter != 0:
		pyautogui.click(clicks=3)
		time.sleep(0.05)
		counter -=1

def speedyAscend(timesToAscend=22):
	def moveForeword(times):
		while times != 0:
			pyautogui.click(1130,75)
			times -= 1
	unit = LevelUp()
	while timesToAscend != 0:
		#unit.goToBottom()
		unit.goToTop()
		unit.goToBottom()
		time.sleep(0.1)
		unit.buyBottom()
		Grind.execute()
		Grind.execute()
		Grind.execute()
		Grind.execute()
		time.sleep(1)
		moveForeword(3)
		timesToAscend -=1
	pyautogui.keyDown('a')
	pyautogui.keyUp('a')
	regularGrind(1,scrolldownClicks=6)	

def clickFishLocations():
	locations = [
			(1010,555),
			(871,465),
			(1153,485),
			(885,412),
			(633,528),
			(1213,480),
	]
	for location in locations:
		pyautogui.click(location)


def guiGo():
	def doGrind(grindUpgrade):
		pyautogui.locateAllOnScreen('fish.png')
		regularGrind(grindUpgrade)
		
	root = Tk()
	fishFound = IntVar()
	fishFound.set(0)
	buySweep = IntVar()
	upgradeToggle = Checkbutton(root,variable=buySweep,text="Upgrades",state='active')
	upgradeToggle.grid(row=1,column=1)
	Button(text="Start",command=lambda:doGrind(buySweep.get())).grid(row=0,column=1)
	Button(text="Open",command=lambda:openGame()).grid(row=0,column=2)
	Button(text="Ascend",command=lambda:speedyAscend()).grid(row=0,column=3)
	Button(text="Raid",command=lambda:raid(counterIn=-1)).grid(row=1,column=2)
	root.geometry("{}x{}+{}+{}".format(200,50,1157,645))
	root.wm_attributes('-topmost',int(True))
	root.mainloop()

def main():
	guiGo()



if __name__ == "__main__":
	main()