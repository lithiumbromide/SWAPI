---
title: "SetDirectionReference Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "SetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetDirectionReference.html"
---

# SetDirectionReference Method (IRuledSurfaceFeatureData)

Sets the direction of the extrusion for this ruled-surface feature.

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
Dim instance As IRuledSurfaceFeatureData
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

- `Ref1`: First reference entity (see **Remarks**)
- `Ref2`: Second reference entity (see **Remarks**)

## VBA Syntax

See [RuledSurfaceFeatureData::SetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~SetDirectionReference.html).

## Remarks

Sometimes one reference entity can sufficiently define a direction; for example, an edge or axis. Other times, two reference entities are required to define a direction; for example, two vertices or two sketch points.

| If... | Then... |
| --- | --- |
| One reference entity can sufficiently define the direction | Ref2 is NULL |
| Two reference entities are required to define the direction | Both Ref1 and Ref2 are non-NULL |

Valid reference entities for type1 and type2:

- line segment
- edge
- axis
- vertex
- face
- plane
- sketch point

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetDirectionReference.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
