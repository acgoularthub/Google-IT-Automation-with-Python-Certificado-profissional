def new_list(tuple):
    list = []
    for email, name in tuple:
        list.append("{} <{}>".format(name, email))
    return 