# PDV-Challange 

## Sobre
Este repositório contém uma resolução para o teste da [ZXVentures](https://github.com/ZXVentures) para o [desafio backend](https://github.com/ZXVentures/code-challenge/blob/master/backend.md)

## Dependências
* python3+
* MongoDB 3.6
* python-pip


## Instalação
1. Instale as dependências
    ```shell
    pip install -r requirements.txt
    ```
    
2. Faça a migração do banco de dados:
    ```shell
    python ./pdv_challenge/migrate/db-migrate.py
    ```
    **OBS: Veja a confiração de conexão com MongoDB em (./pdv_challenge/settings/config.py)**
    
3. Adicione as variáveis de ambiente
    ```shell
    export FLASK_APP=./pdv_challenge/http/index.py
    ```
    
    Por padrão o servidor subirá em modo de produção, mude a variável de ambinete **FLASK_ENV** para trocar para desenvolvimento
    ```shell
    export FLASK_ENV=development
    ```
    
4. Inicie o servidor:
    ```shell
    python -m flask run -h 0.0.0.0
    ```
    
    
## Testando
  * Buscar PDV por ID
      ```shell
      curl -X GET http://localhost:5000/pdv/<ID>
      ```      
      
  * Buscar PDV mais próximo ou dentro por latitude e longitude
      ```shell
      curl -X GET 'http://localhost:5000/search?lat=<LAT>&lng=<LON>
      ```
       
  * Criando novo PDV
      ```shell
      curl -X POST http://localhost:5000/pdv -H \ 
      'Content-Type: application/json' \
      -d '<JSON>'
      ```


## Docker
Toda a aplicação também está pronta para rodar em containers docker

   1. Edite o arquivo de configuração do MongoDB em **./pdv_challenge/settings/config.py**
       ```python
      MONGO_SERVER = 'mongo'
        ```

  2. Crie os containers
        ```shell
        docker-compose build
        ```
        
  3. Suba os containers
        ```shell
        docker-compose up
        ```
        
  4. Faça a migração dos dados para MongoDB
        ```shell
        docker-compose exec web bash -c "python3 ./pdv_challenge/migrate/db-migrate.py"
        ```
        
  5. Teste como nos exemplos acima.
