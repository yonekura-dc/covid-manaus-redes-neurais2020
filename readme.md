##Configurando o ambiente
###Instale o conda
[Site para instalação](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
Pode instalar o anaconda ou miniconda.

###Importe o ambiente padrão
Basta executar o seguinte comando no dir base do repositório.
    conda env create -f environment.yml

Para testar a instalação execute os comandos:
    conda activate covid
    python src/test_conda_env.py

###Utilizando o Jupyter-lab
Para habilitar o env como um kernel do Jupyter, basta executar:
    python -m ipykernel install --user --name covid --display-name "Python (covid)"

Abra o jupyter-lab (so precisa escrever jupyter-lab no console), ele vai abrir o seu navegador padrão. E execute o
notebook test\_jupyter.ipynb

