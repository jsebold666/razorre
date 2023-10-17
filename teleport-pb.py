Spells.Cast('Teleport')
Target.WaitForTarget(3000)
last = Target.GetLast()
Target.TargetExecuteRelative(Target.GetLast(),8)
Target.SetLast(last)
if not Player.HasSpecial:
    Player.WeaponSecondarySA()