def test():
    try:
        x = 5
        return x
    finally:
        print("finally")
        x = 10
        
print(test())
    
    