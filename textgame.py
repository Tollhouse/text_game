import random
import time

namelist = ['Jack MeHoff','Richard Long','Wex MaDick','Butt Stuff','Doktor Seks','Tess Tickals','Girth Worm Jim','Yuri Nator']

#Everones stat blocks are random and persistant add in level adjustment for harder fights later on
#TODO should probably limit health boosting as of right now it is unlimited
class monster():
    def __init__(self):
        self.health = random.randrange(15,25)
        self.mana = random.randrange(10,15)
        self.name = random.choice(namelist)
        namelist.remove(self.name)
        self.init_health = self.health
    def Heal(self):
        heals = random.randrange(1,5)
        drain = random.randrange(1,5)
        print(self.name + ' heals for ' + str(heals) + ' HP.')
        print('Costing ' + self.name + ' ' + str(drain) + ' mana.')
        self.health += heals
        self.mana -= drain
    def Regen(self):
        recharge = random.randrange(1,5)
        print(self.name + ' takes a second to take a deep breath recharging ' + str(recharge) + ' mana.')
        self.mana += recharge
    def Attacked(self,target):
        damage = random.randrange(2,10)
        print(target + ' attacks ' + self.name + ' for ' + str(damage) + ' damage!')
        self.health -= damage

#Sorts through the choices and returns updated stats
def choice(player,enemy):
    selected = input()
    enemyoption = random.randint(1,3)
    if int(selected) == 1:
        enemy.Attacked(player.name)
    if int(selected) == 2:
        player.Heal()
    if int(selected) == 3:
        player.Regen()
    if enemyoption == 1:
        player.Attacked(enemy.name)
    if enemyoption == 2:
        enemy.Heal()
    if enemyoption == 3:
        enemy.Regen()
    return player,enemy

#Input loop to let player interact with enemy
def gameloop(player,enemy):
    while (player.health > 0 and enemy.health > 0) and (player.mana > 0 and enemy.mana > 0):
        print(player.name + ' Health: ' + str(player.health) + '    ' + player.name +' Mana: ' + str(player.mana) + '   ' + enemy.name + ' Health: ' + str(enemy.health) + '  ' + enemy.name + ' Mana: ' + str(enemy.mana))
        print('Attack-1 | Heal-2 | Regen-3')
        player,enemy = choice(player,enemy)
    if player.health <= 0:
        print('You got your ass beat haha.')
    if player.mana <= 0:
        print('You passed out you goober.')
    if enemy.health <= 0:
        print('Nice work you beat ' + enemy.name + '\'s ass way to go.')
    if enemy.mana <= 0:
        print(enemy.name + ' passed out like a doofus. Steal his shit and piss in his boots.')
    return player

def fightone(player):
    enemy = monster()
    print('Welcome to the adventure of your lifetime ' + player.name + ".")
    print('You encounter ' + enemy.name + ' on your way to town. Kick his ass!')
    return gameloop(player,enemy)

def fighttwo(player):
    enemy = monster()
    player.health = player.init_health
    print('Great job, you finally make it into town for some rest.')
    print('Unfortunate for you though ' + enemy.name + ' blocks your path in the street.')
    print('Seems like someone is in for a beat down')
    return gameloop(player,enemy)

#Just keeps making fights till its over
def main():
    player = monster()
    player = fightone(player)
    if player.health <= 0 or player.mana <= 0:
        return
    player = fighttwo(player)
    if player.health <= 0 or player.mana <= 0:
        return

main()