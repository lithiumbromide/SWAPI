---
title: "GetEdgesCount Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "GetEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdgesCount.html"
---

# GetEdgesCount Method (ISketchContour)

Gets the number of edges in this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
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

See [SketchContour::GetEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~GetEdgesCount.html).

## Remarks

Call this method before calling [ISketchContour::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~IGetEdges.html) to get the size of the array for that method.

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
