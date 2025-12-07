#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    if isinstance(value, str):
      self._value = value
    else:
      self._value = ""

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value

  def is_sentence(self):
    return isinstance(self._value, str) and self._value.endswith('.')

  def is_question(self):
    return isinstance(self._value, str) and self._value.endswith('?')

  def is_exclamation(self):
    return isinstance(self._value, str) and self._value.endswith('!')

  def count_sentences(self):
    if not isinstance(self._value, str) or self._value == "":
      return 0
    # Count groups of sentence-ending punctuation (., ?, !) as sentences
    matches = re.findall(r'[.?!]+', self._value)
    return len(matches)
