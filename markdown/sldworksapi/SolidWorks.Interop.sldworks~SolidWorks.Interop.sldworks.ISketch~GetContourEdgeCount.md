---
title: "GetContourEdgeCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetContourEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdgeCount.html"
---

# GetContourEdgeCount Method (ISketch)

Gets the number of edges for this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContourEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetContourEdgeCount()
```

### C#

```csharp
System.int GetContourEdgeCount()
```

### C++/CLI

```cpp
System.int GetContourEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [Sketch::GetContourEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetContourEdgeCount.html).

## Remarks

If the sketch contour is not closed or contains interior non-construction elements, this method returns 0.

Call this method before calling [ISketch::IGetContourEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetContourEdges.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
