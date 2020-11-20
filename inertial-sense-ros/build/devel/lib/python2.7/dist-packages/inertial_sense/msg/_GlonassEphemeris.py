# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from inertial_sense/GlonassEphemeris.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import inertial_sense.msg

class GlonassEphemeris(genpy.Message):
  _md5sum = "d6e50080404485ddd899caa0ddef8be5"
  _type = "inertial_sense/GlonassEphemeris"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 sat 	# satellite number 
int32 iode 	# IODE (0-6 bit of tb field) 
int32 frq 	# satellite frequency number 
int32 svh 	# satellite health 
int32 sva 	# satellite accuracy 
int32 age 	# satellite age of operation 
GTime toe 	# epoch of epherides (gpst) 
GTime tof 	# message frame time (gpst) 
float64[3] pos 	# satellite position (ecef) (m) 
float64[3] vel 	# satellite velocity (ecef) (m/s) 
float64[3] acc 	# satellite acceleration (ecef) (m/s^2) 
float64 taun 	# SV clock bias (s) 
float64 gamn 	# relative freq bias 
float64 dtaun 	# delay between L1 and L2 (s) 
================================================================================
MSG: inertial_sense/GTime
int64 time
float64 sec"""
  __slots__ = ['sat','iode','frq','svh','sva','age','toe','tof','pos','vel','acc','taun','gamn','dtaun']
  _slot_types = ['int32','int32','int32','int32','int32','int32','inertial_sense/GTime','inertial_sense/GTime','float64[3]','float64[3]','float64[3]','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sat,iode,frq,svh,sva,age,toe,tof,pos,vel,acc,taun,gamn,dtaun

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GlonassEphemeris, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sat is None:
        self.sat = 0
      if self.iode is None:
        self.iode = 0
      if self.frq is None:
        self.frq = 0
      if self.svh is None:
        self.svh = 0
      if self.sva is None:
        self.sva = 0
      if self.age is None:
        self.age = 0
      if self.toe is None:
        self.toe = inertial_sense.msg.GTime()
      if self.tof is None:
        self.tof = inertial_sense.msg.GTime()
      if self.pos is None:
        self.pos = [0.] * 3
      if self.vel is None:
        self.vel = [0.] * 3
      if self.acc is None:
        self.acc = [0.] * 3
      if self.taun is None:
        self.taun = 0.
      if self.gamn is None:
        self.gamn = 0.
      if self.dtaun is None:
        self.dtaun = 0.
    else:
      self.sat = 0
      self.iode = 0
      self.frq = 0
      self.svh = 0
      self.sva = 0
      self.age = 0
      self.toe = inertial_sense.msg.GTime()
      self.tof = inertial_sense.msg.GTime()
      self.pos = [0.] * 3
      self.vel = [0.] * 3
      self.acc = [0.] * 3
      self.taun = 0.
      self.gamn = 0.
      self.dtaun = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6iqdqd().pack(_x.sat, _x.iode, _x.frq, _x.svh, _x.sva, _x.age, _x.toe.time, _x.toe.sec, _x.tof.time, _x.tof.sec))
      buff.write(_get_struct_3d().pack(*self.pos))
      buff.write(_get_struct_3d().pack(*self.vel))
      buff.write(_get_struct_3d().pack(*self.acc))
      _x = self
      buff.write(_get_struct_3d().pack(_x.taun, _x.gamn, _x.dtaun))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.toe is None:
        self.toe = inertial_sense.msg.GTime()
      if self.tof is None:
        self.tof = inertial_sense.msg.GTime()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.sat, _x.iode, _x.frq, _x.svh, _x.sva, _x.age, _x.toe.time, _x.toe.sec, _x.tof.time, _x.tof.sec,) = _get_struct_6iqdqd().unpack(str[start:end])
      start = end
      end += 24
      self.pos = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 24
      self.vel = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 24
      self.acc = _get_struct_3d().unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.taun, _x.gamn, _x.dtaun,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6iqdqd().pack(_x.sat, _x.iode, _x.frq, _x.svh, _x.sva, _x.age, _x.toe.time, _x.toe.sec, _x.tof.time, _x.tof.sec))
      buff.write(self.pos.tostring())
      buff.write(self.vel.tostring())
      buff.write(self.acc.tostring())
      _x = self
      buff.write(_get_struct_3d().pack(_x.taun, _x.gamn, _x.dtaun))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.toe is None:
        self.toe = inertial_sense.msg.GTime()
      if self.tof is None:
        self.tof = inertial_sense.msg.GTime()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.sat, _x.iode, _x.frq, _x.svh, _x.sva, _x.age, _x.toe.time, _x.toe.sec, _x.tof.time, _x.tof.sec,) = _get_struct_6iqdqd().unpack(str[start:end])
      start = end
      end += 24
      self.pos = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      start = end
      end += 24
      self.vel = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      start = end
      end += 24
      self.acc = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      _x = self
      start = end
      end += 24
      (_x.taun, _x.gamn, _x.dtaun,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_6iqdqd = None
def _get_struct_6iqdqd():
    global _struct_6iqdqd
    if _struct_6iqdqd is None:
        _struct_6iqdqd = struct.Struct("<6iqdqd")
    return _struct_6iqdqd
