**Dockerfile** представлен непосредственно в `Dockerfile`, простой echo-server написан на Python и представлен в `simple_api.py`.
Команды, которые были использованы для пуша образа в регистри
```
docker login # логинимся
docker build -t flpfl/cloud_echo_server:latest -f Dockerfile . # собираем образ
docker push flpfl/cloud_echo_server:latest # пушим образ в регистри
```
