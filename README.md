
# Integrando OpenWeatherMap API com aplicação FastAPI

Neste projeto foi desenvolvido uma aplicação web local 
por meio do FastAPI e utilizado a API da OpenWeatherMap 
para requisitar temperatura e umidade de uma lista predeterminada 
de cidades identificadas por seu ID.

#### API utilizada

- [OpenWeatherMap](https://openweathermap.org/)

## Informações

Os dados climáticos obtidos pelas requisições serão salvos
em um arquivo JSON na pasta data.

Para replicação do projeto em qualquer máquina 
foi criado o arquivo Dockerfile. 
Para isto é necessario ter o Docker instalado em sua máquina.

A descrição dos passos a serem seguidos se encontra logo abaixo.

### Deployment
Copie e cole os scripts em destaque de acordo com as instruções.
Deve-se usar o terminal shell.

1 - Crie uma pasta em algum diretório de preferência

2 - Navegue pelo terminal até a pasta criada e execute o script
para baixar o repositório:
```bash
git clone https://github.com/apoloferreira/weather-api.git
```
3 - Entre na pasta pelo terminal

4 - Copie, cole e execute os comandos:
```bash
docker build -t apolo-image .
```
```bash
docker run -p 8888:8888 --name app-apolo apolo-image
```
*fique a vontade para mudar a porta

5 - O conteiner já está funcionando.
Agora abra uma aba do navegador e cole o caminho:
```bash
127.0.0.1:8888/home
```

6 - Pronto, tudo ok.
Faça os testes a vontade.

* Botão Enviar: faz a requisição das condições climáticas e salva em um aquivo json.
- Botão Verificar: informa a porcentagem concluida da requisição digitada.

7 - Para finalizar a imagem docker, abra outro terminal e execute:
```bash
docker kill app-apolo
```
