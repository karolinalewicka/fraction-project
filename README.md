# fraction-project

Treść projektu:\
\
Specyfikacja wejścia/wyjścia:\
\
Wejście: \
W każdej linii wejścia program otrzyma jedno działanie (dodawanie/odejmowanie/mnozenie/dzielenie) do wykonania. Każda linia będzie zapisana w postaci:\
• liczba operator ułamek\
• ułamek operator liczba\
• ułamek operator ułamek\
gdzie:\
• liczba jest liczbą całkowitą,\
• operator to jeden ze znaków: + - * :\
• ułamek jest zapisany jako: liczba/liczba\
• liczba, operator, ułamek oddzielone są od siebie jednym znakiem spacji\

Wyjście: \
Jedyne informacje jakie program wypisuje to ułamek lub informacja o błędzie.\
Ułamek będący wynikiem dzialania, musi być zapisany w postaci nieskracalnej. Format zapisu ułamka: liczba/liczba\
W przypadku, gdy:\
• użytkownik wprowadzi błędne dane,\
• użytkownik wprowadzi dane w niepoprawnym formacie,\
• wynikowego ułamka nie da się zapisać\
program musi wypisać napis 'BLAD'\

Szczegóły implementacyjne:\

1. Zdefiniuj klasę Fraction będącą reprezentacją ułamka, klasa to musi posiadać:\
• funkcję __init__ przyjmującą licznik i mianownik ułamka,\
• własny operator + (z użyciem metody magicznej),\
• własny operator - (z użyciem metody magicznej),\
• własny operator * (z użyciem metody magicznej),\
• własny operator / (z użyciem metody magicznej),\
• własną funkcję __str__ zwracającą napis bedący tekstową reprezentacją ułamka.\
Wszelkie działania na ułamkach powinny być realizowane za pomocą obiektów tej klasy.\
Klasa ta powinna przechowywać ułamki w postaci nieskracalnej.\

2. Za pomocą mechanizmu wyjątków obsłuż EOFError sygnalizujący koniec danych wejściowych.\
