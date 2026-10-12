---
title: "Transform Parts and Bodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/ProgrammersGuide/Transform_Parts_and_Bodies.htm"
---

# Transform Parts and Bodies

A transform ([eDTransform3d](../eDTransform3d/eDTransform3d_Class.htm)) contains rotation matrix ([eDMatrix3d](../eDMatrix3d/eDMatrix3d_Class.htm)), translation vector ([eDPt3d](../eDPt3d/eDPt3d_Class.htm)), scale value, and Boolean values that describe other properties of the transform.

Within a part or an assembly, set part transforms with eDTransform3d objects. Within a part, set body transforms with eDTransform3d objects before or after adding them to parts. All pointers remain valid.
