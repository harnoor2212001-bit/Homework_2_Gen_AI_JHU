## Initial Model
- **Initial Version:** General summary prompt.

## Revision 1: Structural Standardization
- **Revision 1:** Added "EXECUTIVE SUMMARY" header and "Potential Impact" bullet point.
- **What Changed:** The output became structured for quick reading.
- **Improvement:** It now identifies the financial consequence (yield impact) instead of just repeating the percentage.

## Revision 2: Automated Risk Flagging
- **Change:** Added logic to trigger an "AUDIT ALERT" for high-risk variances ( >25% prepayment or >5% dilution).
- **Observation:** The model correctly identified the 6% dilution and flagged it.
- **Improvement:** The system now acts as a preliminary auditor, highlighting specific concerns for human review rather than just summarizing.