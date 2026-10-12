---
title: "SetDirectionReference Method (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "SetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetDirectionReference.html"
---

# SetDirectionReference Method (ISimpleHoleFeatureData2)

Sets the direction of the cut extrude for this simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDirectionReference( _
   ByVal Ref1 As System.Object, _
   ByVal Ref2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim Ref1 As System.Object
Dim Ref2 As System.Object
Dim value As System.Boolean

value = instance.SetDirectionReference(Ref1, Ref2)
```

### C#

```csharp
System.bool SetDirectionReference(
   System.object Ref1,
   System.object Ref2
)
```

### C++/CLI

```cpp
System.bool SetDirectionReference(
   System.Object^ Ref1,
   System.Object^ Ref2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ref1`: First reference entity (see **Remarks**)
- `Ref2`: Second reference entity (see **Remarks**)

### Return Value

True if the direction for the cut is set, false if not

## VBA Syntax

See [SimpleHoleFeatureData2::SetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~SetDirectionReference.html).

## Remarks

Sometimes one reference entity defines a direction; for example, an edge or axis. Other times, two reference entities define a direction; for example, two vertices or two sketch points.

Valid reference entities for Ref1 and Ref2:

- line segment
- edge
- axis
- vertex
- face
- plane
- sketch point

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetDirectionReference.html)
[ISimpleHoleFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseDirection.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
