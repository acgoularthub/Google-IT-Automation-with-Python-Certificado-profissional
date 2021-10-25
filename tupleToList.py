#create a list that receives a tuple with the email and name pf people and
#return a list with the format "name <email>"

def new_list(tuple):
    list = []
    for email, name in tuple:
        list.append("{} <{}>".format(name, email))
    return list