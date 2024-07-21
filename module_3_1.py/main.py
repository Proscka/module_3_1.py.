calls=0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string_info = string
    print(len(string_info))
    count_calls()
    return string,string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    new_list=[]
    for i in list_to_search:
        new_list.append(i.lower())
    return string in new_list

print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban",["ban","BaNaN","urBAN"]))#Urban~urBAN
print(is_contains("cycle",["recycle","cyclic"]))#No matches
print(calls)


