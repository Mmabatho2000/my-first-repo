from fpdf import FPDF

# === Personal Info ===
name = "Mmabatho"
email = "your.email@example.com"
phone = "+27 123 456 789"
linkedin = "https://www.linkedin.com/in/yourprofile"

# === Education ===
education = [
    {
        "degree": "BSc in Computer Science",
        "university": "University Name",
        "year": "2025"
    }
]

# === Experience ===
experience = []  # No work experience yet

# === Skills ===
skills = [
    "Microsoft Office (Word, Excel, PowerPoint)",
    "Basic Python programming",
    "Internet research",
    "Email and professional communication",
    "Time management",
    "Teamwork / Collaboration",
    "Problem solving"
]

# === Create PDF ===
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Personal Info
pdf.cell(0, 10, name, ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 8, f"Email: {email}", ln=True)
pdf.cell(0, 8, f"Phone: {phone}", ln=True)
pdf.cell(0, 8, f"LinkedIn: {linkedin}", ln=True)
pdf.ln(5)

# Education
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "Education:", ln=True)
pdf.set_font("Arial", '', 12)
for edu in education:
    pdf.cell(0, 8, f"- {edu['degree']}, {edu['university']} ({edu['year']})", ln=True)
pdf.ln(3)

# Experience
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "Experience:", ln=True)
pdf.set_font("Arial", '', 12)
if experience:
    for exp in experience:
        pdf.cell(0, 8, f"- {exp['role']} at {exp['company']} ({exp['year']})", ln=True)
        pdf.cell(0, 8, f"  {exp['details']}", ln=True)
else:
    pdf.cell(0, 8, "- No work experience yet", ln=True)
pdf.ln(3)

# Skills
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "Skills:", ln=True)
pdf.set_font("Arial", '', 12)
for skill in skills:
    pdf.cell(0, 8, f"- {skill}", ln=True)

# Save PDF
pdf.output("resume.pdf")
print("✅ resume.pdf created successfully!")
