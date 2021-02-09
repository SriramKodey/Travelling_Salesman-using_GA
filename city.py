class city:
    ''' City class, with x and y points'''
    def __init__(self, num):
        y = int(num/101)
        x = int(num%101)

        self.x = x
        self.y = y

if __name__ == "__main__":
    hyd = city(10200)
    print(hyd.x, hyd.y)