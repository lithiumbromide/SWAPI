---
title: "ISetReferencePoints Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ISetReferencePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.html"
---

# ISetReferencePoints Method (IDimension)

Sets the reference points for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetReferencePoints( _
   ByVal PointsCount As System.Integer, _
   ByRef RefPoints As MathPoint _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim PointsCount As System.Integer
Dim RefPoints As MathPoint

instance.ISetReferencePoints(PointsCount, RefPoints)
```

### C#

```csharp
void ISetReferencePoints(
   System.int PointsCount,
   ref MathPoint RefPoints
)
```

### C++/CLI

```cpp
void ISetReferencePoints(
   System.int PointsCount,
   MathPoint^% RefPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointsCount`: Number of reference points for this dimension
- `RefPoints`: Pointer to the [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object

## VBA Syntax

See [Dimension::ISetReferencePoints](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ISetReferencePoints.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::IGetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.html)
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.html)
[IDimension::GetReferencePointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
