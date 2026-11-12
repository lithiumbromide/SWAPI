---
title: "IGetContourEdges Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetContourEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.html"
---

# IGetContourEdges Method (ISketch)

Gets the edges for a sketch that has one contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetContourEdges( _
   ByRef Xform As System.Double, _
   ByVal EdgeCount As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Xform As System.Double
Dim EdgeCount As System.Integer
Dim value As Edge

value = instance.IGetContourEdges(Xform, EdgeCount)
```

### C#

```csharp
Edge IGetContourEdges(
   ref System.double Xform,
   System.int EdgeCount
)
```

### C++/CLI

```cpp
Edge^ IGetContourEdges(
   System.double% Xform,
   System.int EdgeCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xform`: Sketch entities, edges
- `EdgeCount`: Number of edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method supports sketches with one contour only. For sketches with multiple contours, use [ISketch::GetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchContours.html) or [ISketch::IGetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchContours.html) and then [ISketchContour::GetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~GetEdges.html) or [ISketchContour::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~IGetEdges.html).

To get the number of edges, call [ISketch::GetContourEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetContourEdgeCount.html) before calling this method.

Specifying the unit transform returns the edges in the space of the sketch.

If your application is expecting the returned edges to be in the context of the model's coordinate system, then xform should be the inverse of the transform returned by [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.html)
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
