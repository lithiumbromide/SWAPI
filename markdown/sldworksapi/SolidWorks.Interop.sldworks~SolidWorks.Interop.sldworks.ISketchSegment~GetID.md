---
title: "GetID Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetID.html"
---

# GetID Method (ISketchSegment)

Gets the for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Object

value = instance.GetID()
```

### C#

```csharp
System.object GetID()
```

### C++/CLI

```cpp
System.Object^ GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array with two longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch segment ID

## VBA Syntax

See [SketchSegment::GetID](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetID.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)
[Get Whether Sketch Segment is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## Remarks

The ID of the sketch segment:

- is an ordered pair (i1, i2). For the specific sketch segment type, for example, line, arc, spline, and so on), the combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each entity within a specific sketch has a unique ID. However, a sketch line may have the same ID values as a sketch arc within the same sketch. Likewise, in a second sketch, you may find a different sketch element with the same ID Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element id to uniquely identify a sketched item

You can determine the sketch element type by using [ISketchSegment::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetType.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::IGetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetID.html)

## Availability

SOLIDWORKS 99, datecode 1999207
