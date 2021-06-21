import sys
import json
try:
    filename = sys.argv[1]
except IndexError:
    filename=False

try:
    field = sys.argv[2]
except IndexError:
    field=False

try:
    year = sys.argv[3]
except IndexError:
    year=False


if filename and field:
    file = open(filename, 'r')
    file = file.read()
    file = json.loads(file)
    papers = file["papers"]
    papers_selected = []
    for paper in papers:
        if paper:
            if (year):
                pDate = paper["publication_date"]
                if year in pDate:
                     papers_selected.append(paper)
            else:
                papers_selected.append(paper)
    field_content = []
    separator=" "
    for paper in papers_selected:
        if field in paper:
            content = paper[field]
            if len(content)>0:
                if isinstance(content, list):
                    separator="\""
                    for term in content:
                        field_content.append("\""+term+"\"")
                else:    
                    field_content.append(content)
    field_content = " ".join(field_content)
    field_content = field_content.replace('-'," ").replace('_'," ")
    field_content_cleaned = field_content
    for i in field_content:
        if i.isalpha() or i.isspace() or i=="\"" or i.isnumeric():
            field_content_cleaned = "".join([field_content_cleaned,i])
    field_content_cleaned = field_content_cleaned.lower()
    field_content_cleaned = field_content_cleaned.replace("\n","").replace("   "," ").strip().replace("   "," ").strip().replace("  "," ").strip().replace("  "," ")
    field_content_cleaned = field_content_cleaned.split(separator)
    field_content = []
    for term in field_content_cleaned:
        if len(term)>1:
            field_content.append(term)
    for term in field_content:
        print(term)