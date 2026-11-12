---
title: "GetEdgesCount Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "GetEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdgesCount.html"
---

# GetEdgesCount Method (ISketchRegion)

Gets the number of edges for this sketch region.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
Dim value As System.Integer

value = instance.GetEdgesCount()
```

### C#

```csharp
System.int GetEdgesCount()
```

### C++/CLI

```cpp
System.int GetEdgesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [SketchRegion::GetEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~GetEdgesCount.html).

## Remarks

Call this method before calling [ISketchRegion::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion~IGetEdges.html) to get the size of the array for that method.

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
[ISketchRegion::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
