# Teqfork Interns Final AI Testing Track Evaluation Framework

This is a clean, robust, and interactive Python-based LLM testing and evaluation framework designed specifically to fulfill the requirements of the **Teqfork AI Testing Track**. It implements, executes, and evaluates the 7 mandatory LLM test scenarios and generates premium HTML and PDF submission-ready reports.

## Features

- **7 Required Test Scenarios**: Complete out-of-the-box support for:
  - Factual Accuracy
  - Instruction Following
  - Edge Case / Ambiguity
  - Safety / Refusal
  - Consistency (multi-trial similarity profiling)
  - Context Retention (multi-turn conversation flow)
  - Hallucination Detection (fictitious entity evaluation)
- **Flexible Modes**: Automatically prompts for a Gemini API Key or runs in an elegant offline **Demo Mode** to show the reports without using API quotas.
- **Premium Reporting**: Generates a glassmorphic modern Dark HTML Dashboard and a clean, structured PDF Evaluation Report suitable for supervisor submissions.
- **GitHub Uploader**: Includes an automated initialization script to stage, commit, and link your code to your private/public GitHub repository.

## Prerequisites

Make sure you have Python 3.8+ and Git installed on your system.

## Setup Instructions

1. Set your Gemini API Key in your environment:
   - **Windows (Command Prompt)**: `set GEMINI_API_KEY=your_key_here`
   - **Windows (PowerShell)**: `$env:GEMINI_API_KEY="your_key_here"`
   - **macOS/Linux**: `export GEMINI_API_KEY="your_key_here"`

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Evaluation

To execute the test suite, run:
```bash
python run_tests.py
```

*Note: If no API key is set in the environment or entered at the prompt, the framework will run in demo/offline mode using high-fidelity pre-configured responses to demonstrate the full reporting capabilities.*

## Exploring Reports

- **report.html**: Open this in any web browser to view a beautifully formatted, responsive dark mode results dashboard.
- **report.pdf**: A clean, structured PDF containing all prompt logs, model responses, and assertion reasons for formal submission.

## Uploading to GitHub

To quickly initialize Git, add a `.gitignore`, commit your files, and push to GitHub, run:
```bash
python push_to_github.py
```
And follow the simple on-screen instructions!
