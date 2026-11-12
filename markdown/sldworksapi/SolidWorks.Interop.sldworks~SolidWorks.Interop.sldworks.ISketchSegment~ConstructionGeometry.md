---
title: "ConstructionGeometry Property (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "ConstructionGeometry"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~ConstructionGeometry.html"
---

# ConstructionGeometry Property (ISketchSegment)

Gets or sets whether this sketch segment is construction geometry, for example, a centerline for a feature revolve operation.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConstructionGeometry As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Boolean

instance.ConstructionGeometry = value

value = instance.ConstructionGeometry
```

### C#

```csharp
System.bool ConstructionGeometry {get; set;}
```

### C++/CLI

```cpp
property System.bool ConstructionGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this sketch segment is construction geometry, false if not

## VBA Syntax

See [SketchSegment::ConstructionGeometry](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~ConstructionGeometry.html).

## Examples

[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)
[Get Whether Sketch Segment Is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
