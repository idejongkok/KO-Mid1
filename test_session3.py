def tambah2an(x,y):
    z = x+y
    return z

def kurang2an(x,y):
    z = x-y
    return z

def result(x,y):
    tambah2an(x,y)
    kurang2an(x,y)
    
# result('a','2')


def test_tambah():
    hasil= tambah2an(2,3)
    assert hasil == 5
    
def test_tambah2():
    hasil= tambah2an(5,3)
    assert hasil == 5
    