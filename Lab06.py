#part2
class Player:
    def __init__(self,firstname,lastname,team=None):

        self.first_name=firstname
        self.last_name=lastname
        self.scores=[1,2,3]
        self.team=team
    def add_score(self,score):
        self.scores.append(score)
        print self.scores
    def total_score(self):
        print sum(self.scores)
    def average_score(self):
        print sum(self.scores)/len(self.scores)

myplayer=Player('Michael','Essien','Chelsea')
myplayer.add_score(6)
myplayer.total_score()
myplayer.average_score()

Fernando_Torres=Player('Fernando','Torres','Liverpool')
Fernando_Torres.add_score(0)
Fernando_Torres.add_score(0)
Fernando_Torres.add_score(1)
Fernando_Torres.add_score(0)
Fernando_Torres.add_score(1)
Fernando_Torres.average_score()
        
#part3
class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.league=league
        self.manager=manager_name
        self.Portugal_players=['Nanny','Maniche']
        self.Spain_players=['Xavi','Puyol','Fabregas','Iniesta']
        self.points=points
    def add_Portugal_player(self,player):
        self.Portugal_players.append(player)
        print self.Portugal_players
    def add_Spain_player(self,player):
        self.Spain_players.append(player)
        print self.Spain_players
    def __str__(self):
        return ("The name of the team is " +
                self.name + "\n" + "The manager is "+
                self.manager + "\n" + "This team belongs to " +
                self.league + "Championship\n" +
                "It currently has " + self.points + " points\n")
        

portugal=Team('Portugal','Euro','me','6')
portugal.add_Portugal_player('Ronaldo')
spain=Team('Spain','Euro','my_dad','9')
spain.add_Spain_player('Torres')
print spain
#When an object is created, the constructor is called and this passes the
#parameters of the constructor into the object.
#Print spain outputs the address of the object spain.

class Match:
    import datetime
    def __init__(self,home_team,away_team,date):
        self.spain_home_scores={'Torres':4,'Fabregas':3,'Iniesta':4}
        self.spain_away_scores={'Torres':1,'Fabregas':0,'Iniesta':2}
        self.portugal_home_score={'Ronaldo':7,'Nanny':3,'Maniche':2}
        self.portugal_away_score={'Ronaldo':4,'Nanny':1,'Maniche':0}
        self.s_home_scores=[4,3,4]
        self.s1_home_scores=[6,3,4]
        self.s_away_scores=[1,0,2]
        self.p_home_scores=[7,3,2]
        self.p1_home_scores=[5,1,0]
        self.p_away_scores=[4,1,0]
    def s_home_score(self):
        print "Spain's home scores is",sum(self.s_home_scores)
    def s_away_score(self):
        print "Spain's away scores is",sum(self.s_away_scores)
    def p_home_score(self):
        print "Portugal's home scores is",sum(self.p_home_scores)
    def p_away_score(self):
        print "Portugal's away scores is",sum(self.p_away_scores)
    def winner(self):
        if ((self.s_home_scores+self.s_away_scores)>
           (self.p_home_scores+self.p_away_scores)):
            print "Spain is the winner"
        else:
            print "Portugal is the winner"
    def winner1(self):
        if (sum(self.s1_home_scores)>sum(self.p1_home_scores)):
            print "Spain has won"
        else:
            print "Portugal has won"

            
    def add_score(self,player,score):
        print player,"is in Spain"
        print "Spain is home"
        self.spain_home_scores['Torres']=5
        print self.spain_home_scores
        self.portugal_away_score['Ronaldo']=5
        print self.portugal_away_score
        self.spain_home_scores['Torres']=6
        print self.spain_home_scores
    

firstleague=Match('Spain','Portugal','2012/06/12')
secondleague=Match('Portugal','Spain','2012/06/23')
firstleague.s_home_score()
secondleague.s_away_score()
firstleague.p_home_score()
secondleague.p_away_score()
firstleague.winner()

euro_semi_final=Match('Spain','Portugal','2012/06/27')
euro_semi_final.add_score('Torres',4)
euro_semi_final.winner1()








        
        
        
