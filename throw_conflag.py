potID = 0x0F06
def potThrowConflag1():
    if Items.BackpackCount(potID, -1) == 0:
        Player.HeadMessage(30, 'Out of Conflag pots')
        Misc.Pause(10)
    else:
        Journal.Clear()
        enemy = Mobiles.FindBySerial(Target.GetLast())
        Misc.Pause(10)
        if enemy != None:
            if Player.DistanceTo(enemy) <= 10 and enemy.Paralized:
                Items.UseItemByID(potID)
                Misc.Pause(100)
                if Journal.Search("You cannot use that"):
                    Misc.Pause(10)
                    return
                Target.WaitForTarget(200)
                Player.HeadMessage(30, 'CONFLAG ENEMY')
                Target.TargetExecute(enemy)
                Misc.Pause(600)

def potThrowConflag():
    if Items.BackpackCount(potID, -1) == 0:
        Player.HeadMessage(30, 'Out of Conflag pots')
        Misc.Pause(10)
    else:
        Items.UseItemByID(potID)
        Target.WaitForTarget(200,True)
        if Journal.Search("You cannot use that"):
            Misc.Pause(10)
            return
        Target.Last()
                        

potThrowConflag1()
Misc.Pause(10)
