---
title: "Create and Destroy Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/ProgrammersGuide/Create_and_Destroy_Objects.htm"
---

# Create and Destroy Objects

To ensure the integrity of all objects that reference other objects, you cannot create objects using their constructors unless otherwise noted. Instead, use the object's Create methods to instantiate pointers to new objects. The exceptions to this rule are:

- [eDApplicationParams](../eDApplicationParams/eDapplicationParams_Class.htm)
- [eDHoleProperties](../eDHoleProperties/eDHoleProperties_Class.htm)
- [eDMassProperties](../eDMassProperties/eDMassProperties_Class.htm)
- [eDMatrix3d](../eDMatrix3d/eDMatrix3d_Class.htm)
- [eDPt3d](../eDPt3d/eDPt3d_Class.htm)
- [eDSerializerPararms](../eDSerializerParams/eDSerializerParams_Class.htm)
- [eDTransform3d](../eDTransform3d/eDTransform3d_Class.htm)

Each of these classes have several public constructors.

Garbage collection is automatic through the destructors in the supported classes. Do not call delete on any pointer allocated by a Create method.
