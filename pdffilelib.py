import hashlib
import rsa

def save_pdf_file(directory, data, pub_key = None):
    """save pdf data to the store.

    parameters:
    directory: system path of the datastore
    data: binary pdf data for the file
    key: public encryption key to encode the file with"""    
    hashhex = hashlib.sha256(data).hexdigest()
    fname = directory + '/' + hashhex
    if pub_key is not None:
        data = rsa.encrypt(data, pub_key)
        fname = fname + '-' + str(pub_key.n) + '-' + str(pub_key.e)
    fname = fname + '.pdf'
    f = open(fname, 'wb')
    f.write(data)
    f.close()
    return hashhex
    
def load_pdf_file(directory, hashhex, priv_key = None):
    """load binary pdf data from the store

    parameters:
    directory: system path of the datastore
    hashex: a sha256 hash of the unencrypted file encoded as a hex string
    priv_key: the decryption key (if the file is encrypted)
    """
    fname = directory + '/' + hashhex
    if priv_key is not None:
        fname = fname + '-' + str(priv_key.n) + '-' + str(priv_key.e)
    fname = fname + '.pdf'
    f = open(fname, 'rb')
    data = f.read()
    if priv_key is not None:
        data = rsa.decrypt(data, priv_key)
    return data
    
        
