# Importação de bibliotecas
import matplotlib.pyplot as plt  # Para visualizações gráficas
import pandas as pd  # Para manipulação de dados
from sklearn.cluster import KMeans  # Algoritmo de clusterização
from sklearn.preprocessing import StandardScaler  # Para padronização dos dados


def plot_clusters(labels, centroids):
    """
    Plota os clusters e seus centroides em um gráfico 2D.

    Parâmetros:
    labels (array): Rótulos de cluster para cada ponto
    centroids (array): Coordenadas dos centroides dos clusters
    """
    plt.figure(figsize=(8, 6))

    # Plotagem dos pontos de dados coloridos por cluster
    plt.scatter(
        X_scaled[:, 0],  # Primeira característica (Renda Anual)
        X_scaled[:, 1],  # Segunda característica (Score de Gastos)
        c=labels,  # Cores baseadas nos rótulos dos clusters
        cmap="viridis",  # Mapa de cores para melhor distinção
        s=50,  # Tamanho dos pontos
        alpha=0.6,  # Transparência para melhor visualização
        edgecolors="k",  # Bordas pretas para destacar os pontos
    )

    # Plotagem dos centroides dos clusters
    plt.scatter(
        centroids[:, 0],  # Coordenada X dos centroides
        centroids[:, 1],  # Coordenada Y dos centroides
        c="red",  # Cor vermelha para destaque
        marker="X",  # Formato de marcador especial
        s=200,  # Tamanho aumentado
        label="Centroides",  # Legenda para identificação
    )

    # Configurações do gráfico
    plt.title("K-Means - Segmentação de Clientes")
    plt.xlabel("Renda Anual Padronizada")  # Eixo X padronizado
    plt.ylabel("Score de Gastos Padronizado")  # Eixo Y padronizado
    plt.legend()  # Exibe a legenda
    plt.grid(True, linestyle="--", alpha=0.4)  # Grid suave
    plt.show()


def plot_cotovelo(X):
    """
    Gera o gráfico do método do cotovelo para determinar o número ideal de clusters.

    Parâmetros:
    X (array): Conjunto de dados pré-processado
    """
    inertia = []  # Lista para armazenar as inércias
    k_values = range(1, 11)  # Valores de k de 1 a 10

    # Loop para calcular a inércia para cada valor de k
    for k in k_values:
        # Configuração do K-Means
        kmeans = KMeans(
            n_clusters=k,
            random_state=42,  # Semente para reproduzibilidade
            n_init=20,  # Número de inicializações diferentes
            max_iter=300,  # Número máximo de iterações
        ).fit(X)
        inertia.append(kmeans.inertia_)  # Armazena a inércia

    # Configuração do gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(k_values, inertia, marker="o", linestyle="--", markersize=8)

    # Destacar o ponto ótimo (cotovelo) encontrado
    plt.plot(5, inertia[4], "ro", markersize=10, label="Melhor K (k=5)")

    # Personalização do gráfico
    plt.title("Método do Cotovelo - Clientes de Shopping")
    plt.xlabel("Número de Clusters (k)")
    plt.ylabel("Inércia (Soma das Distâncias Quadradas)")
    plt.xticks(k_values)  # Mostra todos os valores de k no eixo
    plt.grid(True, linestyle="--", alpha=0.4)  # Grid estilo tracejado
    plt.legend()  # Exibe a legenda
    plt.show()


# Carregamento e preparação dos dados ------------------------------------------
url = "https://raw.githubusercontent.com/GGB0T11/qp3_clustering/refs/heads/main/datasets/Mall_Customers.csv"
df = pd.read_csv(url)  # Carrega o dataset direto da URL

# Seleciona e prepara as características relevantes:
# - Annual Income (k$): Renda anual em milhares de dólares
# - Spending Score (1-100): Pontuação de gastos do cliente
X = df[["Annual Income (k$)", "Spending Score (1-100)"]].values

# Pré-processamento dos dados:
scaler = StandardScaler()  # Cria o objeto para padronização
X_scaled = scaler.fit_transform(X)  # Padroniza os dados (média=0, desvio=1)

# Fluxo principal de execução --------------------------------------------------
# 1. Primeiro gera o gráfico do cotovelo para análise
plot_cotovelo(X_scaled)

# 2. Cria o modelo final com o melhor número de clusters identificado
kmeans = KMeans(
    n_clusters=5,  # Número ótimo identificado pelo método do cotovelo
    random_state=42,  # Garante resultados reproduzíveis
    n_init=20,  # Número de inicializações para evitar mínimos locais
)
kmeans.fit(X_scaled)  # Treina o modelo com os dados padronizados

# 3. Visualiza os clusters resultantes
plot_clusters(kmeans.labels_, kmeans.cluster_centers_)
