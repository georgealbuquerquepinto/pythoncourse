'''
Created on 9 de mar de 2017

Obtém dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8

import string
import re
from src.Endereco import Endereco
from src.UnidadeDeSaude import UnidadeDeSaude
from src.NumeroTelefoneInvalido import NumeroTelefoneInvalido

BUFF_SIZE = 1024

def download_length(response, output, length):
  times = length/BUFF_SIZE
  if length % BUFF_SIZE > 0:
    times = times + 1
  for time in range(int(times)):
    output.write(response.read(BUFF_SIZE))
    print("Downloaded %d " % (((time * BUFF_SIZE)/100.0) * 100))

def download(response, output):
  total_downloaded = 0
  while True:
    data = response.read(BUFF_SIZE)
    total_downloaded += len(data)
    if not data:
      break
    output.write(data)
    print('Downloaded {bytes}'.format(bytes=total_downloaded))

def extract_filename(filename):
  filename = filename.split('.')
  del filename[len(filename) - 1]
  string = ""
  return string.join(filename)

def validarTelefone(telefone):
  if not re.match('\(\d{2}\)\d{8,9}$', telefone):
    raise NumeroTelefoneInvalido(1)

def read_data(path):
  fdata = open(path, 'rt', encoding="utf8")
  data = []
  for line in fdata:
    linedata = line.split(',')
    endereco = Endereco(linedata[5], linedata[6], linedata[7], linedata[8])
    unidade = UnidadeDeSaude(linedata[0] + linedata[1], linedata[2], linedata[3], linedata[9], linedata[10], linedata[11], endereco)
    
    data.append(unidade)
  fdata.close()
  return data

def create_cidcnes_index(data):
  dic = {}

  for d in data:
    dic[d[2]+d[3]] = d
  return dic

def create_index_from(source, columns_index, *args):
  dic = {}

  for s in source:
    key = ""
    for c in args:
      key += s[columns_index[c]]

    dic[key] = s
  return dic

def interpret(line_from_source, **kargs):
  for i in range(count(kargs)):
    line_from_source[i] = kargs[i](line_from_source[i])

  return line_from_source
