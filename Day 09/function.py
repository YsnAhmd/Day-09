#Defining function
def hello():
    print('Hi,Kese ho?')
    print('AAi bala asi')



hello()
#Function with one perameter
def Sayhello(n):
    print('Hi,' + n + ' Kese ho?')
    print('AAi bala asi')

Sayhello('Tonoya')
#Function with two perameter
def Sayhello2(n,m):
    print('Hi,' + n + " "+m + ' Kese ho?')
    """Formating perameter"""
    print('%s %s' %(n,m))
    print('{0} {1}'.format(n,m))
    print('{} {}'.format(n,m))
    print('AAi bala asi')

Sayhello2('Tonoya','Rahman')

#Python Arbitrary Arguments
def greet(*names):
    '''This function greets all the person in the names tuple.'''
    #names in a tuple with arguments
    for name in names:
        print("Hello",name)

greet('Ami','Tarpor o ami','Abong ami')
