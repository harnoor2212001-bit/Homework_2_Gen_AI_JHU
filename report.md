Report: ABS Technical Disclosure Translator  
Author: Harnoor Singh  

1. Business Use Case  
The Asset-Backed Securities (ABS) market relies on complex legal disclosures, or prospectus documents, to communicate risk. For a finance professional in Internal Audit at a company like Verizon, these documents are essential but very dense.  
The Goal: To translate technical terms, specifically Loss History, Prepayment Rates, and Dilution, into plain English summaries for non-technical executive stakeholders.  
Value: Automating the first pass of these summaries reduces the manual burden on audit teams and ensures that "red flags," like high gift card dilution, are flagged immediately for human review.

2. Model Selection and Technical Pivot  
Initial Choice: I began development using Google Gemini (1.5, 2.0, and 3-Flash).  
Observed Challenges: I encountered persistent 404 NOT_FOUND and 429 RESOURCE_EXHAUSTED errors. These issues arose from a mix of rapid API version updates and strict free-tier rate limits.  
Final Selection: I pivoted to Llama 3.3-70B via Groq.  
Reasoning: Groq offered a more stable, OpenAI-compatible SDK and much faster inference speeds using LPU technology, which made the testing process more efficient.

3. Design Evolution & Prompt Iteration  
The system improved through three distinct stages:  

Version: Baseline
Focus: Basic Definition  
Result: This provided a simple summary, but it lacked professional structure and an executive tone.  

Version: Revision 1  
Focus: Structural Formatting  
Result: I added EXECUTIVE SUMMARY headers and Potential Impact bullets to enhance scannability for leadership.  

Version: Revision 2  
Focus: Risk-Based Logic  
Result: I included AUDIT ALERT flags. If a metric, such as Dilution > 5%, exceeded a threshold, the system highlighted it for deeper investigation.  
Evidence of Improvement: In testing, the final design correctly identified a 6% dilution rate from using internal gift cards to pay balances and triggered an alert. The baseline, however, only noted this as a fact.

4. Limitations and Human Review  
Despite its accuracy, the prototype has clear boundaries:
  
Contextual Nuance: The AI can identify that a variance exists, but it cannot explain why, such as a specific marketing promotion that causes a spike in gift card usage.  
Threshold Sensitivity: The risk thresholds, like 5% dilution, are hard-coded in the prompt. A human auditor must periodically check if these thresholds remain appropriate for the current economy.

5. Deployment Recommendation  
I recommend deploying this workflow as an "Internal Audit Co-pilot" under the following conditions:  
Advisory Only: The output must be clearly labeled as AI-generated and used only for preliminary screening.  
Review Requirement: Every "Audit Alert" must be approved by a Senior Analyst or Manager.  
Data Security: Ensure the API environment complies with Verizon's internal data privacy policies before processing proprietary loan data.