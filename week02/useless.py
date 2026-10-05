#functions

def validate_int(input_str: str) -> bool:
    try:
        int(input_str)
        return True
    except ValueError:
        return False



def validate_float(input_str: str) -> bool:
    try:
        float(input_str)
        return True
    except ValueError:
        return False

#input
try:
    subscription = float(input("Enter price of subscription: "))
    ticket = float(input("Enter price of single ticket: "))
    visits = int(input("Enter number of visits: "))
    total_ticket = ticket * visits

    if total_ticket == subscription or total_ticket < subscription:
        print("Single tickets: €" + str(total_ticket))
        print("Monthly subscription: €" + str(subscription))
        print("Advice: Buy single tickets")
    elif total_ticket > subscription:
        print("Single tickets: €" + str(total_ticket))
        print("Monthly subscription: €" + str(subscription))
        print("Advice: Buy a subscription")
        print("You save " + str(total_ticket - subscription))
    else:
        pass
except ValueError:
    print("Invalid input")