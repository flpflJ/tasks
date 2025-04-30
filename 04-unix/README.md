# Ответ к задаче "Запереть контейнер изнутри"
## Способ №1
 Способ заключается в том, что мы стираем список DNS-серверов для разыменования доменных имен.
```
 apt-get update # Проверяем, что команда работает
 echo > /etc/resolv.conf # стираем список DNS
 apt-get update # наблюдаем в выводе игнорирования и ошибки.
```
![resolу](https://github.com/flpflJ/tasks/blob/main/04-unix/Screenshot%202025-04-30%20195611.png)
## Способ №2
 Способ заключается в том, что мы меняем nsswitch.conf, ломая список источников служб доменных имен.
```
apt-get update # Проверяем, что команда работает
echo "hosts: files" > /etc/nsswitch.conf
apt-get update # наблюдаем в выводе игнорирования и ошибки.
``` 
![nss](https://github.com/flpflJ/tasks/blob/main/04-unix/Screenshot%202025-04-30%20195747.png)
