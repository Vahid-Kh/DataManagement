import requests
import json
import epo_ops
import patent_client
from patent_client import USApplication
google_apps = USApplication.objects.filter(first_named_applicant='Google LLC')

microsoft_pats = (USApplication.objects
                  .filter(first_named_applicant='Microsoft')
                  .filter(app_status='Patented Case')
                  .order_by('patent_issue_date')
                  .limit(10)
                  )
print(google_apps[0])
print(microsoft_pats[0])
print(microsoft_pats.values('appl_id', 'patent_title')[:3].to_list())

from patent_client import Patent, PublishedApplication
test1 = Patent.objects.get("10000000")
test2 = PublishedApplication.objects.get("20200000001")
tennis_patents = Patent.objects.filter(title="tennis", assignee_name="wilson")
tennis_patents = Patent.objects.filter(query="TTL/tennis OR AN/wilson")
print(test1)
print(tennis_patents[0])
""" Full text can be retrieved by “publication” attribute """
basketball_patents = Patent.objects.filter(title="basketball")
basketball_patents[0].publication
"""US Applications
Original API URL: https://ped.uspto.gov/peds/"""
apps = USApplication.objects.filter(first_named_applicant='Caterpillar')
"""US Assignments
Original API URL: https://assignment-api.uspto.gov/documentation-patent/"""
from patent_client import Assignment
assignments = Assignment.objects.filter(patent_number='9534285')
assignments = Assignment.objects.filter(assignee='Google')
"""Date Ranges"""
from patent_client import PtabProceeding
PtabProceeding.objects.filter(accorded_filing_from_date="2020-01-01")
