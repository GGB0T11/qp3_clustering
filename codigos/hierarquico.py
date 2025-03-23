# Importação de bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage  # Para dendrograma
from sklearn.cluster import AgglomerativeClustering  # Clustering hierárquico
from sklearn.decomposition import PCA  # Redução de dimensionalidade
from sklearn.preprocessing import StandardScaler  # Normalização de dados


def plot_dendograma(X_scaled):
    """
    Cria um dendrograma para visualizar a hierarquia de clusters.

    Parâmetros:
    X_scaled (array): Dados normalizados para análise
    """
    # Calcula a matriz de ligação usando o método de Ward (minimiza a variância intra-cluster)
    linked = linkage(X_scaled, method="ward")

    plt.figure(figsize=(10, 6))
    # Cria o dendrograma com configurações específicas
    dendrogram(
        linked,
        orientation="top",  # Orientação vertical
        truncate_mode="lastp",  # Trunca os últimos p clusters formados
        p=20,
    )  # Mostra apenas os últimos 20 clusters

    plt.title("Dendrograma: Hierarquia de Clusters de Vinho")
    plt.xlabel("Amostras")  # Índices das observações
    plt.ylabel("Distância")  # Distância entre clusters fusionados
    plt.show()

    return


def plot_clusters(X_scaled, cluster):
    """
    Visualiza os clusters em 2D usando PCA para redução de dimensionalidade.

    Parâmetros:
    X_scaled (array): Dados normalizados
    cluster (array): Rótulos dos clusters para cada observação
    """
    # Reduz para 2 componentes principais para visualização
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(X_scaled)  # Transforma os dados

    plt.figure(figsize=(10, 6))
    # Plota os pontos coloridos por cluster
    plt.scatter(
        data_pca[:, 0],
        data_pca[:, 1],
        c=cluster,  # Cores baseadas nos clusters
        cmap="viridis",  # Mapa de cores
        alpha=0.6,  # Transparência
        edgecolors="k",
    )  # Bordas pretas nos pontos

    plt.title("Clusters de Vinhos (PCA)")
    plt.xlabel("Componente Principal 1")  # Primeiro componente principal
    plt.ylabel("Componente Principal 2")  # Segundo componente principal
    plt.colorbar(label="Cluster")  # Legenda dos clusters
    plt.show()

    return


# Carregamento e preparação dos dados
df = pd.read_csv("https://raw.githubusercontent.com/GGB0T11/qp3_clustering/refs/heads/main/datasets/winequality-red.csv")  # Dataset de qualidade de vinhos

# Separação em features e target
X = df.drop("quality", axis=1)  # Todas as colunas exceto qualidade
y = df["quality"]  # Variável target (não usada no clustering)

# Pré-processamento dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Normalização (média=0, desvio=1)

# Criação e execução do modelo hierárquico
hierarquico = AgglomerativeClustering(
    n_clusters=3,  # Número final de clusters
    linkage="ward",  # Método de ligação (minimiza variância intra-cluster)
)
cluster = hierarquico.fit_predict(X_scaled)  # Executa o clustering

# Visualização dos resultados
plot_dendograma(X_scaled)  # Mostra hierarquia completa
plot_clusters(X_scaled, cluster)  # Mostra clusters em 2D
