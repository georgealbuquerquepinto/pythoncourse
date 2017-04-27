class LocalizacaoGeografica
  def __init__ (self, latitude, longitude):
    self._latitude = latitude
    self._longitude = longitude

  def _get_latitude(self):
    return self._latitude

  def _set_latitude(self, _latitude):
    self._latitude = _latitude

  def _get_longitude(self):
    return self._longitude

  def _set_longitude(self, _longitude):
    self._longitude = _longitude

