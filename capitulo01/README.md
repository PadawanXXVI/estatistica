# ANÁLISE EXPLORATÓRIA DE DADOS - AED

## ELEMENTOS DE DADOS ESTRUTURADOS

Existem dois tipos básicos de dados estruturados: numérico e categórico.

## Termos-chave para tipos de dados

### Contínuos

São os dados que podem assumir qualquer valor em um intervalo.  
Sinônimos: intervalo, flutuação, numérico.

### Discretos

Dados que podem assumir apenas valores inteiros, como contagens.  
Sinônimos: inteiro, contagem.

### Categóricos

Dados que podem assumir apenas um conjunto específico de valores representando um conjunto de possíveis categorias.  
Sinônimos: enumeração, enumerado, fatores, nominal, politômico.

### Binários

Um caso especial de dados categóricos com apenas duas categorias de valores (0/1, verdadeiro/falso).  
Sinônimos: dicotômico, lógico, indicador, booleano.

### Ordinais

Dado categórico que tem uma ordem explícita.  
Sinônimo: fator ordenado


## DADOS RETANGULARES

Dado retangular é basicamente uma matriz bidimensional em linhas indicando registros (casos) e colunas indicando carcterísticas (variáveis).

## Termos-chave para dados retangulares

### Quadro de dados

Os dados retangulares (como em um planilha) são a estrutura básica de dados para modelos estatísticos e aprendizado de máquina (machine learning).

### Características

Uma coluna na tabela costuma ser chamada de característica.  
Sinônimos: atributo, entrada, indicador, variável.

### Conclusão

Muitos projetos dee ciência de dados envolvem a previsão de uma conclusão - geralmente, uma conclusão sim/não. As *características* algumas vezes são usadas para prever a *conclusão* em um experimento ou estudo.  
Sinônimos: variável dependente, resposta, alvo, resultado.

### Registros

Uma linha na tabela costuma ser chamada de registro.  
Sinônimos: caso, exemplo, instância, observação, padrão, amostra.

### QUADRO DE DADOS E ÍNDICE

As tabelas de banco de dados tradicionalmente têm uma ou mais colunas designadas como um índice. Isso pode melhorar muito a eficiência em certas buscas SQL.

### ESTRUTURAS DE DADOS NÃO RETANGULARES

Ideias-chave  
A estrutura básica de dados na ciência de dados é uma matriz retangular, em que linhas são registros e colunas são variáveis (características).  
A terminologia pode ser confusa. Existem diversos sinônimos resultantes das diferentes disciplinas que contribuem com a ciência de dados (estatística, ciências da computação e tecnologia da informação).

## ESTIMATIVAS DE LOCALIZAÇÃO

Variáveis com dados de medição ou contagem podem ter milhares de valores diferentes. Um passo fundamental na exploração de seus dados é definir um 'valor típico' para cada característica (variável): uma estimativa de onde a maioria dos dados está localizada (ou seja, sua tendência central).

## Termos-chave para estimativas de localização

### Média

A soma de todos os valores, dividida pelo número de valores.  
Sinônimo: média aritmética simples.

### Média ponderada

A soma de todos os valores, multiplicada por um peso e dividida pela soma dos pesos.  
Sinônimo: média aritmética ponderada.

### Mediana

O valor que ocupa a posição central dos dados.  
Sinônimos: 52º percentil, 2º quartil.

### Mediana ponderada

Valor cuja posição está no centro da soma dos pesos, estando metade da soma antes e metade da soma depois desse dado.

### Média aparada

A média de todos os valores depois da exclusão de um número fixo de um número fixo de valores extremos.  
Sinônimo: média truncada.

### Robusto

Não sensível a valores extremos.  
Sinônimo: resistente.

### Outlier

Um valor de dados que é muito diferente da maioria dos dados.  
Sinônimo: valor extremo.


### MÉDIA

Forma de localização mais básica.

A fórmula da média é:

