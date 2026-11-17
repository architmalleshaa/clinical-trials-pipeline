# Data Spec

## Client question

A Pharma client wants to run a diabetes trial in the US. Which states have the most recruiting sites, and which sponsors already run trials there?

## Fields
- nctId: trial ID
- overallStatus: trial status
- leadSponsor name: company running the trial
- state: site state
- country: site country

## Rules
- Count only trials with overallStatus = RECRUITING
- Count only sites where country = United States
