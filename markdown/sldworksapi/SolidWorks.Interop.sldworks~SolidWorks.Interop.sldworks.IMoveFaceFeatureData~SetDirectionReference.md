---
title: "SetDirectionReference Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "SetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetDirectionReference.html"
---

# SetDirectionReference Method (IMoveFaceFeatureData)

Sets the direction reference for the Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDirectionReference( _
   ByVal LpDispatch As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim LpDispatch As System.Object
Dim value As System.Boolean

value = instance.SetDirectionReference(LpDispatch)
```

### C#

```csharp
System.bool SetDirectionReference(
   System.object LpDispatch
)
```

### C++/CLI

```cpp
System.bool SetDirectionReference(
   System.Object^ LpDispatch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpDispatch`: Direction reference:

  - If a translated, then a [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), [planar face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [linear edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), or [reference axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)
  - If rotated, then a [linear edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [reference axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html)

### Return Value

True if the direction reference is set, false if not

## VBA Syntax

See [MoveFaceFeatureData::SetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~SetDirectionReference.html).

## Examples

[Change Direction Reference of Move Face Feature (VBA)](Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm)

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetDirectionReference.html)
[IMoveFaceFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ReverseDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
