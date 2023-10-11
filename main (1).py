class player:
def play(self) :
Print("The player is playing cricket. ") 
class Batsman(player) :
def play(self) :
Print(" The  batsman is batting. ") 
class Bowler (player) :
def play(self) :
Print(" The bowler is bowling. ") 
batsman=Batsman() 
bowler=Bowler() 
batsman.play() 
bowler.play()