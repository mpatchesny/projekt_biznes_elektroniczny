# Webscraper do pobierania danych ze strony sklepu Ostrovit.com

## Instalacja

Pobrać skrypt webscraper.py i zainstalować wymagane biblioteki z requirements.txt

## Sposób użycia

Ściągnąc kod źródłowy głównych stron z odnośnikami do produktów na dysk lokalny. Uruchomić skrypt ze ściezkami do ściągniętych stron, np.:
webscraper.py ostrovit.com_pl_menu_dla-sportowcow-18756.html ostrovit.com_pl_menu_suplementy-diety-18755.html ostrovit.com_pl_menu_zywnosc-18757.html

Skrypt będzie zapisywał dane o produktach na bieżąco do pliku result.json, oraz pobierał zdjęcie główne każdego produktu do folderu images.

Skrypt remove_dups.py usuwa duplikaty z wyników działania webscraper.py i zapisuje w pliku results_no_dups.json.
