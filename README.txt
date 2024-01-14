# API Wikipedie

Tato aplikace Flask slouží jako jednoduché API pro vyhledávání ve Wikipedii. Umožňuje uživatelům vyhledávat informace o Wikipedii na konkrétní hledaný výraz ve zvoleném jazyce.

## Použití

### Instalace

1. Ujistěte se, že máte v systému nainstalován Python 3.11.
2. Nainstalujte požadované závislosti spuštěním:


### Spuštění aplikace

V terminálu spusťte následující příkaz:
python api.py

Ve výchozím nastavení bude aplikace přístupná na adrese `http://127.0.0.1:5000/`.

#### Parametry požadavku

- `search_term` (povinné): Hledaný výraz, který se má vyhledat ve Wikipedii.
- `lang` (nepovinné): Jazyk pro vyhledávání ve Wikipedii (výchozí je 'cs').

#### Odpověď

- Pokud je nalezen přesný článek, vrátí první odstavec článku se stavovým kódem 200.
- Pokud článek není nalezen, vrátí stav 404 s odpovědí JSON, která uvádí, že článek nebyl nalezen.
- Pokud hledaný výraz existuje v jiných článcích, vrátí stav 303 s přesměrováním na výsledky vyhledávání ve Wikipedii pro daný výraz.

## Zpracování chyb

- V případě vnitřní chyby serveru během zpracování vrátí odpověď JSON se stavovým kódem 500.

## Poznámka

- Tato aplikace používá k vyhledávání a získávání informací rozhraní API Wikipedie.

Translated with DeepL.com (free version)