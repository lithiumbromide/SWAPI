---
title: "IEnumSketchPoints Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IEnumSketchPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.html"
---

# IEnumSketchPoints Method (ISketch)

Gets the sketch points enumeration in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEnumSketchPoints() As EnumSketchPoints
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As EnumSketchPoints

value = instance.IEnumSketchPoints()
```

### C#

```csharp
EnumSketchPoints IEnumSketchPoints()
```

### C++/CLI

```cpp
EnumSketchPoints^ IEnumSketchPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch points enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchPoints.html)

## VBA Syntax

See [Sketch::IEnumSketchPoints](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IEnumSketchPoints.html).

## Examples

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.html)
[ISketch::GetSketchPointsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPointsCount2.html)
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.html)
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.html)
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html)

## Availability

SOLIDWORKS 99, datecode 1999207
