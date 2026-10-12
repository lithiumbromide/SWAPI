---
title: "GetCurve Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "GetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetCurve.html"
---

# GetCurve Method (ISilhouetteEdge)

Gets the curve for this silhouette edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISilhouetteEdge
Dim value As Curve

value = instance.GetCurve()
```

### C#

```csharp
Curve GetCurve()
```

### C++/CLI

```cpp
Curve^ GetCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [SilhouetteEdge::GetCurve](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~GetCurve.html).

## Remarks

After getting the curve, then you can create annotations on that curve.

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)
[ISilhouetteEdge::GetEndPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetEndPoint.html)
[ISilhouetteEdge::GetStartPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetStartPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
