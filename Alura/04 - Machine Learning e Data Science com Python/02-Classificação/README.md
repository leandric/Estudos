# Estudos em modelos de Classificação

* **Classificação:** baseia-se em prever a categoria de uma observação dada. Aqui, procura-se estimar um “classificador” que gere como saída a classificação qualitativa de um dado não observado com base em dados de entrada (que abrangem observações com classificações já definidas).
Exemplo: um classificador que utilize dados não observados de um paciente e classifique-o como doente ou não-doente.

## Desempenho

Acurácia e erro podem ser medidas utilizando a equação abaixo.

![image](https://user-images.githubusercontent.com/45865115/145413215-837d2267-7251-4c4f-b4ec-b5b2ced9d0a7.png)

* True Positive (TP): Valores classificados como positivos nos dados originais e corretamente previstos como positivos no modelo.
* True Negatives (TN): Valores classificados como negativos nos dados originais e corretamente previstos como negativos no modelo.
* False Positives (FP): Valores classificados como negativos nos dados originais e erroneamente previstos como positivos no modelo.
* False Negatives (FN): Valores classificados como positivos nos dados originais e erroneamente previstos como negativos no modelo.

### Confuision Matrix

![image](https://user-images.githubusercontent.com/45865115/145414013-ac1b41fa-76dc-41fe-a5c5-2e78d7d672d2.png)

![image](https://user-images.githubusercontent.com/45865115/145414300-ffec579c-3303-463e-b327-b10ff36ba017.png)

