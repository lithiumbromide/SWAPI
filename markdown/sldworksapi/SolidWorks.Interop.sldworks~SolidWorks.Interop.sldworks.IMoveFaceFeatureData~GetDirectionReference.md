---
title: "GetDirectionReference Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "GetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetDirectionReference.html"
---

# GetDirectionReference Method (IMoveFaceFeatureData)

Gets the direction reference for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionReference( _
   ByRef DirRefType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim DirRefType As System.Integer
Dim value As System.Object

value = instance.GetDirectionReference(DirRefType)
```

### C#

```csharp
System.object GetDirectionReference(
   out System.int DirRefType
)
```

### C++/CLI

```cpp
System.Object^ GetDirectionReference(
   [Out] System.int DirRefType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DirRefType`: Direction reference type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Direction reference:

- If a translated, then a [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), [planar face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [linear edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), or [reference axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)
- If rotated, then a [linear edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [reference axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [MoveFaceFeatureData::GetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~GetDirectionReference.html).

## Examples

[Change Direction Reference of Move Face Feature (VBA)](Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm)

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetDirectionReference.html)
[IMoveFaceFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ReverseDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
