# Word Cloud Generator 

FILE=search_results.json
CATEGORIES_CONTRIBUTION="Contribution:Metric,Tool,Model,Method"
CATEGORIES_RESEARCH_TYPE="Research Type:Validation Research,Solution Proposal,Philosophical,Opinion,Experience,Other"
HIGHLIGHTS="propose, achiev, accuracy, method, metric, result, limitation, state of the art, serverless, function as a service, faas, function-as-a-service"
#findpapers refine ${FILE} --abstract --extra-info --categories "$CATEGORIES_CONTRIBUTION" --categories "$CATEGORIES_RESEARCH_TYPE" --highlights "$HIGHLIGHTS"
findpapers refine ${FILE} -r --abstract --extra-info --highlights "$HIGHLIGHTS"
