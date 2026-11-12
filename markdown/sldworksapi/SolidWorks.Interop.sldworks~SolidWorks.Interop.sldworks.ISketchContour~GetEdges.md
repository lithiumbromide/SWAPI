---
title: "GetEdges Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.html"
---

# GetEdges Method (ISketchContour)

Gets the edges in this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
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

Array of the [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SketchContour::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~GetEdges.html).

## Examples

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdgesCount.html)
[ISketchContour::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
