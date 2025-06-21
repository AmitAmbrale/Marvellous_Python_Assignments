import hashlib

def CheckSum(fname):

    hobj = hashlib.md5()

    fobj = open(fname, 'rb')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    return hobj.hexdigest()