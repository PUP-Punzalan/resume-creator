# importing all necessary things (filename, json, fpdf)
from fileinput import filename
import json
from fpdf import FPDF

# formatting the pdf file (portrait, milimeters, legal size)
pdf = FPDF('P', 'mm', 'Legal')
pdf.add_page()

# importing the json file as variable
with open('datas.json') as data:
    datas = json.load(data)

for i in datas:
    # header
    pdf.set_font('times', 'B', 20)
    pdf.cell(3, 0)
    pdf.cell(0, 10, i["name"], ln=1)

    # body
    pdf.set_font('times', 'I', 12)
    pdf.cell(0, 7, i["address"], ln=1)
    pdf.cell(0, 7, i["phone_number"], ln=1)
    pdf.cell(0, 7, i["e_mail"], ln=1)
    pdf.cell(0, 7, i["website"], ln=1)
    pdf.ln(4)

    # skills title
    pdf.set_font('times', 'B', 16)
    pdf.cell(0, 10, 'Skills:', ln=1)

    # skills data
    for skill in i["skills"]:
        pdf.set_font('times', '', 12)
        pdf.cell(0, 7, f"{skill['skill']}", ln=1)

    # experience title
    pdf.ln(4)
    pdf.set_font('times', 'B', 16)
    pdf.cell(0, 10, 'Experiences:', ln=1)
    pdf.ln(1)

    # job1 title
    pdf.set_font('times', 'BI', 14)
    pdf.cell(0, 6, i['job1'], ln=1)

    # experience1 data
    for exp in i["experience1"]:
        pdf.set_font('times', '', 12)
        pdf.cell(0, 8, f"{exp['date']}", ln=1)
        pdf.cell(0, 6, f"{exp['company']}", ln=1)
        pdf.cell(0, 6, f"{exp['place']}", ln=1)
        pdf.cell(0, 8, f"{exp['desc']}", ln=1)

    # job2 title
    pdf.ln(4)
    pdf.set_font('times', 'BI', 14)
    pdf.cell(0, 6, i['job2'], ln=1)

    # experience2 data
    for exp in i["experience2"]:
        pdf.set_font('times', '', 12)
        pdf.cell(0, 8, f"{exp['date']}", ln=1)
        pdf.cell(0, 6, f"{exp['company']}", ln=1)
        pdf.cell(0, 6, f"{exp['place']}", ln=1)
        pdf.cell(0, 8, f"{exp['desc']}", ln=1)

    # academic title
    pdf.ln(4)
    pdf.set_font('times', 'B', 16)
    pdf.cell(0, 10, 'Academic Background:', ln=1)
    pdf.ln(2)

    # date1 data
    pdf.set_font('times', '', 12)
    pdf.cell(28, 6, i['date1'])

    # academic data
    for acad in i["academic"]:
        pdf.set_font('times', '', 12)
        pdf.cell(0, 6, f"{acad['school']}", ln=1)
        pdf.cell(28, 0)
        pdf.cell(0, 6, f"{acad['course']}", ln=1)
        pdf.cell(28, 0)
        pdf.cell(0, 6, f"{acad['place']}", ln=1)

    # set line
    pdf.set_line_width(0.6)
    pdf.line(12, 11, 12, 19)
    pdf.set_line_width(0.3)
    pdf.line(10, 50, 200, 50)
    pdf.line(10, 106, 200, 106)
    pdf.line(10, 192, 200, 192)

# exporting the data to pdf
pdf.output('resume.pdf')