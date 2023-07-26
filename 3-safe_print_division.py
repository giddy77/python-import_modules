
def safe_print_division(a, b):
    result = None
     
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result))

    return result
