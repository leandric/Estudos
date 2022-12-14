
# Credit Risk
base de dados --> https://www.kaggle.com/laotse/credit-risk-dataset

Processo realizado:
* Selecionado as colunas **person_age , person_income, loan_amnt e loan_status**.
* Colunas foram renomeadas respectivamente para: **idade, renda, emprestimo_mnt e status**.
* Tratamento de valores inconsistentes.
* Tratamento de valores nulos.
* Divisão de previsores e classe.
* Escalonamento de valores.

Descrição do conjunto de dados:

| Coluna                | Descrição                                                 | Tipo Variavel |
|-----------------------|-----------------------------------------------------------|--------------------|
|person_age             | Age                                                       | Numérica Discreta  |
|person_income          | Rendimento anual                                          | Categórica Continua|
|personhomeownership    | Propriedade de casa                                       | Numérica Discreta  |
|personemplength        | Tempo de trabalho (em anos)                               | Categórica Continua|
|loan_intent            | Intenção de empréstimo                                    | Categórica Continua|
|loan_grade             | Grau de empréstimo                                        | Categórica Continua|
|loan_amnt              | Montante do empréstimo                                    | Categórica Continua|
|loanintrate            | Taxa de juro                                              | Categórica Continua|
|loan_status            | Status do empréstimo (0 não é o padrão, 1 é o padrão)     | Categórica Discreta|
|loanpercentincome      | Renda percentual                                          | Categórica Continua|
|cbpersondefaultonfile  | Padrão histórico                                          | Categórica Continua|
|cbpresoncredhistlength | Comprimento do histórico de crédito                       | ??                 |
