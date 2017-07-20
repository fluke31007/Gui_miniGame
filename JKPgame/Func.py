import random
class Function(object):

	def __init__(self):
		self.turnC =0
		self.HeroHp =10
		self.MonsHp =10
		self.MonsCard = 0
		self.HeroCard =0
	def MonRan(self):
		self.MonsCard = random.randint(0,2)
	def checkCard(self):
		if self.HeroHp >0 and self.MonsHp>0 :
			if self.HeroCard == 0 and self.MonsCard == 1 or self.HeroCard==1 and self.MonsCard ==2 or self.HeroCard==2 and self.MonsCard==0:
				self.MonsHp = self.MonsHp-1
				self.turnC +=1
			elif self.MonsCard ==0 and self.HeroCard==1 or self.MonsCard==1 and self.HeroCard ==2 or self.MonsCard==2 and self.HeroCard==0:
				self.HeroHp= self.HeroHp-1
				self.turnC +=1

			else:
				self.turnC +=1
	def reset(self):
		self.turnC =0
		self.HeroHp =10
		self.MonsHp =10