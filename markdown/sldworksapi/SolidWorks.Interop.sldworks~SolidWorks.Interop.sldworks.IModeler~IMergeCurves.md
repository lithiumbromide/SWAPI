---
title: "IMergeCurves Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IMergeCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMergeCurves.html"
---

# IMergeCurves Method (IModeler)

Merges multiple curves into one curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMergeCurves( _
   ByVal CurveCount As System.Integer, _
   ByRef CurveArr As Curve _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CurveCount As System.Integer
Dim CurveArr As Curve
Dim value As Curve

value = instance.IMergeCurves(CurveCount, CurveArr)
```

### C#

```csharp
Curve IMergeCurves(
   System.int CurveCount,
   ref Curve CurveArr
)
```

### C++/CLI

```cpp
Curve^ IMergeCurves(
   System.int CurveCount,
   Curve^% CurveArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveCount`: Number of curves to merge
- `CurveArr`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to merge

### Return Value

Newly created merged [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) or NULL if merge fails

## VBA Syntax

See [Modeler::IMergeCurves](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IMergeCurves.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::MergeCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MergeCurves.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
