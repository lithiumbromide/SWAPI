---
title: "ImprintCurve Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "ImprintCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.html"
---

# ImprintCurve Method (IFace2)

Imprints a curve on the selected face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ImprintCurve( _
   ByVal Curve As System.Object, _
   ByRef NewEdges As System.Object, _
   ByRef NewFaces As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Curve As System.Object
Dim NewEdges As System.Object
Dim NewFaces As System.Object

instance.ImprintCurve(Curve, NewEdges, NewFaces)
```

### C#

```csharp
void ImprintCurve(
   System.object Curve,
   out System.object NewEdges,
   out System.object NewFaces
)
```

### C++/CLI

```cpp
void ImprintCurve(
   System.Object^ Curve,
   [Out] System.Object^ NewEdges,
   [Out] System.Object^ NewFaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve`: [Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to imprint on the face
- `NewEdges`: Array of new [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) created by the imprinted curve
- `NewFaces`: Array of new [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) created by the imprinted curve

## VBA Syntax

See [Face2::ImprintCurve](ms-its:sldworksapivb6.chm::/sldworks~Face2~ImprintCurve.html).

## Remarks

The specified curve must lie on the face.

To imprint a curve on a new face of a temporary body, create a copy of the original curve and imprint the copy of the curve on the new face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IImprintCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve.html)
[IFace2::ImprintCurveCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
