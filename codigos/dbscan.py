# Importação de bibliotecas necessárias
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN  # Algoritmo de clusterização baseado em densidade
from sklearn.preprocessing import StandardScaler  # Para normalização dos dados


def plot_clusters(X_scaled, clusters):
    """
    Cria um gráfico de dispersão mostrando os clusters e outliers detectados pelo DBSCAN.

    Parâmetros:
    X_scaled (array): Dados normalizados utilizados para o clustering
    clusters (array): Array com os rótulos de cluster para cada ponto (-1 = outlier)
    """
    plt.figure(figsize=(10, 6))
    # Cria o gráfico de dispersão colorido pelos rótulos dos clusters
    plt.scatter(
        X_scaled[:, 0],
        X_scaled[:, 1],
        c=clusters,  # Cores baseadas nos rótulos dos clusters
        cmap="viridis",  # Mapa de cores para diferenciação
        alpha=0.6,  # Transparência para melhor visualização
        s=20,
    )  # Tamanho dos pontos
    plt.title("DBSCAN: Clusters e Outliers (10% da base)")
    plt.xlabel("V1 (normalizado)")  # Feature V1 normalizada
    plt.ylabel("V2 (normalizado)")  # Feature V2 normalizada
    plt.colorbar(label="Cluster")  # Legenda da escala de cores
    plt.show()

    return

# Carregamento e preparação dos dados
df = pd.read_csv("https://raw.githubusercontent.com/GGB0T11/qp3_clustering/refs/heads/main/datasets/creditcard.csv")

# Seleção das features para análise (colunas V1 e V2)
X = df[["V1", "V2"]]  # Normalmente são componentes principais em datasets de fraude

# Pré-processamento dos dados
scaler = StandardScaler()  # Criando o objeto para normalização
X_scaled = scaler.fit_transform(X)  # Padroniza os dados (média=0, desvio padrão=1)

# Configuração e execução do DBSCAN
dbscan = DBSCAN(
    eps=0.9,  # Raio de vizinhança para considerar pontos como vizinhos
    min_samples=5,  # Número mínimo de pontos para formar um cluster denso
)
clusters = dbscan.fit_predict(X_scaled)  # Executa o algoritmo e retorna os rótulos

# Identificação e análise dos outliers (cluster -1)
outliers = df[clusters == -1]  # Filtra os pontos classificados como outliers

# Exibição dos resultados
print(f"Transações normais: {len(df) - len(outliers)}")  # Pontos dentro de clusters
print(f"Outliers detectados: {len(outliers)}")  # Possíveis fraudes detectadas
print(f"Fraudes reais: {df['Class'].sum()}")  # Fraudes confirmadas no dataset

# Visualização gráfica dos resultados
plot_clusters(X_scaled, clusters)
