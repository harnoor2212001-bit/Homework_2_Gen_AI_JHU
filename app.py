import os
from groq import Groq

# 1. Initialize the Groq client
# It will automatically look for the "GROQ_API_KEY" environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Define the System Instruction (Configurable Step)
SYSTEM_PROMPT = """
You are a specialized Financial Audit Assistant for Verizon's ABS (Asset-Backed Securities) team.
Your task is to translate technical prospectus jargon into "Plain English" for executives.

Key Domain Definitions:
- Loss History: The history of write-offs among loans with the same characteristics as those in the deal.
- Dilution: Using company gift cards or credit cards to pay off loan balances (self-generated cash vs. organic customer cash).
- Prepayment - Individual loan that is part of the issued security being paid off early.

Guidelines:
- Keep summaries to 2-3 sentences.
- Maintain numerical accuracy.
- Tone: Professional, objective, and auditor-focused.
- Format the output as follows: Start with a bold header 'EXECUTIVE SUMMARY' followed by a single-sentence definition and one bullet point titled 'Potential Impact'.
- If a mentioned metric is more than 5% higher than market average, add a bold 'AUDIT ALERT' at the bottom suggesting a deeper dive into the underlying asset eligibility criteria.
"""

def summarize_text(input_text):
    try:
        chat_completion = client.chat.completions.create(
            # Using Llama 3.3 70B (High performance, Free on Groq)
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            temperature=0.1, # Low temperature for consistent audit results
            max_tokens=150
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Test case from your eval_set.md
    sample_input = "Characteristics of the included loans contain 6% higher dilution rates than market average"
    
    print("--- ABS Technical Input ---")
    print(sample_input)
    print("\n--- Plain English Summary ---")
    print(summarize_text(sample_input))