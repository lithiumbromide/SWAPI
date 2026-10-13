---
title: "IGetEdges Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges.html"
---

# IGetEdges Method (ISketchContour)

Gets the edges in this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetEdges(Count)
```

### C#

```csharp
Edge IGetEdges(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetEdges(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of the [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchContour::GetEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~GetEdgesCount.html) to get the value for Count.

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
