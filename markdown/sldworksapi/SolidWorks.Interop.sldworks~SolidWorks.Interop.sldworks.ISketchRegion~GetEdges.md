---
title: "GetEdges Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdges.html"
---

# GetEdges Method (ISketchRegion)

Gets the edges on this sketch region.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
Dim value As System.Object

value = instance.GetEdges()
```

### C#

```csharp
System.object GetEdges()
```

### C++/CLI

```cpp
System.Object^ GetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SketchRegion::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~GetEdges.html).

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
[ISketchRegion::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdgesCount.html)
[ISketchRegion::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~IGetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
