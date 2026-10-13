---
title: "MergeCurves Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "MergeCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MergeCurves.html"
---

# MergeCurves Method (IModeler)

Merges multiple curves into one curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function MergeCurves( _
   ByVal CurveVar As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CurveVar As System.Object
Dim value As Curve

value = instance.MergeCurves(CurveVar)
```

### C#

```csharp
Curve MergeCurves(
   System.object CurveVar
)
```

### C++/CLI

```cpp
Curve^ MergeCurves(
   System.Object^ CurveVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveVar`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to merge

### Return Value

Newly created merged [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) or Nothing if merge fails

## VBA Syntax

See [Modeler::MergeCurves](ms-its:sldworksapivb6.chm::/sldworks~Modeler~MergeCurves.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IMergeCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMergeCurves.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
