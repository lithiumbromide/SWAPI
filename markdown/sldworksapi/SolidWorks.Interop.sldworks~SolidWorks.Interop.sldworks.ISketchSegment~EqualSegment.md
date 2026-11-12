---
title: "EqualSegment Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "EqualSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~EqualSegment.html"
---

# EqualSegment Method (ISketchSegment)

Divides this sketch segment into equally spaced sketch segments or points.

## Syntax

### Visual Basic (Declaration)

```vb
Function EqualSegment( _
   ByVal SketchType As System.Integer, _
   ByVal SegmentPoints As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim SketchType As System.Integer
Dim SegmentPoints As System.Integer
Dim value As System.Boolean

value = instance.EqualSegment(SketchType, SegmentPoints)
```

### C#

```csharp
System.bool EqualSegment(
   System.int SketchType,
   System.int SegmentPoints
)
```

### C++/CLI

```cpp
System.bool EqualSegment(
   System.int SketchType,
   System.int SegmentPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SketchType`: Type of entity with which to divide this sketch segment as defined in [swSketchSegmentType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSegmentType_e.html)
- `SegmentPoints`: 2 <= Number of sketchType entities into which to divide this sketch segment <= 100

### Return Value

True if successful, false if not

## VBA Syntax

See [SketchSegment::EqualSegment](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~EqualSegment.html).

## Examples

[Divide Sketch Segment (VBA)](Divide_Sketch_Segment_Example_VB.htm)
[Divide Sketch Segment (VB.NET)](Divide_Sketch_Segment_Example_VBNET.htm)
[Divide Sketch Segment (C#)](Divide_Sketch_Segment_Example_CSharp.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
