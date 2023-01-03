# Projekt zaliczeniowy z przedmiotu Biznes elektroniczny

## Temat: sklep sportowy z odżywkami, zdrowną żywnością (produkty ze sklepu Ostrovit)

## Instalacja

### Wymagania wstępne

* Docker

### Instalacja krok po kroku

#### Instalacja lokalnie

* skopiować repo
* w konsoli przejść do repo
* przejść do scripts i uruchomić skrypt substitute_environ_variables.py
* z poziomu głównego folderu repo uruchomić docker compose:\
```docker compose --env-file ./config/local.env up -d```
  * w trakcie tej operacji mogą zostać pobrane obrazy dockera: mysql i prestashop, jeżeli nie ma ich w rejestrze lokalnym
  * sklep będzie działał w pełni dopiero wtedy, kiedy kontener duzybiceps-init przestanie działać - jest to celowe, ten kontener ma za zadanie tylko przywrócić dane na bazie danych
* uruchomić skrypt:
  * copy_selected_presta_folder.bat (wersja dla Windows), lub
  * copy_selected_presta_folder.sh (wersja dla Linux/ Unix)
* jeżeli podstrony sklepu nie działają, to trzeba nadać odpowiednie uprawnienia do folderów w kontenerze duzybiceps-presta:\
  `chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html`
* uruchomić polecenie `a2enmod ssl` na duzybiceps-presta i zrestartować kontener
* żeby odblokować SSL wejść w admin > Preferencje > włącz SSL + włącz SSL na wszystkich stronach

#### Instalacja w klastrze

TODO
