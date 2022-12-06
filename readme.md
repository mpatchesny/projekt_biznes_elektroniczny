# Projekt zaliczeniowy z przedmiotu Biznes elektroniczny

## Temat: sklep sportowy z odżywkami, zdrowną żywnością (produkty ze sklepu Ostrovit)

## Instalacja

### Wymagania wstępne

* Docker

### Instalacja krok po kroku

* skopiować repo
* w konsoli przejść do repo i uruchomić docker compose:
```docker compose up -d```
  * w trakcie tej operacji mogą zostać pobrane obrazy dockera: mysql i prestashop, jeżeli nie ma ich w rejestrze lokalnym
  * sklep będzie działał w pełni dopiero wtedy, kiedy kontener duzybiceps-init przestanie działać - jest to celowe, ten kontener ma za zadanie tylko przywrócić dane na bazie danych
* uruchomić skrypt:
  * copy_selected_presta_folder.bat (wersja dla Windows), lub
  * copy_selected_presta_folder.sh (wersja dla Linux/ Unix)
  * jeżeli podstrony sklepu nie działają, to trzeba nadać odpowiednie uprawnienia do folderów w kontenerze duzybiceps-presta:
  chmod +777 -r /var/www/html
