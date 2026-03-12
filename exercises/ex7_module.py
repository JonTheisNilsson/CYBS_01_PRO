def input_number(_type : type):
    while (True):
        try:
            i = input("Input a number: ")
            out = _type(i)
            return out

        except Exception:
            retry = input("Invalid input. Retry? (y/n): ").lower()
            if retry  == 'y':
                continue
            raise ValueError("No valid value was entered!")

