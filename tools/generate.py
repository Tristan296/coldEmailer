from datetime import datetime
from fpdf import FPDF

class CoverLetterPDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 14)
        self.set_text_color(0)
    
    def add_section_spacing(self):
        self.ln(8)

def generate_cover_letter_pdf(company_name, position, recipient_address, your_name, your_address, date, body_text, filename="results/cover_letter.pdf"):
    pdf = CoverLetterPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Fonts
    heading_font = ("Times", "B", 12)
    body_font = ("Times", "", 12)

    # Margins
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)

    # Your info
    pdf.set_font(*body_font)
    pdf.cell(0, 10, your_name, ln=True)
    pdf.cell(0, 10, your_address, ln=True)
    pdf.cell(0, 10, date, ln=True)

    pdf.add_section_spacing()

    # Recipient info
    pdf.cell(0, 10, f"Hiring Manager at {company_name}", ln=True)
    pdf.cell(0, 10, recipient_address, ln=True)

    pdf.add_section_spacing()

    # Greeting
    pdf.set_font(*body_font)
    pdf.cell(0, 10, "Dear Hiring Manager,", ln=True)
    pdf.add_section_spacing()

    # Body
    pdf.set_font(*body_font)
    line_height = 7
    for paragraph in body_text.split("\n"):
        pdf.multi_cell(0, line_height, paragraph.strip())
        pdf.ln(2)

    pdf.add_section_spacing()

    # Closing
    pdf.cell(0, 10, "Sincerely,", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, your_name, ln=True)

    # Output file
    pdf.output(filename)

def generate_email(job):
    # Customize these parts as you want
    company = job.get('company', 'Hiring Team')
    title = job.get('title', 'the position')
    location = job.get('location', '')
    job_url = job.get('url', '')  # if your CSV has direct URLs
    
    email_body = f"""
    Subject: Enthusiastic applicant for {title} at {company}

    Dear {company} Hiring Team,

    I am very excited to apply for the {title} role{f' in {location}' if location else ''}. 
    With my skills in software development and a strong passion for technology, I am confident I would be a great fit for your team.

    I have attached my resume for your consideration, and you can view more details about my experience on my LinkedIn: www.linkedin.com/in/tristan-norbury

    I would love the opportunity to discuss how I can contribute to {company}’s success.

    Thank you for your time and consideration.

    Best regards,
    Tristan Norbury
    Email: tristannorbury123@gmail.com
    Phone: +61477494866
    """
    if job_url:
        email_body += f"\nJob link: {job_url}\n"
    return email_body.strip()

# Example usage:
# company = "Example Corp"
# position = "Software Engineer"
# recipient_addr = "123 Main St, Anytown, USA"
# your_name = "Tristan Norbury"
# your_addr = "Glenorie, NSW 2157, Australia"
# current_date = datetime.now().strftime("%B %d, %Y")
# letter_body = f"""
# I am writing to express my keen interest in the {position} position at {company}. My experience aligns well with the requirements outlined in your job posting.

# I hold a degree in Computer Science and have worked with Python, JavaScript, and cloud platforms like AWS. I take pride in writing clean, maintainable code, and collaborating effectively within teams.

# Thank you for your time and consideration. I would welcome the opportunity to discuss how my skills could benefit your team.
# """

# generate_cover_letter_pdf(company, position, recipient_addr, your_name, your_addr, current_date, letter_body)