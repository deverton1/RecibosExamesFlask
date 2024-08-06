function calculateTotal() {
    const admissionais = document.getElementById('admissionais').value.split('\n').filter(name => name.trim() !== '');
    const demissionais = document.getElementById('demissionais').value.split('\n').filter(name => name.trim() !== '');
    const periodicos = document.getElementById('periodicos').value.split('\n').filter(name => name.trim() !== '');
    
    const totalFuncionarios = admissionais.length + demissionais.length + periodicos.length;
    const precoExame = parseFloat(document.getElementById('precoExame').value);
    const valorTotal = totalFuncionarios * precoExame;

    document.getElementById('totalExames').value = `R$ ${valorTotal.toFixed(2)}`;
}
function consultaCnpj(){
    URL=("https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp?cnpj=")
}