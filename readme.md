# Projekt zaliczeniowy z przedmiotu Biznes elektroniczny

## Temat: sklep sportowy z odżywkami, zdrowną żywnością (produkty ze sklepu Ostrovit)

## Instalacja

### Wymagania wstępne

* Docker

### Instalacja krok po kroku

#### Budowanie obrazu

* skopiować repo
* w konsoli, w folderze scripts, uruchomić skrypt `substitute_environ_variables.py`
* w konsoli, w folderze głównym repo, uruchomić polecenie:
`docker build -t duzybiceps:latest .`

#### Instalacja lokalnie

* aby uruchomić kontener, w konsoli w folderze głównym repozytorium, wpisać polecenie:
```docker compose --env-file ./config/local.env up -d```
  * w trakcie tej operacji mogą zostać pobrane obrazy dockera: mysql i prestashop, jeżeli nie ma ich w rejestrze lokalnym
  * sklep będzie działał w pełni dopiero wtedy, kiedy kontener duzybiceps-init przestanie działać - jest to celowe, ten kontener ma za zadanie tylko przywrócić dane na bazie danych
* żeby odblokować SSL wejść w admin > Preferencje > włącz SSL + włącz SSL na wszystkich stronach

#### Instalacja w klastrze

TODO
