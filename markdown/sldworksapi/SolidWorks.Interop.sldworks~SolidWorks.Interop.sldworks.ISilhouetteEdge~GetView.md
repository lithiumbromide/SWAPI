---
title: "GetView Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "GetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~GetView.html"
---

# GetView Method (ISilhouetteEdge)

Gets the drawing view for this silhouette edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As ISilhouetteEdge
Dim value As View

value = instance.GetView()
```

### C#

```csharp
View GetView()
```

### C++/CLI

```cpp
View^ GetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [SilhouetteEdge::GetView](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~GetView.html).

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
