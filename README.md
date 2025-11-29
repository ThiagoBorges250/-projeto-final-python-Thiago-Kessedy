# -projeto-final-python-Thiago-Kessedy
Projeto Final da disciplina de Programação Python
# Sistema de Cadastro de Loja

Este projeto implementa um **sistema de gerenciamento de produtos** para uma loja, utilizando Python e seguindo o modelo **CRUD** (Create, Read, Update, Delete).  
O sistema funciona no terminal e permite cadastrar, listar, atualizar e remover produtos, além de gerar relatórios automáticos.

---

## Funcionalidades do Sistema

O sistema inclui:

### **1. Cadastrar Produto**
Permite adicionar novos produtos ao sistema informando:
- Nome  
- Preço  
- Quantidade em estoque  

Cada produto recebe um **ID automático**.

---

### **2. Listar Produtos**
Exibe todos os produtos cadastrados em formato organizado, contendo:
- ID  
- Nome  
- Preço  
- Estoque  

---

### **3. Atualizar Produto**
Permite editar os dados de um produto existente:
- Nome  
- Preço  
- Estoque  

Os campos podem ser deixados em branco para manter o valor atual.

---

### **4. Remover Produto**
Remove um produto da lista com base no seu ID.

---

### **5. Gerar Relatório**
O sistema mostra:
- Total de itens em estoque  
- Valor total do estoque  
- Produto mais caro cadastrado  

---

### **6. Sair do Sistema**
Finaliza o programa com segurança.

---

## Estrutura dos Dados

Os produtos são armazenados em uma **lista de dicionários**, seguindo este formato:

```python
{
    "id": 1,
    "nome": "Mouse Gamer",
    "preco": 99.90,
    "estoque": 15
}
