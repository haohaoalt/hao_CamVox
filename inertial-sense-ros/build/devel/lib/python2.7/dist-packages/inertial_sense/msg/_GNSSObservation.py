# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from inertial_sense/GNSSObservation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import inertial_sense.msg
import std_msgs.msg

class GNSSObservation(genpy.Message):
  _md5sum = "f652831660ce8b4781ba3cf83655ca76"
  _type = "inertial_sense/GNSSObservation"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
GTime time              # time of observation
uint8 sat 		# satellite number
uint8 rcv 		# receiver number
uint8 SNR 		# Signal Strength (0.25 dBHz)
uint8 LLI 		# Loss-of-Lock Indicator (bit1=loss-of-lock, bit2=half-cycle-invalid)
uint8 code 		# code indicator (BeiDou: CODE_L1I, Other: CODE_L1C )
uint8 qualL 	# Estimated carrier phase measurement standard deviation (0.004 cycles)
uint8 qualP 	# Estimated pseudorange measurement standard deviation (0.01 m)
float64 L      	# observation data carrier-phase (cycle)
float64 P      	# observation data pseudorange (m)
float32 D      	# observation data doppler frequency (0.002 Hz)
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: inertial_sense/GTime
int64 time
float64 sec"""
  __slots__ = ['header','time','sat','rcv','SNR','LLI','code','qualL','qualP','L','P','D']
  _slot_types = ['std_msgs/Header','inertial_sense/GTime','uint8','uint8','uint8','uint8','uint8','uint8','uint8','float64','float64','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time,sat,rcv,SNR,LLI,code,qualL,qualP,L,P,D

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GNSSObservation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time is None:
        self.time = inertial_sense.msg.GTime()
      if self.sat is None:
        self.sat = 0
      if self.rcv is None:
        self.rcv = 0
      if self.SNR is None:
        self.SNR = 0
      if self.LLI is None:
        self.LLI = 0
      if self.code is None:
        self.code = 0
      if self.qualL is None:
        self.qualL = 0
      if self.qualP is None:
        self.qualP = 0
      if self.L is None:
        self.L = 0.
      if self.P is None:
        self.P = 0.
      if self.D is None:
        self.D = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.time = inertial_sense.msg.GTime()
      self.sat = 0
      self.rcv = 0
      self.SNR = 0
      self.LLI = 0
      self.code = 0
      self.qualL = 0
      self.qualP = 0
      self.L = 0.
      self.P = 0.
      self.D = 0.

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_qd7B2df().pack(_x.time.time, _x.time.sec, _x.sat, _x.rcv, _x.SNR, _x.LLI, _x.code, _x.qualL, _x.qualP, _x.L, _x.P, _x.D))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time is None:
        self.time = inertial_sense.msg.GTime()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 43
      (_x.time.time, _x.time.sec, _x.sat, _x.rcv, _x.SNR, _x.LLI, _x.code, _x.qualL, _x.qualP, _x.L, _x.P, _x.D,) = _get_struct_qd7B2df().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_qd7B2df().pack(_x.time.time, _x.time.sec, _x.sat, _x.rcv, _x.SNR, _x.LLI, _x.code, _x.qualL, _x.qualP, _x.L, _x.P, _x.D))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time is None:
        self.time = inertial_sense.msg.GTime()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 43
      (_x.time.time, _x.time.sec, _x.sat, _x.rcv, _x.SNR, _x.LLI, _x.code, _x.qualL, _x.qualP, _x.L, _x.P, _x.D,) = _get_struct_qd7B2df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_qd7B2df = None
def _get_struct_qd7B2df():
    global _struct_qd7B2df
    if _struct_qd7B2df is None:
        _struct_qd7B2df = struct.Struct("<qd7B2df")
    return _struct_qd7B2df
