# Is file me reports generate karne ke templates hain
import os

# Dark mode HTML dashboard banane ka function
def generate_html_report(results, summary, filename="report.html"):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Testing Track - Evaluation Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0B0F19;
            --card-bg: rgba(22, 28, 45, 0.6);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #F3F4F6;
            --text-secondary: #9CA3AF;
            --primary: #6366F1;
            --success: #10B981;
            --success-bg: rgba(16, 185, 129, 0.1);
            --danger: #EF4444;
            --danger-bg: rgba(239, 68, 68, 0.1);
            --glow-primary: rgba(99, 102, 241, 0.15);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 2rem;
            background-image: 
                radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.1) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.05) 0px, transparent 50%);
            background-attachment: fixed;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            margin-bottom: 3rem;
            text-align: center;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #FFF 30%, var(--primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--text-secondary);
            font-size: 1.1rem;
            font-weight: 300;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }}

        .stat-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(99, 102, 241, 0.3);
        }}

        .stat-value {{
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
            color: #FFF;
        }}

        .stat-label {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
        }}

        .results-list {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}

        .result-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 2rem;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            transition: border-color 0.3s ease;
        }}

        .result-card.passed {{
            border-left: 4px solid var(--success);
        }}

        .result-card.failed {{
            border-left: 4px solid var(--danger);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 1rem;
        }}

        .test-title {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #FFF;
        }}

        .badge {{
            padding: 0.4rem 1rem;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .badge.pass {{
            background-color: var(--success-bg);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }}

        .badge.fail {{
            background-color: var(--danger-bg);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.2);
        }}

        .content-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }}

        @media (min-width: 768px) {{
            .content-grid {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        .content-box {{
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 1.25rem;
        }}

        .box-label {{
            font-size: 0.8rem;
            text-transform: uppercase;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}

        .box-value {{
            font-size: 0.95rem;
            line-height: 1.6;
            white-space: pre-wrap;
            color: #E5E7EB;
        }}

        .meta-footer {{
            margin-top: 1.5rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            font-size: 0.85rem;
            color: var(--text-secondary);
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 1rem;
        }}

        .meta-item strong {{
            color: #FFF;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Testing Track Evaluation</h1>
            <div class="subtitle">Structured LLM Performance & Safety Assessment</div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{summary['total']}</div>
                <div class="stat-label">Total Scenarios</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" style="color: var(--success);">{summary['passed']}</div>
                <div class="stat-label">Passed</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" style="color: var(--danger);">{summary['failed']}</div>
                <div class="stat-label">Failed</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" style="background: linear-gradient(135deg, #FFF 30%, var(--primary) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{summary['rate']:.1f}%</div>
                <div class="stat-label">Success Rate</div>
            </div>
        </div>

        <div class="results-list">
"""

    for res in results:
        status_class = "passed" if res["passed"] else "failed"
        badge_class = "pass" if res["passed"] else "fail"
        badge_text = "Pass" if res["passed"] else "Fail"
        
        prompt_html = ""
        if "prompt" in res:
            prompt_html = f"""
                <div class="content-box">
                    <div class="box-label">Prompt</div>
                    <div class="box-value">{res['prompt']}</div>
                </div>
            """
        elif "turns" in res:
            turns_desc = []
            for t in res["turns"]:
                turns_desc.append(f"[{t['role'].upper()}]: {t['content']}")
            prompt_html = f"""
                <div class="content-box">
                    <div class="box-label">Multi-turn Conversation Flow</div>
                    <div class="box-value">{chr(10).join(turns_desc)}</div>
                </div>
            """

        html_content += f"""
            <div class="result-card {status_class}">
                <div class="card-header">
                    <div class="test-title">{res['name']}</div>
                    <div class="badge {badge_class}">{badge_text}</div>
                </div>
                <div class="content-grid">
                    {prompt_html}
                    <div class="content-box">
                        <div class="box-label">Model Response</div>
                        <div class="box-value">{res['response']}</div>
                    </div>
                </div>
                <div class="meta-footer">
                    <div class="meta-item">Assertion: <strong>{res['assertion']}</strong></div>
                    <div class="meta-item">Details: <strong>{res['reason']}</strong></div>
                </div>
            </div>
        """

    html_content += """
        </div>
    </div>
</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

# Print-ready PDF report banane ka function using fpdf2
def generate_pdf_report(results, summary, filename="report.pdf"):
    from fpdf import FPDF

    # Report page layout structure manage karne ke liye subclass kiya hai
    class PDFReport(FPDF):
        def header(self):
            self.set_fill_color(11, 15, 25)
            self.rect(0, 0, 210, 297, "F")
            self.set_text_color(255, 255, 255)
            self.set_font("Helvetica", "B", 14)
            self.cell(0, 10, "TEQFORK AI TESTING TRACK EVALUATION REPORT", 0, 1, "C")
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_text_color(156, 163, 175)
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Evaluation Summary Status", 0, 1)
    pdf.ln(2)

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(45, 8, f"Total Scenarios: {summary['total']}", 0, 0)
    pdf.cell(45, 8, f"Passed: {summary['passed']}", 0, 0)
    pdf.cell(45, 8, f"Failed: {summary['failed']}", 0, 0)
    pdf.cell(45, 8, f"Success Rate: {summary['rate']:.1f}%", 0, 1)
    pdf.ln(10)

    # Saare results ko pdf page par dynamic print karenge
    for res in results:
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(150, 8, res["name"], 0, 0)
        
        if res["passed"]:
            pdf.set_text_color(16, 185, 129)
            pdf.cell(40, 8, "PASSED", 0, 1, "R")
        else:
            pdf.set_text_color(239, 68, 68)
            pdf.cell(40, 8, "FAILED", 0, 1, "R")
            
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 5, f"Assertion: {res['assertion']}", 0, 1)
        pdf.cell(0, 5, f"Details: {res['reason']}", 0, 1)
        pdf.ln(2)

        pdf.set_fill_color(22, 28, 45)
        pdf.set_font("Helvetica", "B", 9)
        
        if "prompt" in res:
            pdf.cell(0, 6, "Prompt:", 0, 1, "L", fill=True)
            pdf.set_font("Helvetica", "", 9)
            pdf.multi_cell(0, 5, res["prompt"])
        elif "turns" in res:
            pdf.cell(0, 6, "Conversation turns:", 0, 1, "L", fill=True)
            pdf.set_font("Helvetica", "", 9)
            turns_desc = []
            for t in res["turns"]:
                turns_desc.append(f"[{t['role'].upper()}]: {t['content']}")
            pdf.multi_cell(0, 5, "\n".join(turns_desc))
            
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(0, 6, "Response:", 0, 1, fill=True)
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(0, 5, res["response"])
        pdf.ln(8)

    pdf.output(filename)
