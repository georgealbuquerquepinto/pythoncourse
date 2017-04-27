class NumeroTelefoneInvalido(Exception):
  def __init__(self, numero, mensagem = "Numero de telefone invalido"):
    self._numero = numero
    self._mensagem = mensagem

  def _get_numero(self):
    return self._numero

  def _set_mensagem(self, _mensagem):
    self._mensagem = _mensagem