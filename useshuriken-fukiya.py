#########  shuriken and fukiya reloader and distance checker by Mourn and Modified by Mark. March 2021

belt = None
fuk = None
shur = None
fukdart = None
if Items.BackpackCount(0x2790,-1) > 0:
    belt = Items.FindByID(0x2790,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Ninja Belt',38)
if Items.BackpackCount(0x27AA,-1) > 0:    
    fuk = Items.FindByID(0x27AA,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Fukiya',38) 
if Items.BackpackCount(0x2806,-1) > 0:    
    fukdart = Items.FindByID(0x2806,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Fukiya Darts in bag',38) 
if Items.BackpackCount(0x27AC,-1) > 0:
    shur = Items.FindByID(0x27AC,-1,Player.Backpack.Serial)
else: 
    Misc.SendMessage('No Shuriken in bag',38) 
    

def uses():
    global belt
    global fuk
    global shur
    if belt is not None and shur is not None:
        beltprops = Items.GetPropStringList(belt)
        for beltprop in beltprops:
            if beltprop.split(' ')[0] == 'uses':
                sUses = beltprop.split(' ')[2]
                Misc.SendMessage(sUses + ' Shuriken in belt',82)
                if int(sUses) == 0:
                    last = Target.GetLast()
                    Misc.WaitForContext(belt, 1500)
                    Misc.ContextReply(belt, 0)
                    Target.WaitForTarget(300,False)
                    Target.TargetExecute(shur)
                    Misc.SendMessage('Loading Shuriken',82)
                    Target.SetLast(last)
    if fuk is not None and fukdart is not None:        
        fukprops = Items.GetPropStringList(fuk)
        for fukprop in fukprops:
            if fukprop.split(' ')[0] == 'uses':
                fUses = fukprop.split(' ')[2]
                Misc.SendMessage(fUses + ' Darks in fukiya',82)    
                if int(fUses) == 0:
                    last = Target.GetLast()
                    Misc.WaitForContext(fuk, 1500)
                    Misc.ContextReply(fuk, 0)
                    Target.WaitForTarget(300,False)
                    Target.TargetExecute(fukdart)
                    Misc.SendMessage('Loading Fukiya',82)
                    Target.SetLast(last)
                
                
def attack():
    
    target = Target.GetLast()
    enemy = Mobiles.FindBySerial(target)
    if enemy == None:
        Player.HeadMessage( 34, "No enemy to fukiya!")
        return
    if Player.DistanceTo(enemy) <= 5 and fuk is not None:
        Items.UseItem(fuk)
        Target.WaitForTarget(300,False)
        Target.TargetExecute(enemy)
    if Player.DistanceTo(enemy) >= 5 and Player.DistanceTo(enemy) <= 10  and belt is not None:
        Items.UseItem(belt)
        Target.WaitForTarget(300,False)
        Target.TargetExecute(enemy)
    
 

    
uses()
attack()
Misc.Pause(10)
