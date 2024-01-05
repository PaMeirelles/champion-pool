from constants import Elo, Role


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
    

def role_to_str (role:Role):
    if role == Role.TOP:
        return "top-lane"
    if role == Role.JUNGLE:
        return "jungle"
    if role == Role.MID:
        return "mid-lane"
    if role == Role.ADC:
        return "adc"
    if role == Role.SUPPORT:
        return "support"

def winrate_url_formatter(champ1:str, champ2:str, elo:Elo):
    return f"https://u.gg/lol/champions/{champ1}/build?rank={elo_to_str(elo)}&opp={champ2}"


def tierlist_formatter(role:Role, elo:Elo):
    return f"https://u.gg/lol/{role_to_str(role)}-tier-list?rank={elo_to_str(elo)}"


