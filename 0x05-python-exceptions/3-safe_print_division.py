#!/usr/bin/python3
def safe_print_division(a, b):
    ''' function that divides 2 integers and prints the result.'''
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Check if 'result' is defined in the local scope.
        if 'result' in locals():
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")

    return result
