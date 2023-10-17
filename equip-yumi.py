bow = 0x45FD9956
if Player.CheckLayer('LeftHand') and bow != Player.GetItemOnLayer('LeftHand').Serial: 
    Spells.Cast('Weaken')
    Player.EquipItem(bow)
    Misc.Pause(10)

if not Player.CheckLayer('LeftHand'):
    Player.EquipItem(bow)
    Misc.Pause(10)