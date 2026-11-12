---
title: "IImprintCurve Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IImprintCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve.html"
---

# IImprintCurve Method (IFace2)

Imprints a curve on the selected face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IImprintCurve( _
   ByVal Curve As Curve, _
   ByVal NewEdgeCount As System.Integer, _
   ByRef NewEdges As Edge, _
   ByVal NewFaceCount As System.Integer, _
   ByRef NewFaces As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Curve As Curve
Dim NewEdgeCount As System.Integer
Dim NewEdges As Edge
Dim NewFaceCount As System.Integer
Dim NewFaces As Face2

instance.IImprintCurve(Curve, NewEdgeCount, NewEdges, NewFaceCount, NewFaces)
```

### C#

```csharp
void IImprintCurve(
   Curve Curve,
   System.int NewEdgeCount,
   out Edge NewEdges,
   System.int NewFaceCount,
   out Face2 NewFaces
)
```

### C++/CLI

```cpp
void IImprintCurve(
   Curve^ Curve,
   System.int NewEdgeCount,
   [Out] Edge^ NewEdges,
   System.int NewFaceCount,
   [Out] Face2^ NewFaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve`: Pointer to the [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to imprint on the face
- `NewEdgeCount`: Number of new edges to create
- `NewEdges`: Array of new [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) created by the imprinted curve of size NewEdgeCount
- `NewFaceCount`: Number of new faces to create
- `NewFaces`: Array of new [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) created by the imprinted curve of size NewFaceCount

## VBA Syntax

See [Face2::IImprintCurve](ms-its:sldworksapivb6.chm::/sldworks~Face2~IImprintCurve.html).

## Remarks

Before calling this method, call [IFace2::ImprintCurveCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ImprintCurveCount.html) to get the size of the arrays.

The specified curve must lie on the face.

To imprint a curve on a new face of a temporary body, create a copy of the original curve and imprint the copy of the curve on the new face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::ImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
