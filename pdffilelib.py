import hashlib
import rsa

def save_pdf_file(directory, data, pub_key = None):
    """save pdf data to the store.

    parameters:
    directory: system path of the datastore
    data: binary pdf data for the file
    key: public encryption key to encode the file with"""    
    datahash = hashlib.sha256(data).hexdigest()
    fname = directory + '/' + datahash
    if pub_key is not None:
        data = rsa.encrypt(data, pub_key)
        fname = fname + '-' + str(pub_key.n) + '-' + str(pub_key.e)
    fname = fname + '.pdf'
    f = open(fname, 'wb')
    f.write(data)
    f.close()
    
