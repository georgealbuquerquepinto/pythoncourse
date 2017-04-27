class Endereco:
  def __init__ (self, logradouro, bairro, cidade, telefone):
    self._logradouro = logradouro
    self._bairro     = bairro
    self._cidade     = cidade
    self._telefone   = telefone

  def _get_logradouro(self):
    return self._logradouro

  def _set_logradouro(self, _logradouro):
    self._logradouro = _logradouro

  def _get_bairro(self):
    return self._bairro

  def _set_bairro(self, _bairro):
    self._bairro = _bairro

  def _get_cidade(self):
    return self._cidade

  def _set_cidade(self, _cidade):
    self._cidade = _cidade

  def _get_telefone(self):
    return self._telefone

  def _set_telefone(self, _telefone):
    self._telefone = _telefone