---
title: "SetDirectionReference Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDirectionReference.html"
---

# SetDirectionReference Method (IExtrudeFeatureData2)

Sets the direction of the extrusion.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirectionReference( _
   ByVal Ref1 As System.Object, _
   ByVal Ref2 As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Ref1 As System.Object
Dim Ref2 As System.Object

instance.SetDirectionReference(Ref1, Ref2)
```

### C#

```csharp
void SetDirectionReference(
   System.object Ref1,
   System.object Ref2
)
```

### C++/CLI

```cpp
void SetDirectionReference(
   System.Object^ Ref1,
   System.Object^ Ref2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ref1`: First reference entity
- `Ref2`: Second reference entity

## VBA Syntax

See [ExtrudeFeatureData2::SetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetDirectionReference.html).

## Remarks

Sometimes one reference entity can sufficiently define a direction; for example, an edge or axis. Other times, two reference entities are required to define a direction; for example, two vertices or two sketch points.

| If... | Then... |
| --- | --- |
| One reference entity can sufficiently define the direction | Ref2 is NULL |
| Two reference entities are required to define the direction | Both Ref1 and Ref2 are non-NULL |

Valid reference entities for Type1 and Type2:

- line segment
- edge
- axis
- vertex
- face
- plane
- sketch point

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.html)
[IExtrudeFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
