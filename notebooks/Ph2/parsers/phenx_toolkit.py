import pandas as pd
import numpy as np
from parsers.names import Names as N
import os
from itertools import chain

class Term(object):
    def __init__(self,row):

        if N.SRC_INDEX in row:
            self.ID = row[N.SRC_INDEX]
            self.ID_INT = int(row[N.SRC_INDEX].replace('PX',''))
        else:
            self.ID = row[N.VARIABLE_TERM]
            self.ID_INT = int(row[N.VARIABLE_TERM].replace('PX',''))
        self.DESC = ' '.join(row[N.VARNAME].split('_')[1:])
        self.PARENT = row[N.VARNAME].split('_')[0]
        self.PARENT_INT = int(self.PARENT.replace('PX',''))
        self.VARDESC = row[N.VARDESC]

def define_term(row):
    t = Term(row)
    print(t.ID)
    return t

def parse_file(fname):
    try:
        df = pd.read_csv(fname, encoding= 'unicode_escape')

        terms = list(map(lambda s: Term(df.iloc[s]), df.index))
        return terms
    except Exception as e:
        print(e)
        return 'NA'


def parse_files(dir):
    terms = []
    for fname in os.listdir(dir):
        fterms = parse_file(os.path.join(dir, fname))
        if fterms != 'NA':
            terms.append(fterms)

    return list(chain.from_iterable(terms))

def get_all_term_names(terms):
    return list(map(lambda s: s.DESC,terms))

