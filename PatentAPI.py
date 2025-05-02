from patent_client import USApplication, Inpadoc, Patent, PublishedApplication

# USPTO databases
Patent.objects.filter("filter criteria here")
PublishedApplication.objects.filter("filter criteria here")

# EPO databases
Inpadoc.objects.filter("filter criteria here")
# Import the model classes you need



from patent_client import Inpadoc, Assignment, USApplication, PatentBiblio

# Fetch US Patents with the word "tennis" in their title issued in 2010
pats = PatentBiblio.objects.filter(title="tennis", issue_date="2010-01-01->2010-12-31")



# Look at the first one
print(pats)

# Fetch US Applications
app = USApplication.objects.get('15710770')
print(app.patent_title)


# Fetch from USPTO Assignments
assignments = Assignment.objects.filter(assignee='Google')
print(len(assignments))

assignment = Assignment.objects.get('47086-788')
print(assignment.conveyance_text)

# Fetch from INPADOC
pub = Inpadoc.objects.get('EP3082535A1')
print(pub.biblio.title)
