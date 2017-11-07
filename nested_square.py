import matplotlib.pyplot as plt
def square(x, y):
    '''
    Objective: To plot a square
    Input Parameters: x, y - lists of x coordinates and y
    coordinates respectively
    Return Value: None
    '''
    plt.plot(x, y, 'ro--')

def draw_s(size,a=0):
    

    if(size!=a):
        x=[a,size,size,a,a]
        y=[a,a,size,size,a]
        square(x, y)
        draw_s(size-1,a+1)
   


def main():
    '''
    Objective: To plot a square based on user input
    Input Parameter: None
    Return Value: None
    '''
    size=int(input('ENTER LENGTH OF BIGGEST SQUARE'))
    draw_s(size)
    x=[0,size,size,0,0]
    y=[0,0,size,size,0]
    plt.title('Square')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.grid()
    plt.show()
if __name__ == '__main__':
    main()
