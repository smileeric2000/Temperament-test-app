from fpdf import FPDF

def generate_pdf_report(name, temperament, description):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Temperament Test Result", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Temperament: {temperament}", ln=True)
    pdf.multi_cell(0, 10, txt=f"\nDescription:\n{description}")

    file_path = f"{name}_temperament_report.pdf"
    pdf.output(file_path)
    return file_path
