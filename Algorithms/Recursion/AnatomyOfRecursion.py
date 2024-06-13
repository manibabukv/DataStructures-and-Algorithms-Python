
counter = 0

def inception():
    print(counter)
    if counter > 3:
        return "done!"

    counter += 1
    return inception()

inception()