---
title: "ImprintCurveCount Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "ImprintCurveCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount.html"
---

# ImprintCurveCount Method (IFace2)

Gets the number of new edges and faces to create when imprinting a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ImprintCurveCount( _
   ByVal Curve As Curve, _
   ByRef NewEdgeCount As System.Integer, _
   ByRef NewFaceCount As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Curve As Curve
Dim NewEdgeCount As System.Integer
Dim NewFaceCount As System.Integer

instance.ImprintCurveCount(Curve, NewEdgeCount, NewFaceCount)
```

### C#

```csharp
void ImprintCurveCount(
   Curve Curve,
   out System.int NewEdgeCount,
   out System.int NewFaceCount
)
```

### C++/CLI

```cpp
void ImprintCurveCount(
   Curve^ Curve,
   [Out] System.int NewEdgeCount,
   [Out] System.int NewFaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve`: Pointer to the [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `NewEdgeCount`: Number of new edges to create when imprinting this curve
- `NewFaceCount`: Number of new faces to create when imprinting this curve

## VBA Syntax

See [Face2::ImprintCurveCount](ms-its:sldworksapivb6.chm::/sldworks~Face2~ImprintCurveCount.html).

## Remarks

Call this method before calling [IFace2::IImprintCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IImprintCurve.html) to get the size of the edges and faces arrays.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::ImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
