---
title: "GetFace Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "GetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetFace.html"
---

# GetFace Method (ISilhouetteEdge)

Gets the face for this silhouette edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISilhouetteEdge
Dim value As Face2

value = instance.GetFace()
```

### C#

```csharp
Face2 GetFace()
```

### C++/CLI

```cpp
Face2^ GetFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SilhouetteEdge::GetFace](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~GetFace.html).

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
