from src.LocalizacaoGeografica import LocalizacaoGeografica
from src.Endereco import Endereco

class UnidadeDeSaude (LocalizacaoGeografica)
  def __init__ (self, codigo, dscEstFisAmb, dscAdapFisIdo, sitEquipamento, endereco, latitude, longitude):
    super(self.__class__, self).__init__(latitude, longitude)
    self._codigo = codigo
    self._dscEstFisAmb = dscEstFisAmb
    self._dscAdapFisIdo = dscAdapFisIdo
    self._sitEquipamentos = sitEquipamentos
    self._endereco = endereco

  def _get_codigo(self):
    return self._codigo

  def _set_codigo(self, _codigo):
    self._codigo = _codigo

  def _get_dscEstFisAmb(self):
    return self._dscEstFisAmb

  def _set_dscEstFisAmb(self, _dscEstFisAmb):
    self._dscEstFisAmb = _dscEstFisAmb

  def _get_dscAdapFisIdo(self):
    return self._dscAdapFisIdo

  def _set_dscAdapFisIdo(self, _dscAdapFisIdo):
    self._dscAdapFisIdo = _dscAdapFisIdo

  def _get_sisEquipamento(self):
    return self._sisEquipamento

  def _set_sisEquipamento(self, _sisEquipamento):
    self._sisEquipamento = _sisEquipamento

  def _get_endereco(self):
    return self._endereco

  def _set_endereco(self, _endereco):
    self._endereco = _endereco

