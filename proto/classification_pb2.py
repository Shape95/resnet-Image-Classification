# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classification.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63lassification.proto\x12\x1fmaum.brain.classification.cifar\"\x16\n\x05Input\x12\r\n\x05image\x18\x01 \x01(\x0c\"E\n\x06Output\x12;\n\x06result\x18\x01 \x01(\x0e\x32+.maum.brain.classification.cifar.CifarClass\"\x1b\n\x0bSampleInput\x12\x0c\n\x04text\x18\x01 \x01(\x0c\"\x1e\n\x0cSampleOutput\x12\x0e\n\x06result\x18\x01 \x01(\x05*z\n\nCifarClass\x12\x0c\n\x08\x41IRPLANE\x10\x00\x12\x0e\n\nAUTOMOBILE\x10\x01\x12\x08\n\x04\x42IRD\x10\x02\x12\x07\n\x03\x43\x41T\x10\x03\x12\x08\n\x04\x44\x45\x45R\x10\x04\x12\x07\n\x03\x44OG\x10\x05\x12\x08\n\x04\x46ROG\x10\x06\x12\t\n\x05HORSE\x10\x07\x12\x08\n\x04SHIP\x10\x08\x12\t\n\x05TRUCK\x10\t2\xe0\x01\n\x0e\x43lassification\x12n\n\rGetTextResult\x12,.maum.brain.classification.cifar.SampleInput\x1a-.maum.brain.classification.cifar.SampleOutput(\x01\x12^\n\tGetResult\x12&.maum.brain.classification.cifar.Input\x1a\'.maum.brain.classification.cifar.Output(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'classification_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CIFARCLASS._serialized_start=213
  _CIFARCLASS._serialized_end=335
  _INPUT._serialized_start=57
  _INPUT._serialized_end=79
  _OUTPUT._serialized_start=81
  _OUTPUT._serialized_end=150
  _SAMPLEINPUT._serialized_start=152
  _SAMPLEINPUT._serialized_end=179
  _SAMPLEOUTPUT._serialized_start=181
  _SAMPLEOUTPUT._serialized_end=211
  _CLASSIFICATION._serialized_start=338
  _CLASSIFICATION._serialized_end=562
# @@protoc_insertion_point(module_scope)