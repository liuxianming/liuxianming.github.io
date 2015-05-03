#! /usr/local/bin/python

import sys
sys.path.append('./')

from tex2rst import bibtex2htmldiv

bibtex2htmldiv.bib2html('publication.bib')
