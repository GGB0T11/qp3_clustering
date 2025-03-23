## 1. Conceitos – O que é Clustering?  

Clustering é uma técnica de aprendizado de máquina usada para agrupar dados semelhantes sem a necessidade de rótulos prévios. Isso significa que ele descobre padrões nos dados sem que haja uma categorização definida. O objetivo do clustering é organizar os dados de forma que pontos dentro do mesmo grupo sejam mais parecidos entre si do que com pontos de outros grupos.  

O clustering utiliza medidas matemáticas para determinar a similaridade entre os pontos. As mais comuns são:  

* **Distância Euclidiana**: Mede a distância direta entre dois pontos no espaço.  
* **Distância de Manhattan**: Mede a soma das diferenças absolutas entre as coordenadas dos pontos.  

Essa técnica é útil para diversas aplicações, como segmentação de clientes, reconhecimento de padrões e recomendação de produtos.  

---

## 2. K-Means – O que é, Vantagens e Desvantagens  

O K-Means é um dos métodos mais populares de clustering e funciona dividindo os dados em um número fixo de grupos chamados clusters. Cada cluster é representado por um ponto central chamado centróide, que é a média dos pontos do grupo.  

### Como o K-Means funciona  

1. Escolhe-se um número de clusters, chamado **k**.  
2. Selecionam-se **k** pontos aleatórios como centroides iniciais.  
3. Cada ponto dos dados é atribuído ao centróide mais próximo.  
4. Os centroides são recalculados com base na média dos pontos atribuídos a cada grupo.  
5. O processo continua até que os centroides parem de mudar ou o algoritmo atinja um número máximo de iterações.  

### Vantagens  

* Rápido e eficiente para grandes conjuntos de dados.  
* Fácil de entender e implementar.  
* Funciona bem quando os clusters são bem separados e têm forma esférica.  

### Desvantagens  

* Precisa definir o número de clusters antes da execução.  
* Sensível a valores extremos (outliers), que podem distorcer os resultados.  
* Não funciona bem para dados que formam clusters de formatos irregulares.  

---

## 3. DBSCAN – O que é, Vantagens e Desvantagens  

O DBSCAN é um algoritmo baseado em densidade. Ele forma clusters onde há uma alta concentração de pontos e identifica pontos isolados como outliers. Diferente do K-Means, ele não exige a definição do número de clusters previamente.  

### Como o DBSCAN funciona  

1. Define-se um **raio de vizinhança** (chamado de **eps**) e um **número mínimo de pontos** para um grupo ser considerado um cluster.  
2. Identifica-se os **pontos centrais**, que possuem um número suficiente de vizinhos dentro do raio.  
3. Os clusters são formados conectando os pontos centrais e seus vizinhos.  
4. Pontos isolados, que não pertencem a nenhum cluster, são considerados **outliers**.  

### Vantagens  

* Não precisa definir o número de clusters antecipadamente.  
* Identifica clusters de diferentes formatos, mesmo se forem irregulares.  
* Detecta automaticamente pontos que não pertencem a nenhum grupo (outliers).  

### Desvantagens  

* A escolha dos parâmetros **eps** e **número mínimo de pontos** pode ser difícil e afetar os resultados.  
* Em conjuntos de dados muito grandes e de alta dimensão, o algoritmo pode ser lento.  

---

## 4. Clustering Hierárquico – O que é, Vantagens e Desvantagens  

O clustering hierárquico organiza os dados em uma estrutura de árvore chamada dendrograma. Ele pode ser feito de duas formas:  

* **Aglomerativo (Bottom-Up)**: Começa com cada ponto como um cluster separado e vai unindo os mais próximos até formar um único cluster.  
* **Divisivo (Top-Down)**: Começa com todos os pontos em um único cluster e vai dividindo-os progressivamente até que cada ponto esteja separado.  

### Como funciona o Clustering Hierárquico Aglomerativo  

1. Cada ponto começa como um cluster separado.  
2. Os dois clusters mais próximos são mesclados.  
3. O processo se repete até restar apenas um cluster contendo todos os pontos.  
4. O dendrograma pode ser cortado em diferentes níveis para obter diferentes números de clusters.  

### Vantagens  

* Não exige a definição do número de clusters antecipadamente.  
* O dendrograma fornece uma representação visual útil para análise.  
* Funciona bem para conjuntos de dados pequenos ou médios.  

### Desvantagens  

* Pode ser lento para conjuntos de dados grandes, pois compara todos os pontos entre si.  
* Pode ser difícil definir o ponto ideal para cortar o dendrograma e escolher o número de clusters.  
* Sensível a outliers, que podem distorcer a formação dos clusters.  

---

## 5. Aplicações Práticas – Exemplos de Empresas  

### Amazon – Segmentação de Clientes  

A Amazon usa clustering para segmentar clientes com base no histórico de compras. Isso permite oferecer recomendações personalizadas, sugerindo produtos que pessoas com hábitos de compra semelhantes adquiriram.  

### Spotify – Recomendação de Músicas  

O Spotify usa clustering para agrupar usuários com gostos musicais parecidos. Ele também agrupa músicas com características semelhantes, ajudando a criar playlists personalizadas.  

### Netflix – Sugestão de Filmes e Séries  

A Netflix analisa padrões de visualização dos usuários e agrupa pessoas com interesses semelhantes para sugerir séries e filmes que possam interessar a cada um.  

### Google Maps – Análise de Tráfego  

O Google Maps usa clustering para identificar áreas de congestionamento no trânsito e sugerir rotas alternativas.  

### Redes Sociais – Agrupamento de Interesses  

Facebook, Instagram e Twitter usam clustering para identificar comunidades e grupos de usuários com interesses semelhantes, ajudando a personalizar o feed e as recomendações de conteúdo.  

---
