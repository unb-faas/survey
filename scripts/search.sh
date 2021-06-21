#/bin/bash
# Source: https://github.com/jonatasgrosman/findpapers
source .env
QUERY="[serverless] OR [function-as-a-service] OR [function as a service] OR [backend-as-a-service] OR [backend as a service] OR [aws lambda] OR [google gloud platform] OR [azure functions]"
findpapers search search_results.json --token-ieee ${TI} --token-scopus ${TS} -q "${QUERY}"
