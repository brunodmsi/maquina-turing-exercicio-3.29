# Exercicio 3.29 - Teoria da Computacao. Maquinas Universais e Computabilidade
Elabore uma Maquina de Turing M sobre o alfabeto {a, b} tal que:  
```
ACEITA(M) = {w | w inicia com a e, apos cada a existe pelo menos um b}  
LOOP(M) = {w | w ∉ ACEITA(M) e existe pelo menos um b entre dois a}  
REJEITA(M) = {a, b}* - (ACEITA(M) ∪ LOOP(M))  
```
  
Para rodar use o Python 2.7 com o comando:
```
python2 main.py
```
  
Tambem tem um arquivo para ser aberto no JFLAP com a resolucao da tal questao
