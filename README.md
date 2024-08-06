## Documentação Detalhada do Sistema de Gerenciamento de Recibos de Exames

### Visão Geral
Este sistema web foi desenvolvido para gerenciar e gerar recibos de exames admissionais, demissionais e periódicos para empresas. A aplicação utiliza Flask como framework web, FPDF para a geração de PDFs, e HTML/CSS/JavaScript para a interface do usuário.

### Estrutura do Projeto

#### Arquivos e Diretórios
1. **app.py**: Arquivo principal da aplicação Flask que contém as rotas e a lógica para gerar os recibos em PDF.
2. **templates/index.html**: Template HTML para a página principal do formulário de recibos.
3. **static/style.css**: Arquivo CSS para estilização da página HTML.
4. **static/script.js**: Arquivo JavaScript para calcular o valor total dos exames no frontend.

### Código Backend (app.py)
#### Importações
- **io**: Biblioteca para manipulação de fluxos de entrada/saída em memória.
- **Flask**: Framework web para Python.
- **render_template**: Função do Flask para renderizar templates HTML.
- **request**: Objeto do Flask para manipulação de dados enviados via requisições HTTP.
- **send_file**: Função do Flask para enviar arquivos como resposta HTTP.
- **FPDF**: Biblioteca para geração de PDFs.

#### Instância do Flask
- `app = Flask(__name__)`: Cria uma instância da aplicação Flask.

#### Rotas
- **Rota Principal ('/')**:
  - `@app.route('/')`: Define a rota principal da aplicação.
  - `def index()`: Função que renderiza o template `index.html`.

- **Rota de Geração de Recibo ('/generate_receipt')**:
  - `@app.route('/generate_receipt', methods=['POST'])`: Define a rota para gerar recibos, aceitando apenas requisições POST.
  - `def generate_receipt()`: Função que processa os dados do formulário, gera o PDF e retorna o arquivo como resposta.

#### Função `generate_receipt()`
1. **Recepção de Dados do Formulário**:
   - `nome_empresa_cliente`: Nome da empresa cliente.
   - `admissionais`: Lista de funcionários admissionais.
   - `demissionais`: Lista de funcionários demissionais.
   - `periodicos`: Lista de funcionários periódicos.
   - `preco_exame`: Preço unitário por exame.

2. **Processamento dos Dados**:
   - Filtra os nomes de funcionários para remover entradas vazias.
   - Calcula o número total de funcionários e o valor total dos exames.

3. **Geração do PDF**:
   - Cria uma instância do `FPDF`.
   - Adiciona uma página e define a fonte.
   - Adiciona cabeçalhos e tabelas com os dados dos exames e funcionários.
   - Calcula e adiciona o valor total ao PDF.

4. **Salvamento e Envio do PDF**:
   - Salva o PDF em um objeto de memória `BytesIO`.
   - Define o nome do arquivo para download.
   - Retorna o arquivo como resposta para o cliente.

### Código Frontend (index.html)
#### Estrutura HTML
- **Cabeçalho**:
  - Meta tags para charset e viewport.
  - Título da página.
  - Links para o CSS e script JavaScript.

- **Conteúdo**:
  - Botão para consulta de CNPJ.
  - Formulário para entrada de dados:
    - Campo para o nome da empresa cliente.
    - Textareas para listas de funcionários admissionais, demissionais e periódicos.
    - Campo para o preço por exame.
    - Campo para o valor total (calculado dinamicamente).
    - Botão para gerar o recibo.

- **Rodapé**:
  - Texto de copyright.

### Código CSS (style.css)
- Define estilos básicos para a página, incluindo:
  - Fonte padrão.
  - Layout e espaçamento do container principal.
  - Estilos para o cabeçalho, formulário e campos de entrada.
  - Estilos para o botão, incluindo efeito de hover.

### Código JavaScript (script.js)
#### Função `calculateTotal()`
- Obtém as listas de nomes dos funcionários dos textareas.
- Filtra as listas para remover entradas vazias.
- Calcula o número total de funcionários.
- Multiplica o total de funcionários pelo preço do exame.
- Atualiza o campo de valor total no formulário com o valor calculado.

### Execução da Aplicação
- `if __name__ == '__main__': app.run('0.0.0.0')`: Inicia a aplicação Flask no endereço '0.0.0.0', tornando-a acessível em todas as interfaces de rede do servidor.

### Conclusão
Este sistema fornece uma solução simples e eficaz para a geração de recibos de exames admissionais, demissionais e periódicos. A combinação de Flask, FPDF, e tecnologias web padrão (HTML/CSS/JavaScript) permite criar uma interface amigável para o usuário e gerar documentos PDF profissionalmente formatados.
