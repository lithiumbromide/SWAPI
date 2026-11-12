---
title: "GetDirectionReference Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetDirectionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.html"
---

# GetDirectionReference Method (IExtrudeFeatureData2)

Gets the direction of the extrusion.

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
Dim instance As IExtrudeFeatureData2
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

- `Ref1`: First reference entity
- `Type1`: Type of reference entity as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)
- `Ref2`: Second reference entity
- `Type2`: Type of reference entity as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Number of reference entities used to define the direction of the extrusion

## VBA Syntax

See [ExtrudeFeatureData2::GetDirectionReference](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetDirectionReference.html).

## Remarks

Sometimes one reference entity defines a direction; for example, an edge or axis. Other times, two reference entities define a direction; for example, two vertices or two sketch points.

| If... | Then... |
| --- | --- |
| One reference entity defined the direction | Ref2 is NULL and the return value is 1 |
| Two reference entities defined the direction | Both Ref1 and Ref2 are non-NULL and the return value is 2 |

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
[IExtrudeFeatureData2::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDirectionReference.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
