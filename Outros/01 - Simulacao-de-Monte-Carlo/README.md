# Simulação de Monte Carlo

O método Monte Carlo começou a ser usado para avaliar integrais matemáticas complicadas. 
Hoje também pode ser usada para se fazer análise de mercado para investimentos.


## Calculo

### Drift
  ![image](img/drif.png)
 
   Indica a direção que os valores tiveram no passado, é dada média menos 1 sobre 2 multiplicado pela variança ao quadrado.
  

### Volatility
  ![image](img/volalitily.png)

   Variavel aleatoria : 
   calculo do desvio padrão(indica o quanto as taxas de retorno estão afastadas da média).
   É preciso criar uma matriz contendo de numeros aleatorios nume distribuição normal.
  
  ![image](img/dist.png)

### Simulações
![image](img/simulacao.png)

   Através da exponeciação de drift + o desvio padrão multiplicado na matriz de volatility obtemos uma matriz de simulações.
   No caso realizei 1.000 simulações buscando 192 posições no futuro:

![image](img/simulacoes.png)


# Escolhendo a melhor Simulação

   Para Encontrar a melhor simulação utilizo o calculo do erro médio absoluto, então seleciono a simulação com o menor erro.

![image](img/melhor_simulacao.png)
  
