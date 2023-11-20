def cholesterol(diastoic, systoic, change_meds, coronary_desease, scheduled):
    if diastoic >= 90:
        if change_meds == "false":
            if systoic < 155:
                if scheduled == "true":
                    print("medium increase")
                elif scheduled == "false":
                    print("low increase")
                else:
                    print('Incorrect Input')
            elif systoic >= 155:
                print('high increase')
            else:
                print('Incorrect Input')
        elif change_meds == "true":
            print('high increase')
        else:
            print('Incorrect Input')
    elif 0 < diastoic < 90:
        if systoic < 165:
            if coronary_desease == "true":
                print('medium increase')
            elif coronary_desease == "false":
                print('low increase')
            else:
                print('Incorrect Input')
        elif systoic >= 165:
            print('medium increase')
        else:
            print('Incorrect Input')
    else:
        print('Incorrect Input')

cholesterol(diastoic=-5, systoic=150, scheduled='true', change_meds='false', coronary_desease='true')
