# Skrypt do tworzenia plików CSV do importu

## Instalacja

Pobrać skrypty generate_categories.py, generate_insert_product_query.py.

## Sposób użycia

Uruchomić skrypty, jako argument podać ścieżkę do pliku json z wynikami scrapowania, np.:
generate_categories.py scrap_results.json

Skrypt generate_categories.py generuje kategorie jako plik csv, który można importować przez sklep Prestashop.
Skrypt generate_insert_product_query.py generuje plik sql, który powinien zostać wykonany na bazie danych podpiętej do Prestashop (dot. bazy mysql).
