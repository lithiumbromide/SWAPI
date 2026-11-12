---
title: "GetDirectionReference Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "GetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetDirectionReference.html"
---

# GetDirectionReference Method (IRuledSurfaceFeatureData)

Gets the direction of this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionReference( _
   ByRef Ref1 As System.Object, _
   ByRef Type1 As System.Integer, _
   ByRef Ref2 As System.Object, _
   ByRef Type2 As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim Ref1 As System.Object
Dim Type1 As System.Integer
Dim Ref2 As System.Object
Dim Type2 As System.Integer
Dim value As System.Integer

value = instance.GetDirectionReference(Ref1, Type1, Ref2, Type2)
```

### C#

```csharp
System.int GetDirectionReference(
   out System.object Ref1,
   out System.int Type1,
   out System.object Ref2,
   out System.int Type2
)
```

### C++/CLI

```cpp
System.int GetDirectionReference(
   [Out] System.Object^ Ref1,
   [Out] System.int Type1,
   [Out] System.Object^ Ref2,
   [Out] System.int Type2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ref1`: First reference entity (see **Remarks**)
- `Type1`: Type of reference entity as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)
- `Ref2`: Second reference entity (see **Remarks**)
- `Type2`: Type of reference entity as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)

### Return Value

Number of reference entities used to define the direction of the ruled surface (see **Remarks**)

## VBA Syntax

See [RuledSurfaceFeatureData::GetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~GetDirectionReference.html).

## Remarks

This method is only available when [IRuledSurfaceFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~Type.html) is set to swRuledSurfaceType_TaperedToVector, swRuledSurfaceType_PerpendicularToVector, or swRuledSurfaceType_Sweep.

Sometimes one reference entity defines a direction; for example, an edge or axis. Other times, two reference entities define a direction; for example, two vertices or two sketch points.

| If... | Then... |
| --- | --- |
| One reference entity defined the direction | Ref2 is NULL and the return value is 1 |
| Two reference entities defined the direction | Both Ref1 and Ref2 are non-NULL and the return value is 2 |

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
[IRuledSurfaceFeatureData::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetDirectionReference.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
