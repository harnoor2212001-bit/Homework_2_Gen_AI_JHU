# Evaluation Set: ABS Technical-to-Plain-English

### Case 1: Normal (Loss History)
**Input:** "The pool characteristics include a 2.4% historical loss rate, defined as the aggregate value of write-offs within the static pool of loans exhibiting identical risk-tiering and vintage characteristics as the underlying assets."
**Goal:** Should explain that 'loss history' is just the record of loans being written off in similar groups.

### Case 2: Normal (Dilution)
**Input:** "Cash flows may be subject to dilution risk in instances where obligors utilize corporate-issued gift cards or internal credit lines to satisfy outstanding balances, thereby reducing net organic cash receipts."
**Goal:** Should clearly explain that 'dilution' means paying with company money/gift cards instead of outside cash.

### Case 3: Edge Case (Mixed Definitions)
**Input:** "While loss history remains within historical norms, net proceeds were impacted by a 50bps increase in dilution due to a seasonal surge in gift card redemptions."
**Goal:** The model must distinguish between money lost (write-offs) and money 'diluted' (gift cards) in the same paragraph.

### Case 4: Edge Case (Dense Jargon/Numbers)
**Input:** "The prospectus supplement details a 15% overcollateralization trigger designed to mitigate both delinquency-related write-offs and potential dilution from promotional credit card offsets."
**Goal:** Must maintain the 15% figure accurately while simplifying the meaning of overcollateralization.

### Case 5: Likely Failure/Hallucination Risk
**Input:** "The dilution factor is non-material due to the circular nature of the internal ledger offsets."
**Goal:** This is vague. A good output should admit it's a technical accounting detail or stay very high-level. A 'failure' would be the AI guessing that 'dilution' means something like 'watering down stock' (the common definition) instead of your specific gift card definition.