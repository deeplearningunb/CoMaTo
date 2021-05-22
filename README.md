# CoMaTo

O CoMaTo é um projeto que utiliza aprendizado de máquina e redes neurais convolucionais para detectar possíveis
doenças existentes em plantas por meio de uma imagem de sua folha.

## Plantas disponíveis
  - Milho
  - Tomate

## Treinamento dos dados

Para o treinamento dos dados, dividiu-se o algoritmo nas seguintes etapas:
- Processamento dos dados
- Construção da Rede Neural Convolucional	
- Treino da Rede Neural Convolucional
- Teste e Visualização de resultados

Os treinamentos da rede neural convolucional se encontram na pasta `cnn` do repositório.

## Aplicativo

A interface de usuário foi desenvolvida utilizando a biblioteca Tkinter.

## Como executar o aplicativo

1º Passo: Clonar repositório

`git clone https://github.com/deeplearningunb/plant-disease/`

2º Passo: Instalar dependência (Necessário python 3.x)

`pip install -r requirements.txt`

3º Passo: Rodar o aplicativo

`python run.py`

## Membros

<table>
    <tr>
     <!-- Rafael -->
        <td align="center"><a href="https://github.com/RcleydsonR">
        <img src="https://avatars.githubusercontent.com/u/74625814?s=460&u=c3b77eaa289d931e139e184d494e0151956372a8&v=4" width="100px"/>
        <br /><sub><b>Rafael Cleydson</b><br><b>190019085</b></sub></a><br /></td>
    <!-- Thiago  -->
        <td align="center"><a href=https://github.com/thiagohdaqw><img src="https://avatars.githubusercontent.com/u/54081877?s=400&u=c1add0666adbf836efe972df83a854185477c2cc&v=4" width="100px"/><br /><sub><b>Thiago Paiva</b><br><b>190020377</sub></a><br/></td>
        </tr>
    </table>

## Dataset

Os dados foram retirados desses dois datasets:
* [PlantVillage](https://www.kaggle.com/abdallahalidev/plantvillage-dataset)
* [PlantDoc](https://github.com/pratikkayal/PlantDoc-Dataset)
