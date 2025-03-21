def get_initials(name):
    name_parts = name.split()
    
    initials = [part[0].upper() + '.' for part in name_parts]
    
    return ' '.join(initials)


full_name = input("Enter your full name (First Middle Last): ")


print(get_initials(full_name))