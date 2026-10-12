---
title: "GetEndPoint Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "GetEndPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetEndPoint.html"
---

# GetEndPoint Method (ISilhouetteEdge)

Gets the end point of this silhouette edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndPoint() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISilhouetteEdge
Dim value As MathPoint

value = instance.GetEndPoint()
```

### C#

```csharp
MathPoint GetEndPoint()
```

### C++/CLI

```cpp
MathPoint^ GetEndPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[End point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [SilhouetteEdge::GetEndPoint](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~GetEndPoint.html).

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)
[ISilhouetteEdge::GetStartPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetStartPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
