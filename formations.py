List = {
        "formations":[
                {'formation': "formation1", "durée":12},
                {'formation': "formation2", "durée":4},
                {'formation': "formation3", "durée":9},
                {'formation': "formation4", "durée":16},
             ]
        }
for cursus in List["formations"]:
    if cursus["durée"] < 10:
        print ("formation " + cursus['formation'])

    else: print ("cursus " + cursus['formation'])