import sqlite3

def tag_pdf(conn, hashhex, tag):
    if tag not in get_pdf_annotations(conn, hashhex):
        c = conn.cursor()
        t =  (hashhex, tag)
        c.execute('INSERT INTO annotations VALUES (NULL,"mypdfdb:tags",NULL,?,?,NULL)', t)
        conn.commit()
    
def declare_equivalent_pdfs(conn, hashhex1, hashhex2):
    if hashhex2 not in get_equivalent_pdfs(conn, hashhex1):
        c = conn.cursor()
        t = (hashhex1, hashhex2)
        c.execute('INSERT INTO annotations VALUES (NULL,NULL,"mypdfdb",?,?,"equivalent")', t)
        t = (hashhex2, hashhex1)
        c.execute('INSERT INTO annotations VALUES (NULL,NULL,"mypdfdb",?,?,"equivalent")', t)
        conn.commit()

def declare_derived_pdf(conn, hashhex1, hashhex2):
    if hashhex2 not in get_direct_component_pdfs(conn, hashhex1):
        c = conn.cursor()
        t = (hashhex1, hashhex2)
        c.execute('INSERT INTO annotations VALUES (NULL,NULL,"mypdfdb",?,?,"derived-from")', t)
        conn.commit()
    
def untag_pdf(conn, hashhex, tag):
    c = conn.cursor()
    t =  (hashhex, tag)
    c.execute('DELETE FROM annotations WHERE domain2 = "mypdfdb:tags" AND object1 = ? AND object2 = ?)', t)
    conn.commit()

def get_pdf_annotations(conn, hashhex):
    c = conn.cursor()
    t = (hashhex,)
    c.execute('SELECT object2 FROM annotations WHERE domain2 = "mypdfdb:tags" and object1 = ?', t)
    return set(map(lambda t: t[0], c.fetchall()))

def get_equivalent_pdfs(conn, hashhex):
    c = conn.cursor()
    t = (hashhex,)
    c.execute('SELECT object2 FROM annotations WHERE object3 = "equivalent" and object1 = ?', t)
    return set(map(lambda t: t[0], c.fetchall()))

def get_direct_component_pdfs(conn, hashhex):
    c = conn.cursor()
    t = (hashhex,)
    c.execute('SELECT object2 FROM annotations WHERE object3 = "derived-from" and object1 = ?', t)
    return set(map(lambda t: t[0], c.fetchall()))
    
