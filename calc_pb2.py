# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\"\x18\n\x06Number\x12\x0e\n\x06number\x18\x01 \x01(\x02\"-\n\tNumberTwo\x12\x0f\n\x07number1\x18\x01 \x01(\x02\x12\x0f\n\x07number2\x18\x02 \x01(\x02\x32\xaa\x01\n\nCalculator\x12\x1d\n\x06getSum\x12\n.NumberTwo\x1a\x07.Number\x12!\n\ngetProduct\x12\n.NumberTwo\x1a\x07.Number\x12\x1e\n\x07getDiff\x12\n.NumberTwo\x1a\x07.Number\x12\x1d\n\x06getDiv\x12\n.NumberTwo\x1a\x07.Number\x12\x1b\n\x07getSqrt\x12\x07.Number\x1a\x07.Numberb\x06proto3')



_NUMBER = DESCRIPTOR.message_types_by_name['Number']
_NUMBERTWO = DESCRIPTOR.message_types_by_name['NumberTwo']
Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)

NumberTwo = _reflection.GeneratedProtocolMessageType('NumberTwo', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERTWO,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:NumberTwo)
  })
_sym_db.RegisterMessage(NumberTwo)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMBER._serialized_start=14
  _NUMBER._serialized_end=38
  _NUMBERTWO._serialized_start=40
  _NUMBERTWO._serialized_end=85
  _CALCULATOR._serialized_start=88
  _CALCULATOR._serialized_end=258
# @@protoc_insertion_point(module_scope)
