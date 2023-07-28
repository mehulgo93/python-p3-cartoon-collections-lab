def roll_call_dwarves(names):
    for index, name in enumerate(names, start= 1):
        print (f"{index}. {name}")
    

def summon_captain_planet(calls):
    captain_list = []
    for call in calls:
        message = f"{call}".capitalize() + "!"
        captain_list.append(message)
    return captain_list

def long_planeteer_calls(calls):
     for call in calls:
         if len(call) > 4:
             return True
     return False


def find_the_cheese(items):
    cheese_list = ["cheddar" , "gouda", "camembert"]

    for item in items:
        if item in cheese_list:
            return item
        
    return None



