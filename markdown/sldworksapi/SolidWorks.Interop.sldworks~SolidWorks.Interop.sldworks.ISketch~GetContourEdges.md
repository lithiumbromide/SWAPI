---
title: "GetContourEdges Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetContourEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.html"
---

# GetContourEdges Method (ISketch)

Gets the edges for a sketch that has one contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContourEdges( _
   ByVal Xform As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Xform As System.Object
Dim value As System.Object

value = instance.GetContourEdges(Xform)
```

### C#

```csharp
System.object GetContourEdges(
   System.object Xform
)
```

### C++/CLI

```cpp
System.Object^ GetContourEdges(
   System.Object^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xform`: Array of size 16 doubles representing the transform

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [Sketch::GetContourEdges](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetContourEdges.html).

## Remarks

This method supports sketches with one contour only. For sketches with multiple contours, use [ISketch::GetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchContours.html) or [ISketch::IGetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchContours.html) and then [ISketchContour::GetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~GetEdges.html) or [ISketchContour::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~IGetEdges.html).

Specifying the unit transform returns the edges in the space of the sketch.

If your application is expecting the returned edges to be in the context of the model's coordinate system, then xform should be the inverse of the transform returned by [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetContourEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdgeCount.html)
[ISketch::IGetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.html)
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
