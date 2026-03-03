Neste projeto, desenvolvi um pipeline completo de ETL (Extract, Transform, Load) para processar e limpar dados simulados de vendas, utilizando Python e a biblioteca Pandas. O objetivo foi transformar uma base de dados bruta e inconsistente em uma base limpa e pronta para análise.



O pipeline foi dividido em três etapas principais:



Extract (Extração): Leitura dos dados brutos a partir de um arquivo CSV (vendas_brutas.csv).


Transform (Transformação): Utilização do Pandas para realizar a limpeza dos dados. Foram removidas as linhas com valores nulos (NaN) nas colunas de cliente e produto. Em seguida, os nomes dos produtos foram padronizados para letras maiúsculas e foi criada uma nova coluna calculada (valor_total), multiplicando a quantidade pelo preço unitário.


Load (Carga): Exportação do DataFrame limpo e tratado para um novo arquivo (vendas_limpas.csv), garantindo a persistência dos dados para uso futuro.
