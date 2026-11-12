---
title: "GetSketch Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketch.html"
---

# GetSketch Method (ISketchSegment)

Gets the sketch for the current sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As Sketch

value = instance.GetSketch()
```

### C#

```csharp
Sketch GetSketch()
```

### C++/CLI

```cpp
Sketch^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchSegment::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetSketch.html).

## Examples

[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)
[Get Whether Sketch Segment Is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)
[Insert Hatch (VBA)](Insert_Hatch_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
