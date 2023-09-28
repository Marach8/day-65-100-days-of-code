class character:
  name = 'Player'
  health = 100
  magic_points = 45
  
  def __init__(self, name, health, magic_points):
    self.name = name
    self.health = health
    self.magic_points = magic_points

  def printe(self):
    print(f'''
Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}
    ''')

class player(character):
  
  def __init__(self, lives):
    self.lives = lives

  def printe(self):
    print(f'''
Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nLife: {self.lives}''')

  def is_alive(self):
    if self.lives > 0:
      print(f'{self.name} is alive!')
    else:
      print(f'{self.name} is dead!')


class enemy(character):
  type = 'enemy'
  strength = '79MP'
  
  def __init__(self, type, strength):
    self.type = type
    self.strength = strength

class orc(enemy):
  speed = None

  def __init__(self, name, speed):
    self.name = name
    self.speed = speed

  def printe(self):
    print(f'''
Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}''')

class vampire(enemy):
  tracker = None
  
  def __init__(self, name, tracker):
    self.tracker = tracker
    self.name = name

  def printe(self):
    print(f'''
Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nType: {self.type}\nStrength: {self.strength}\nTracker: {self.tracker}''')


Player = player(200)
Player.printe()
Player.is_alive()

vamp1 = vampire('VampireAA', 'Day')
vamp1.printe()

vamp2 = vampire('VampireBB', 'Night')
vamp2.printe()

orc1 = orc('OrcAA', 560)
orc1.printe()

orc2 = orc('OrcBB', 1000)
orc2.printe()

orc3 = orc('OrcCC', 2000)
orc3.printe()