'''
savedvalue(value):
    if value is sauce:
        return sauce

filesave(score, tps, scorerate, tabasco, bbq, ketchup, mayo, soy):
    update file text

'''
inputvalue = ["tacos", "tps", "scorerate", "tabasco", "bbq", "ketchup", "mayo", "soy", "tcost", "bcost", "kcost", "mcost", "scost", "timer"]

# function to get the saved values
def savedvalue(value):
    global saved_file
    saved_file = open("savefile.txt", "r")
    all_values = []
    for line in saved_file:
        all_values.append(line)
    if value == "tps":
        return float(all_values[inputvalue.index(value)])   
    elif value == "timer":
        return all_values[inputvalue.index(value)] == "True\n"
    elif value != "tps" and value != "timer":
        return int(all_values[inputvalue.index(value)])
    saved_file.close()

# saving the values
def filesave(value_list):
    global saved_file 
    saved_file = open("savefile.txt", "w")
    for i in range(len(value_list)):
        print(value_list[i])
        saved_file.write(str(value_list[i]) + "\n")
    saved_file.close()
