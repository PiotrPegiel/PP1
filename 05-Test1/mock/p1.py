def f(card_number):
    string_in_list = list(card_number)
    for i in range(2,len(card_number)-4):
        string_in_list[i]="*"
    card_number = "".join(string_in_list)
    return card_number