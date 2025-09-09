# resume.py

# === Personal Info ===
name = "Mmabatho Mahlangu"
email = "mahlangummabatho109@gmail.com"
phone = "0766267607"
linkedin = "https://www.linkedin.com/in/mahlangu-mmabatho-488005270/"

# === Education ===
education = [
    {
        "degree": "National Diploma in Information Technology",
        "university": "VaaL University of Technology",
        "year": "2023 - Still ongoing"
    }
]

# === Experience ===
experience = [
    {
        "role": "N/A",
        "company": "N/A",
        "year": "N/A",
        "details": "N/A"
    }
]

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


# === Print Resume ===
def print_resume():
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"LinkedIn: {linkedin}\n")
    
    print("Education:")
    for edu in education:
        print(f"- {edu['degree']}, {edu['university']} ({edu['year']})")
    
    print("\nExperience:")
    for exp in experience:
        print(f"- {exp['role']} at {exp['company']} ({exp['year']})")
        print(f"  {exp['details']}")
    
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")

if __name__ == "__main__":
    print_resume()
