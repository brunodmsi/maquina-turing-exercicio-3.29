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

  def loop(self, word):
    if self.result == "ACEITA":
      return "ACEITA"

    for letter in range(len(word)):
      if word[letter] == "a" and letter + 1 < len(word):
        if word[letter + 1] == "b" and letter + 2 < len(word):
          if word[letter + 2] == "a":
            return "LOOP"
          if word[letter + 2] == "b":
            continue

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