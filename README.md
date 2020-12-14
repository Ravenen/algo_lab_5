
# Deterministic state automate algorithm  
Task: implement **Knuth-Morris=Pratt** algorithm for searching the substring in string

#### Input data:
Input file `search.in` contains 2 rows:

 1. input string where search will be performed
 2. pattern string - substring which will be searched in input string
#### Output data:
Each row of output file `search.out` contains 2 numbers: start and end position in the string where the substring was found

##Algorithm
Алгоритм побудований на скінченному автоматі, в якому кожен стан відповідає співпадінню символу з шуканої підстрічки. Отримуємо стан автомата для кожного символа зі стрічки і коли стан відповідатиме довжині шуканої стрічки - ми знайшли співпадіння  
