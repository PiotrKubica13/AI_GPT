# AI_GPT
Interview

## Opis projektu

Projekt to aplikacja, która za pomocą promptów do AI GPT przekształca zawartość pliku `Zadanie ...` zgodnie z podanymi wytycznymi. Dzięki tej aplikacji można automatycznie modyfikować treść danego pliku i zapisywać go w pliku 'artykul.html', wprowadzając zmiany sugerowane przez sztuczną inteligencję.

## Wymagania

Aby uruchomić aplikację, potrzebne są następujące technologie i języki programowania:

- Python 3.7 lub nowszy
- OpenAI GPT API
- Biblioteki Python: `openai`
- Plik HTML: `artykul.html`

Zaleca się także utworzenie wirtualnego środowiska dla izolacji zależności.

## Instalacja

1. **Skopiuj repozytorium**
   ```bash
   git clone https://github.com/PiotrKubica13/AI_GPT.git
   cd AI_GPT
   ```

2. **Utwórz wirtualne środowisko**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate   # Na systemach Unix
   myenv\Scripts\activate      # Na systemach Windows
   ```

3. **Zainstaluj potrzebne biblioteki**
   ```bash
   pip install python3
   pip install openai

W przypadku problemów lub pytań możesz skontaktować się z nami poprzez [email@example.com](mailto:email@example.com).



**   Wymaga posiadania klucza API do OpenAI GPT


## Instrukcje użycia

1. **Przygotuj plik `artykul.html`**
   Upewnij się, że plik `artykul.html` znajduje się w katalogu głównym projektu.

2. **Uruchom aplikację**
   ```bash
   python3 Prog_101.py
   ```
   **Modyfikacja zmiennej wytyczne**
   ```bash
   nano Prog_101.py
   ```
   "wytyczne" - zemienna okleśla instrukcje dla AI dotyczące modyfikacji treści.

3. **Wynik**
   Po wykonaniu aplikacji, zawartość `artykul.html` zostanie zaktualizowana zgodnie z podanymi wytycznymi.


## Uwagi

- Upewnij się, że masz prawidłowy dostęp do OpenAI API. Czas odpowiedzi może się różnić w zależności od złożoności promptu.
- Przed uruchomieniem aplikacji zaleca się zrobienie kopii zapasowej pliku `artykul.html`.
