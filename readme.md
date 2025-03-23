# 📌 Conceitos Fundamentais
O **clustering** é uma técnica de aprendizado de máquina **não supervisionado** usada para identificar padrões ocultos em dados não rotulados. Ele agrupa elementos similares e separa os que possuem características distintas.

A base matemática do clustering envolve **métricas de distância**, como a **Euclidiana** e a de **Manhattan**, para medir a similaridade entre pontos. O objetivo central do clustering é:
- **Minimizar** a variabilidade dentro dos clusters.
- **Maximizar** a diferença entre eles.

---

# 🚀 Algoritmos de Clustering

## 🔹 K-Means (Baseado em Partição)
O **K-Means** é um dos algoritmos de clustering mais usados, baseado na divisão dos dados em **k grupos (partições)**. Cada grupo é representado pelo seu **centróide**, que é o ponto médio de todos os elementos do cluster.

### 🛠 Como Funciona?
1. Definir o **número de clusters k**.
2. Selecionar **k pontos aleatórios** como centroides iniciais.
3. Atribuir cada ponto ao centróide mais próximo (usando a **distância Euclidiana**).
4. Atualizar os centroides calculando a **média dos pontos** em cada cluster.
5. Repetir os passos **3 e 4** até que os centroides parem de mudar (**convergência**).

| ✅ **Vantagens** | ❌ **Desvantagens** |
| --- | --- |
| • Simples e eficiente para grandes conjuntos de dados | • Precisa definir k previamente |
| • Funciona bem em dados esféricos e bem separados | • Sensível a valores atípicos e clusters de formas irregulares |

---

## 🔹 DBSCAN (Baseado em Densidade)
O **DBSCAN** forma clusters com base na **densidade dos pontos** e pode **detectar outliers automaticamente**.

### 🛠 Como Funciona?
1. Define um **raio de vizinhança (eps)** e um **número mínimo de pontos (min_samples)**.
2. Identifica **pontos centrais** (com pelo menos **min_samples vizinhos** dentro de **eps**).
3. Expande clusters a partir desses **pontos centrais**, incluindo vizinhos próximos.
4. Pontos que não pertencem a nenhum cluster são marcados como **outliers (-1)**.

| ✅ **Vantagens** | ❌ **Desvantagens** |
| --- | --- |
| • Detecta clusters de formas irregulares | • Sensível à escolha de eps e min_samples |
| • Identifica outliers automaticamente | • Pode ter dificuldades em dados de alta dimensão |

---

## 🔹 Clustering Hierárquico
O **clustering hierárquico** cria uma estrutura de árvore (**dendrograma**) para organizar os dados. Ele pode ser de dois tipos:
- **Aglomerativo (Bottom-Up):** Começa com cada ponto separado e vai unindo os mais próximos até formar um único cluster.
- **Divisivo (Top-Down):** Começa com um único cluster e vai dividindo em subgrupos.

### 🛠 Como Funciona? (Método Aglomerativo)
1. Cada ponto começa como um **cluster individual**.
2. Os **clusters mais próximos** são mesclados com base na **distância**.
3. O processo continua até que reste **apenas um cluster** contendo todos os pontos.
4. Podemos **cortar o dendrograma** para obter o número desejado de clusters.

### 🛠 Como Funciona? (Método Divisivo)
1.  Todos os pontos pertencem a um único **cluster inicial** (a raiz do dendrograma).
2.  O cluster é dividido em **dois subgrupos**, baseando-se na maior dissimilaridade entre os pontos.
3. Cada subgrupo continua sendo dividido **recursivamente**, usando um critério de separação, como a **distância entre os pontos.**
4. O processo continua até que cada ponto seja um cluster individual ou até atingir um número específico de clusters.

| ✅ **Vantagens** | ❌ **Desvantagens** |
| --- | --- |
| • Não exige definir o número de clusters previamente | • Computacionalmente mais pesado que K-Means para grandes conjuntos de dados |
| • Gera um dendrograma útil para análise exploratória | • Não lida bem com outliers |

---

# 🔍 Aplicação Prática
## 🛒 Amazon (Segmentação de Clientes – K-Means)
A Amazon usa K-Means para segmentar clientes com base no histórico de compras, comportamento de navegação e preferências.
Isso permite recomendações personalizadas e ofertas direcionadas para diferentes perfis de consumidores.

## 🎵 Spotify (Recomendação de Músicas – K-Means / Hierárquico)
O Spotify usa clustering hierárquico e K-Means para agrupar usuários com gostos musicais semelhantes.
Além disso, agrupa músicas em clusters com base em características como ritmo, gênero e frequência sonora, criando playlists automáticas como Discover Weekly.

## 📺 Netflix (Recomendação de Filmes – K-Means / DBSCAN)
A Netflix utiliza clustering para identificar padrões de consumo e sugerir séries e filmes com base em usuários com gostos semelhantes.
Também agrupa vídeos com base em categorias ocultas (subgêneros, tipo de narrativa, atores, etc.).
