---
title: "GetRelationType Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetRelationType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetRelationType.html"
---

# GetRelationType Method (ISketchRelation)

Gets the type of sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelationType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Integer

value = instance.GetRelationType()
```

### C#

```csharp
System.int GetRelationType()
```

### C++/CLI

```cpp
System.int GetRelationType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of sketch relation as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

## VBA Syntax

See [SketchRelation::GetRelationType](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetRelationType.html).

## Examples

[Get All Sketch Relations and Their Types (VBA)](Get_All_Sketch_Relations_and_Their_Types_Example_VB.htm)
[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
