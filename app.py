from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_receipt', methods=['POST'])
def generate_receipt():
    nome_empresa_cliente = request.form['nomeEmpresaCliente']
    admissionais = request.form['admissionais'].split('\n')
    demissionais = request.form['demissionais'].split('\n')
    periodicos = request.form['periodicos'].split('\n')
    preco_exame = float(request.form['precoExame'])
    
    # Filtrar nomes vazios
    admissionais = [nome.strip() for nome in admissionais if nome.strip()]
    demissionais = [nome.strip() for nome in demissionais if nome.strip()]
    periodicos = [nome.strip() for nome in periodicos if nome.strip()]
    
    total_funcionarios = len(admissionais) + len(demissionais) + len(periodicos)
    valor_total = total_funcionarios * preco_exame
    
    # Criar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="SL ASSESSORIA EMPRESARIAL", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Empresa Cliente: {nome_empresa_cliente}", ln=True, align='C')
    
    pdf.ln(10)  # Add a line break
    
    # Create table headers
    pdf.cell(60, 10, txt="Tipo de Exame", border=1, align='C')
    pdf.cell(100, 10, txt="Nome do Funcionário", border=1, align='C')
    pdf.cell(30, 10, txt="Preço", border=1, align='C')
    pdf.ln(10)
    
    # Add Admissionais
    for nome in admissionais:
        pdf.cell(60, 10, txt="Admissional", border=1, align='C')
        pdf.cell(100, 10, txt=nome, border=1, align='L')
        pdf.cell(30, 10, txt=f"R$ {preco_exame:.2f}", border=1, align='R')
        pdf.ln(10)
    
    # Add Demissionais
    for nome in demissionais:
        pdf.cell(60, 10, txt="Demissional", border=1, align='C')
        pdf.cell(100, 10, txt=nome, border=1, align='L')
        pdf.cell(30, 10, txt=f"R$ {preco_exame:.2f}", border=1, align='R')
        pdf.ln(10)
    
    # Add Periódicos
    for nome in periodicos:
        pdf.cell(60, 10, txt="Periódico", border=1, align='C')
        pdf.cell(100, 10, txt=nome, border=1, align='L')
        pdf.cell(30, 10, txt=f"R$ {preco_exame:.2f}", border=1, align='R')
        pdf.ln(10)
    
    pdf.ln(10)
    pdf.cell(160, 10, txt="Valor Total", border=1, align='R')
    pdf.cell(30, 10, txt=f"R$ {valor_total:.2f}", border=1, align='R')
    
    # Salvar PDF em memória
    pdf_output = io.BytesIO()
    pdf_output.write(pdf.output(dest='S').encode('latin1'))
    pdf_output.seek(0)
    
    return send_file(pdf_output, as_attachment=True, download_name="recibo.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)