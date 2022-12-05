def f(map,av):
    if sum(map["subject"]["grades"])/len(map["subject"]["grades"]) > av:
        return True
    else:
        return False