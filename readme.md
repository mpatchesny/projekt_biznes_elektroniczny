# Projekt zaliczeniowy z przedmiotu Biznes elektroniczny

## Temat: sklep sportowy z odżywkami, zdrowną żywnością (produkty ze sklepu Ostrovit)

## Instalacja

### Wymagania wstępne

* Docker

### Budowanie obrazu

* skopiować repo
* uruchmić skrypt `substitute_environ_variables.py` z folderu scripts, z argumentem wskazującym na odpowiedni plik ze zmiennymi środowiskowym, np. dla uruchomienia lokalnie: local.env, dla uruchomienia w klastrze: cluster.env:\
`substitute_environ_variables.py ../config/local.env`
* w folderze głownym repo z konsoli uruchomić polecenie:\
`docker build -t <nazwa_obrazu> .`

### Uruchomienie/ instalacja krok po kroku

#### Uruchomienie lokalnie

* obraz powinien być w lokalnym rejestrze dockera, patrz: [Budowanie obrazu](#budowanie-obrazu)
* aby uruchomić kontener, w folderze głównym repo w konsoli wpisać polecenie:\
```docker compose --env-file ./config/local.env up -d```
  * w trakcie tej operacji mogą zostać pobrane obrazy dockera: mysql i prestashop, jeżeli nie ma ich w rejestrze lokalnym
  * sklep będzie działał w pełni dopiero wtedy, kiedy kontener duzybiceps-init przestanie działać - jest to celowe, ten kontener ma za zadanie tylko przywrócić dane na bazie danych
* żeby odblokować SSL wejść w admin > Preferencje > włącz SSL + włącz SSL na wszystkich stronach

#### Uruchomienie w klastrze

* zbudować obraz lokalnie, patrz: [Budowanie obrazu](#budowanie-obrazu)
* wysłać obraz do rejestru zgodnie z tym, co jest w instrukcji
* uruchomić kontener w klastrze za pomocą polecenia:
```sudo docker stack deploy --env-file ./config/cluster.env -c docker-compose-cluster.yml be_187229 --with-registry-auth```
