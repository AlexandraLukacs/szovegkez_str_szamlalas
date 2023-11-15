"""Szövegkezelés - Hányszor szerepel egy adott string?
Egy tetszőleges Stringben meg kell számolni, hogy egy másik String hányszor fordul elő. 
A feladat egyszerűsítése érdekében, most kis és nagybetűk között nem teszünk különbséget, 
bár azzal sem lenne túl bonyolult a feladat.
"""

def string_szamolas():
    szoveg: str= "kék ég alatt kék virágok nőnek."
    db: str= "kék"
    s: str= szoveg.count(db)
    print(szoveg)
    print(f"A 'kék' szó {s} alkalommal fordul elő.")