$$
Mean = \overline{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Onde $n$ se refere ao número total de registros ou observações. Em estatística ele é maiúsculo se for referente a uma população, e minúsculo se for referente a uma amostra da população. Em ciência de dados, essa distinção não é vital, então, pode ser visto das duas formas.

### Média aparada

Uma variação da média é a *média aparada*, a qual se calcula excluindo um número fixado de valores selecionados em cada ponta, e então tirando uma média dos valores restantes.

A fórmula da média aparada é:

```math
Trimmed\ mean = \overline{x}_{\text{aparada}} = \frac{\sum_{i=p+1}^{n-p} x_i}{n - 2p}
```

Onde:  
$`\overline{x}_{\text{aparada}}`$ é a média aparada.  
${𝑥}_{𝑖}$ são os valores ordenados.  
$𝑛$ é o número total de valores.  
$p$ é o número de valores a serem removidos de cada extremidade da lista ordenada.

Essa fórmula assume que os valores ${𝑥}_{𝑖}$ foram previamente ordenados em ordem crescente e que $p$ valores foram removidos das extremidades superior e inferior.

Uma média aparada elimina a influência dos valores extremos. Por exemplo, em uma competição internacional de mergulho, as notas máximas e mínimas dos cinco juízes são descartadas, e a nota final é a média dos três juízes restantes.

### Média ponderada

Outro tipo de média é a média ponderada, a qual se calcula pela multiplicação de cada valor de dado $`{x}_{i}`$, por um peso $`{w}_{i}`$ e dividindo sua somatória pela soma total de todos os pesos.

A fórmula da média ponderada é:

```math
Weighted\ mean = \overline{x}_{w} = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}
```

Existem duas razões principais para o uso da média ponderada:
- Alguns valores são intrisicamente mais variáveis que outros

### MEDIANA E ESTIMATIVAS ROBUSTAS

A *mediana* é a medida central em uma lista de dados **classificados**. Se houver um número par de valores de dados, o valor central é aquele que não está relamente no conjunto de dados, mas sim a média dos dois valores que dividem os valores classificados nas metades superior e inferior.

### Outliers

A mediana é chamada de estimativa *robusta* de localização, pois não é influenciada por *outliers* (casos extremos), que podem enviesar os resultados. Um outlier é qualquer valor que seja muito distante dos outros valores em um conjunto de dados. Se um outlier por si só não torna um valor de dado invélido ou errado, os outliers costumam ser o rsultado de erros de dados, como misturar dados de unidades diferentes (quilômetros versus metros) ou leituras ruins de um sensor. Quando os outliers são resultado de dados ruins, a média resultará em uma má estimativa de localização, enquanto a mediana ainda será válida. Em qualquer caso, os outliers devem ser identificados e costmam ser dignos de maior investigação.

A mediana não é a única estimativa de localização robusta. Na verdade, a média aparada é muito usada para evitar a influência de outliers.

## Ideias-chave

A métrica básica para localização é a média, mas esta pode ser sensível a valores extremos (outlier).  
Outras métricas (mediana, média aparada) são mais robustas.

## ESTIMATIVAS DE VARIABLIDADE

A localização é apenas uma dimensão na sumarização de uma característica. Uma segunda dimensao, *variabilidade*, também chamada de *dispersão*, mede se os valores de dados estão compactados ou espalhados. A variabilidade fica no centro da estatística: medindo, reduzindo, distinguindo variabilidade aleatória de real, identificando as diversas fontes de variabilidade real e tomando decisões em sua presença.

## Termos-chave para métricas de variabilidade

### Desvios

A diferença entre os valores observados e a estimativa de localização.

Sinônimos: erros, resíduos.

### Variância

A soma dos quadrados dos desvios da média, divididos por $n-1$, em que $n$ é o número de valores de dados.

Sinônimo: erro médio quadrático

### Desvio-padrão

A raiz quadrada da variância.

Sinônimos: norma l2, norma Euclidiana.

### Desvio absoluto médio

A média do valor absoluto dos desvios da média.

Sinônimos: norma l1, norma Manhattan.

### Desvio absoluto mediano da mediana

A mediana do valor absoluto dos desvios da mediana.

### Amplitude

A diferença entre o maior e o menor valor no conjunto de dados.

### Estatísticas ordinais

Métricas baseadas nos valores de dados classificados do menor ao maior.

Sinônimo: classificações

### Percentil

Valor tal que $P$ por cento dos valores assumam esse valor ou menos, e $(100-P)$ por cento assumam esse valor ou mais.

Sinônimo: quantil

### Amplitude interquartílica

A diferença entre o 75º percentil e o 25º percentil.

Sinônimo: IQR

Da mesma forma que há modos diferentes de medir a localização (média, mediana etc.), há também modos diferentes de medir a variabilidade.
