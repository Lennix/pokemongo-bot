# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Map/Fort/FortRenderingType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Map/Fort/FortRenderingType.proto',
  package='POGOProtos.Map.Fort',
  syntax='proto3',
  serialized_pb=_b('\n Map/Fort/FortRenderingType.proto\x12\x13POGOProtos.Map.Fort*3\n\x11\x46ortRenderingType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x11\n\rINTERNAL_TEST\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FORTRENDERINGTYPE = _descriptor.EnumDescriptor(
  name='FortRenderingType',
  full_name='POGOProtos.Map.Fort.FortRenderingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TEST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=57,
  serialized_end=108,
)
_sym_db.RegisterEnumDescriptor(_FORTRENDERINGTYPE)

FortRenderingType = enum_type_wrapper.EnumTypeWrapper(_FORTRENDERINGTYPE)
DEFAULT = 0
INTERNAL_TEST = 1


DESCRIPTOR.enum_types_by_name['FortRenderingType'] = _FORTRENDERINGTYPE


# @@protoc_insertion_point(module_scope)
