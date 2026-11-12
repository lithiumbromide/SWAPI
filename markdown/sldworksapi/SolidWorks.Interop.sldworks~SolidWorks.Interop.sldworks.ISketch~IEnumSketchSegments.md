---
title: "IEnumSketchSegments Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IEnumSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.html"
---

# IEnumSketchSegments Method (ISketch)

Gets the sketch segments enumeration in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEnumSketchSegments() As EnumSketchSegments
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As EnumSketchSegments

value = instance.IEnumSketchSegments()
```

### C#

```csharp
EnumSketchSegments IEnumSketchSegments()
```

### C++/CLI

```cpp
EnumSketchSegments^ IEnumSketchSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch segments enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchSegments.html)

## VBA Syntax

See [Sketch::IEnumSketchSegments](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IEnumSketchSegments.html).

## Examples

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

## Remarks

Sketch segments include line, arc, spline, parabola, and ellipse entities.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.html)
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.html)
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.html)

## Availability

SOLIDWORKS 99, datecode 1999207
