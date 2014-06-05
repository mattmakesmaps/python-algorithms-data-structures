__author__ = 'matt'
__date__ = '6/1/14'

def edit_list(myvals):
    newvals = [value*2 for value in myvals]
    myvals = newvals
    print myvals
    return myvals

if __name__ == '__main__':
    myvals = [1]*3
    print('Pre',myvals)
    edit_list(myvals)
    print('Post',myvals)
