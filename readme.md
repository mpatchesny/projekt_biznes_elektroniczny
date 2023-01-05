# Projekt zaliczeniowy z przedmiotu Biznes elektroniczny

## Temat: sklep sportowy z odżywkami, zdrowną żywnością (produkty ze sklepu Ostrovit)

## Instalacja

### Wymagania wstępne

* Docker

### Budowanie obrazu

* skopiować repo
* uruchmić skrypt `substitute_environ_variables.py` z folderu scripts, z argumentem wskazującym na odpowiedni plik ze zmiennymi środowiskowym, np. dla instalacji lokalnie: local.env, dla instalacji w klastrze: cluster.env:\
`substitute_environ_variables.py ../config/local.env`
* w folderze głownym repo z konsoli uruchomić polecenie:\
`docker build . -t BE_187229_duzybiceps`
* jeżeli instalacja ma być w klastrze, trzeba przesłać zbudowany obraz do dockerhuba:\
TODO

### Uruchomienie/ instalacja krok po kroku

#### Uruchomienie lokalnie

* obraz powinien być w lokalnym rejestrze dockera, patrz [Budowanie obrazu](### Budowanie obrazu)
* aby uruchomić kontener, w folderze głównym repo w konsoli wpisać polecenie:\
```docker compose --env-file ./config/local.env up -d```
  * w trakcie tej operacji mogą zostać pobrane obrazy dockera: mysql i prestashop, jeżeli nie ma ich w rejestrze lokalnym
  * sklep będzie działał w pełni dopiero wtedy, kiedy kontener duzybiceps-init przestanie działać - jest to celowe, ten kontener ma za zadanie tylko przywrócić dane na bazie danych
* żeby odblokować SSL wejść w admin > Preferencje > włącz SSL + włącz SSL na wszystkich stronach

#### Uruchomienie w klastrze

* pobrać zbudowany wcześniej obraz z dockerhuba do odpowiedniego folderu:\
TODO
* wysłać obraz do rejestru zgodnie z tym, co jest w instrukcji
* uruchomić kontener w klastrze za pomocą polecenia:
sudo docker stack deploy -c docker-compose.yml BE_187229 --with-registry-auth
