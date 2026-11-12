---
title: "GetSketchSlot Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetSketchSlot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchSlot.html"
---

# GetSketchSlot Method (ISketchSegment)

Gets sketch slot with which this sketch segment is associated.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSlot() As SketchSlot
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As SketchSlot

value = instance.GetSketchSlot()
```

### C#

```csharp
SketchSlot GetSketchSlot()
```

### C++/CLI

```cpp
SketchSlot^ GetSketchSlot();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch slot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot.html) if the sketch segment is associated with a sketch slot, or null if the sketch segment is not associated with a sketch slot

## VBA Syntax

See [SketchSegment::GetSketchSlot](ms-its:sldworksapivb6.chm::/Sldworks~SketchSegment~GetSketchSlot.html).

## Examples

[Get Sketch Slot Using Sketch Point and Segment (C#)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_CSharp.htm)
[Get Sketch Slot Using Sketch Point and Segment (VB.NET)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm)
[Get Sketch Slot Using Sketch Point and Segment (VBA)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
