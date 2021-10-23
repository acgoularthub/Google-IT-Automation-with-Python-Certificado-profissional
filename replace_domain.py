#the objective of this function is to rename the domain in a list of e-mail
#only if the domain was not modified yet.

def reolace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email