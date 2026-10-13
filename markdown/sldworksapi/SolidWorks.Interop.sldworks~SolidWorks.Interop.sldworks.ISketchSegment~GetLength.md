---
title: "GetLength Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetLength.html"
---

# GetLength Method (ISketchSegment)

Gets the length of this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLength() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Double

value = instance.GetLength()
```

### C#

```csharp
System.double GetLength()
```

### C++/CLI

```cpp
System.double GetLength();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sketch segment length

## VBA Syntax

See [SketchSegment::GetLength](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetLength.html).

## Examples

[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
