def is_valid_trick(trick_name):
    splittedname=trick_name.split()
    firstword=["Misty","Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"]
    secword=["Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow"]
    for i in range(0,len(splittedname)):
        if splittedname[i] in firstword and splittedname[i+1] in secword:
            return True
        else:
            return False
print(is_valid_trick("Misty Sharma"))
