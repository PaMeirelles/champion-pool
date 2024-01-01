from constants import Elo

def elo_to_str (elo:Elo):
    if elo == Elo.IRON:
        return "iron"
    elif elo == Elo.BRONZE:
        return "bronze"
    elif elo == Elo.SILVER:
        return "silver"
    elif elo == Elo.GOLD:
        return "gold"
    elif elo == Elo.PLATINUM:
        return "platinum"
    elif elo == Elo.EMERALD:
        return "emerald"
    elif elo == Elo.DIAMOND:
        return "diamond"
    elif elo == Elo.MASTER:
        return "master"
    elif elo == Elo.GRANDMASTER:
        return "grandmaster"
    elif elo == Elo.CHALLENGER:
        return "challenger"

def url_formatter(champ1:str, champ2:str, elo:Elo):
    return f"https://u.gg/lol/champions/{champ1}/build?rank={elo_to_str(elo)}&opp={champ2}"

print(url_formatter("pantheon", "ornn", Elo.PLATINUM))