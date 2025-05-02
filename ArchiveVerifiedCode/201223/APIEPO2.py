""" This library Inpadoc is currently notmworking """


import epo_ops
from patent_client import Inpadoc


""" From EPO """


"""
Keyword	CQL Equivalent	                       # Notes
title	title	 
abstract	abstract	 
title_and_abstract	titleandabstract	 
inventor	inventor	 
applicant	applicant	 
inventor_or_applicant	inventorandapplicant	 
epodoc_publication	spn	 
epodoc_application	sap	 
priority	prioritynumber	 
epodoc_priority	spr	 
number	num	                         #Pub, App, or Priority Number
publication_date	publicationdate	 
citation	citation	 
cited_in_examination	ex	 
cited_in_opposition	op	 
cited_by_applicant	rf	 
other_citation	oc	 
family	famn	 
cpc_class	cpc	 
ipc_class	ipc	 
ipc_core_invention_class	ci	 
ipc_core_additional_class	cn	 
ipc_advanced_class	ai	 
ipc_advanced_additional_class	an	 
ipc_advanced_class	a	 
ipc_core_class	c	 
classification	cl	                 # IPC or CPC Class
full_text	                        #txt	title, abstract, inventor and applicant
"""
import sys, json
client = epo_ops.Client(key='udiuu8ajbQHdG0FEZ5WlPcXhkGSa3E5E', secret='1E4F7RAQklF1wHM3')  # Instantiate client

case = Inpadoc.objects.get('EP2906782A2')
bib_data = case.biblio
bib_data.title

from pprint import pprint
import requests

case = Inpadoc.objects.get('EP2906782A2')
pprint(list(case.family))
results = Inpadoc.objects.filter(cql_query='pa="Google LLC"')