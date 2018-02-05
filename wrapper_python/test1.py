import sys

def stringify_xy(x,y):
    return x+y

if __name__=="__main__":
    print(str(stringify_xy(sys.argv[1], sys.argv[2])))
