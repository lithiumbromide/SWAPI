---
title: "GetStartPoint Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "GetStartPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetStartPoint.html"
---

# GetStartPoint Method (ISilhouetteEdge)

Gets the start point of this silhouette edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStartPoint() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISilhouetteEdge
Dim value As MathPoint

value = instance.GetStartPoint()
```

### C#

```csharp
MathPoint GetStartPoint()
```

### C++/CLI

```cpp
MathPoint^ GetStartPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Start point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [SilhouetteEdge::GetStartPoint](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~GetStartPoint.html).

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)
[ISilhouetteEdge::GetEndPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetEndPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
