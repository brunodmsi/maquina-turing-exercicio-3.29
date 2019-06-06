# -*- coding: utf-8 -*-

class Turing():
  def __init__(self):
    self.result = ""

  def entry(self, word):
    self.result = self.accept(word)

    self.result = self.loop(word)

    return self.result

  def accept(self, word):
    if word[0] != "a":
      return "REJEITADA"
    
    if word[len(word) - 1] == "a":
      return "REJEITADA"

    for letter in range(len(word)):
      if word[letter] == "a":
        if word[letter + 1] != "b":
          return "REJEITADA"

    return "ACEITA"

  def getNextA(self, word, letter):
    original = letter

    if letter + 1 == len(word):
      return "LOOP"
    else:
      letter = letter + 1

    if word[letter] == "a":
      return "REJEITADA"

    found_a = False
    while(found_a == False):
      if word[letter] == "a":
        if letter + 1 < len(word) and word[letter + 1] == "a":
          return "REJEITADA"

        found_a = True
        return letter               

      letter = letter + 1

  def loop(self, word):
    if self.result == "ACEITA":
      return "ACEITA"

    tst = ""

    for letter in range(len(word)):
      if word[letter] == "a":
        pos = self.getNextA(word, letter)
        
        if pos == "REJEITADA":
          return "REJEITADA"
        
        letter = pos

        tst = "LOOP"

    if tst == "LOOP":
      return "LOOP"
    return "REJEITADA"

def main():
  print "ACEITA(M) = {w | w inicia com a e, apos cada a existe pelo menos um b}"
  print "LOOP(M) = {w | w ∉ ACEITA(M) e existe pelo menos um b entre dois a}"
  print "REJEITA(M) = {a, b}* - (ACEITA(M) ∪ LOOP(M))"

  word = raw_input("Entre a palavra -> ")
  ans = Turing().entry(word)
  print ans

if __name__ == "__main__":
  main()
