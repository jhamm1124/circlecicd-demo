def Add(a, b):
        return a + b
        
def SayHello():
        assert Add(2,3) == 6
        assert Add(5,5) == 10
        print("Hello CIS 411")

if __name__ == '__main__':
        SayHello()